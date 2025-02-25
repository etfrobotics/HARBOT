#!/usr/bin/env python3

import rospy
import math
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry  # For robot position
from mobile_manipulation.srv import MoveTask, MoveTaskResponse  
from actionlib_msgs.msg import GoalStatusArray  # For move_base status messages

# killall -9 gazebo & killall -9 gzserver & killall -9 gzclient

class MobileBaseHandler:
    def __init__(self):
        rospy.init_node('mobile_base_handler', anonymous=False)
        rospy.loginfo("MobileBaseHandler initialized")
        self.finished_pub = rospy.Publisher('/finished_stream', String, queue_size=10)
        self.goal_pub = rospy.Publisher('/robot/move_base_simple/goal', PoseStamped, queue_size=10)

        self.robot_position = [0.0, 0.0, 0.0]
        self.position_threshold = 0.1  # Distance threshold in meters

        self.status_sub = rospy.Subscriber('/robot/move_base/status', GoalStatusArray, self.status_callback)

        # Create service
        self.service = rospy.Service('move_task_service', MoveTask, self.handle_move_task)
        self.goal_reached = False


    def status_callback(self, msg):
        for status in msg.status_list:
            if status.status == 3 and status.text == "Goal reached.":
                print("Menjam")
                self.goal_reached = True
                rospy.loginfo("Goal reached successfully.")
                return  # Exit loop after detecting goal reached

        # If no status with "Goal reached" is found, reset flag
        self.goal_reached = False

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

            # Wait until the robot is close to the target
            target_position = [x, y, z]
            rate = rospy.Rate(10)  # 10 Hz
    
            rospy.sleep(1) #TODO: debug this so that it doesnt run over the block to the response
            while not rospy.is_shutdown():
                if self.goal_reached:
                    break
                rate.sleep()

            # Publish task completion
            self.finished_pub.publish(f"MOVE_COMPLETED {x} {y}")
            rospy.loginfo("Move task completed")

            self.goal_reached=False
            return MoveTaskResponse(success=True, message="Task completed")
        except Exception as e:
            rospy.logerr(f"Error in handle_move_task: {e}")
            return MoveTaskResponse(success=False, message=str(e))

    def run(self):
        rospy.loginfo("MobileBaseHandler service is ready")
        rospy.spin()

if __name__ == '__main__':
    handler = MobileBaseHandler()
    try:
        handler.run()
    except rospy.ROSInterruptException:
        pass
