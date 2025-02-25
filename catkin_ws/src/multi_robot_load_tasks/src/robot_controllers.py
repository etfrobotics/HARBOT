#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from mobile_manipulation.srv import MoveTask, MoveTaskRequest, MoveTaskResponse
from mobile_manipulation.srv import PickPlaceTask, PickPlaceTaskRequest, PickPlaceTaskResponse

import moveit_commander
from geometry_msgs.msg import PoseWithCovarianceStamped, PoseStamped
from mobile_manipulation.srv import PickPlaceTask, PickPlaceTaskResponse 
import sys
import numpy as np

from nav_msgs.msg import Odometry  # For robot position
from actionlib_msgs.msg import GoalStatusArray  # For move_base status messages


class RobotController:
    def __init__(self, robot_id):
        rospy.init_node(f'{robot_id}_controller', anonymous=True)
        self.robot_id = robot_id

        # Subscribe to the robot's plan topic
        rospy.Subscriber(f'/{robot_id}/plan', String, self.plan_callback)

        # Initialize services for move and pick-place
        self.move_service = rospy.ServiceProxy(f'/{robot_id}/move_task_service', MoveTask)
        self.pickplace_service = rospy.ServiceProxy(f'/{robot_id}/pickplace_service', PickPlaceTask)

        rospy.loginfo(f"{robot_id} Controller initialized")

    def plan_callback(self, msg): 
        """Executes the received plan."""
        tasks = msg.data.strip().split("\n")
        for task in tasks:
            args = task.strip().split()
            if args[0] == "MOVE":
                self.execute_move(args[1:])
            elif args[0] == "PICKPLACE":
                self.execute_pickplace(args[1:])
            else:
                rospy.logwarn(f"Unknown command for {self.robot_id}: {task}")

            # Task execution is often T >> 1 seconds, so the sleep param doesnt hinder program flexibility.
            # The exectuion needs to be paused so that the robot states can be updated across the nodes.
            rospy.sleep(2)

    def execute_move(self, args):
        """Calls the move service with provided parameters."""
        move_request = MoveTaskRequest(*[float(a) for a in args])
        response = self.move_service(move_request)
        rospy.loginfo(f"MOVE executed for {self.robot_id}: {response.message}")

    def execute_pickplace(self, args):
        """Calls the pick-place service with provided parameters."""
        pickplace_request = PickPlaceTaskRequest(*[float(a) for a in args])
        response = self.pickplace_service(pickplace_request)
        rospy.loginfo(f"PICKPLACE executed for {self.robot_id}: {response.message}")
    
    def run(self):
        rospy.loginfo(f"{self.robot_id} controller is running")
        rospy.spin()


class ManipulationHandler:
    def __init__(self, robot_id):
        rospy.init_node(f'{robot_id}_manipulation_handler', anonymous=True)
        self.robot_id = robot_id
        
        # 0.0104 0.842 1.124 # Pos
        # -0.5753 -0.411 0.586 0.3955 # Ori
        # Initialize MoveIt Commander
        moveit_commander.roscpp_initialize(sys.argv)
        self.robot = moveit_commander.RobotCommander(robot_description=f'/{robot_id}/robot_description', ns=self.robot_id)
        self.group = moveit_commander.MoveGroupCommander("ur5_arm", robot_description=f'/{robot_id}/robot_description', ns=self.robot_id)

        # self.finished_pub = rospy.Publisher('/finished_stream', String, queue_size=10)

        # Create a service for pick-and-place tasks
        self.service = rospy.Service(f'/{robot_id}/pickplace_service', PickPlaceTask, self.handle_pickplace_task)

        rospy.loginfo("ManipulationHandler initialized and ready for tasks")

    def handle_pickplace_task(self, req):
        """Handles the pick-and-place task via service request."""
        try:
            # Extract start and end poses from the request
            start_pose = [req.start_x, req.start_y, req.start_z, req.start_qx, req.start_qy, req.start_qz, req.start_qw]
            end_pose = [req.end_x, req.end_y, req.end_z, req.end_qx, req.end_qy, req.end_qz, req.end_qw]

            # Move to the start position
            self.move_arm_to(start_pose)
            print("prosao start")

            # Move to the end position
            self.move_arm_to(end_pose)

            # Publish task completion
            # self.finished_pub.publish(f"PICKPLACE_COMPLETED {req.start_x} {req.start_y} {req.end_x} {req.end_y}")
            rospy.loginfo("Pick-and-place task completed")

            return PickPlaceTaskResponse(success=True, message="Task completed successfully")
        except Exception as e:
            rospy.logerr(f"Error during pick-and-place task: {e}")
            return PickPlaceTaskResponse(success=False, message=str(e))

    def move_arm_to(self, pose_data):
        """Moves the robotic arm to the specified pose."""
        pose = PoseStamped()
        pose.header.frame_id = "robot_base_footprint"
        pose.header.stamp = rospy.Time.now()
        pose.pose.position.x, pose.pose.position.y, pose.pose.position.z = pose_data[:3]
        pose.pose.orientation.x, pose.pose.orientation.y, pose.pose.orientation.z, pose.pose.orientation.w = pose_data[3:]
        # print(pose)
        self.group.set_pose_target(pose)
        success = self.group.go(wait=True)
        if not success:
            raise Exception("Failed to move to the target pose")
        rospy.loginfo(f"Moved to pose: {pose.pose}")

    def run(self):
        rospy.loginfo("ManipulationHandler service is running")
        rospy.spin()

class MobileBaseHandler:
    def __init__(self, robot_id):
        rospy.init_node(f'{robot_id}_mobile_base_handler', anonymous=False)
        rospy.loginfo("MobileBaseHandler initialized")
        # self.finished_pub = rospy.Publisher('/finished_stream', String, queue_size=10)
        self.goal_pub = rospy.Publisher(f'/{robot_id}/move_base_simple/goal', PoseStamped, queue_size=10)


        self.status_sub = rospy.Subscriber(f'/{robot_id}/move_base/status', GoalStatusArray, self.status_callback)
        self.curr_position = rospy.Subscriber(f'/{robot_id}/amcl_pose', PoseWithCovarianceStamped, self.amcl_callback)
        

        # Create service
        self.service = rospy.Service(f'/{robot_id}/move_task_service', MoveTask, self.handle_move_task)
        self.ACTIVE = False
        self.delta_location = 100000000
        self.epsilon = 0.5
        self.robot_position = PoseWithCovarianceStamped()
        


    def status_callback(self, msg):
        for status in msg.status_list:

            # status 3 => Stopped
            # status 1 => Moving
            if status.status == 1: 
                self.ACTIVE = True
            else:
                self.ACTIVE = False

    def amcl_callback(self, msg):
        self.robot_position = msg

            
    

    def handle_move_task(self, req):
        try:
            x, y, z, qx, qy, qz, qw = req.x, req.y, req.z, req.qx, req.qy, req.qz, req.qw

            # Publish the goal position
            goal = PoseStamped()
            goal.header.stamp = rospy.Time.now()
            goal.header.frame_id = "robot_map"

            goal.pose.position.x = x
            goal.pose.position.y = y
            goal.pose.position.z = z

            goal.pose.orientation.x = qx
            goal.pose.orientation.y = qy
            goal.pose.orientation.z = qz
            goal.pose.orientation.w = qw

            rospy.loginfo(f"Moving robot to: {goal.pose}")
            self.goal_pub.publish(goal)
            rospy.sleep(1) # To make sure all the nodes are updated and that the state changes to ACTIVE 
            # This is bad, because if it takes a bit longer to update the state, the robot will not move,
            # It will run over the Blocker, and the task will be marked as completed, even though it is not. TODO: Fix this

            #IDEA: Add a TIMEOUT, and if the robot does not reach the goal in that time, Go to the next goal. 
            # -> to increase the robustness


            # Blocks the execution until the robot reaches the goal (A bit hacky)
            while not rospy.is_shutdown():

                self.delta_location = np.sqrt((self.robot_position.pose.pose.position.x - x)**2 + 
                                      (self.robot_position.pose.pose.position.y - y)**2)

                if self.ACTIVE == False and self.delta_location < self.epsilon:
                    break

                print("MOVEBASE BLOCKED")
                print(self.delta_location)
                rospy.sleep(1)
    
            return MoveTaskResponse(success=True, message="Task completed")
        except Exception as e:
            rospy.logerr(f"Error in handle_move_task: {e}")
            return MoveTaskResponse(success=False, message=str(e))

    def run(self):
        rospy.loginfo("MobileBaseHandler service is ready")
        rospy.spin()


# rosservice call /robot/pickplace_service "{start_x: -0.4, start_y: 0.0, start_z: 0.7, start_qx: -0.00192, start_qy: 0.98355, start_qz: -0.18062,
#   start_qw: 0.00037445, end_x: -0.5, end_y: 0.0, end_z: 0.7, end_qx: -0.0019288, end_qy: 0.98355, end_qz: -0.18062,
#   end_qw: 0.00037}" 
