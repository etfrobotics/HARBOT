#!/usr/bin/env python3

import rospy
import moveit_commander
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
import sys


class ManipulationHandler:
    def __init__(self):
        rospy.init_node('manipulation_handler', anonymous=True)

        # rospy.sleep(5) # Waiting for the sim to load

        self.task_sub = rospy.Subscriber('/task_stream', String, self.task_callback)
        self.finished_pub = rospy.Publisher('/finished_stream', String, queue_size=10)
        moveit_commander.roscpp_initialize(sys.argv)
        self.robot = moveit_commander.RobotCommander(robot_description='/robot/robot_description', ns="robot")
        self.group = moveit_commander.MoveGroupCommander("ur5_arm", robot_description='/robot/robot_description', ns="robot")

        self.completed_flag = False

        #TODO: Dodati da robot ide u neku home poziciju

    def task_callback(self, msg):
        task = msg.data.strip().split()
        if task[0] == "PICKPLACE":
            self.handle_pickplace_task(task)

    def handle_pickplace_task(self, task):
        start = list(map(float, task[1:8]))
        end = list(map(float, task[8:]))
        self.move_arm_to(start)
        self.move_arm_to(end)
        self.finished_pub.publish(f"PICKPLACE_COMPLETED {task[1]} {task[2]} {task[8]} {task[9]}")
        rospy.loginfo("Pick and place task completed")
    
    def check_if_near_2_goal():
        pass

    def move_arm_to(self, pose_data):
        pose = PoseStamped()
        pose.header.frame_id = "robot_base_footprint"
        pose.header.stamp = rospy.Time.now()
        pose.pose.position.x, pose.pose.position.y, pose.pose.position.z = pose_data[:3]
        pose.pose.orientation.x, pose.pose.orientation.y, pose.pose.orientation.z, pose.pose.orientation.w = pose_data[3:]
        self.group.set_pose_target(pose)
        self.group.go(wait=True)
        # TODO: Add a condition which checks if the task has been completed
        # while(True):
        #     if self.check_if_near_2_goal():
        #         break
        #     else:
        #         pass 
        rospy.sleep(25) 

    def run(self):
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            rate.sleep()

if __name__ == '__main__':
    handler = ManipulationHandler()
    handler.run()
