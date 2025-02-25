#!/usr/bin/env python3

import rospy
import math
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry  # For robot position
from mobile_manipulation.srv import MoveTask, MoveTaskResponse  
from actionlib_msgs.msg import GoalStatusArray  # For move_base status messages

# killall -9 gazebo & killall -9 gzserver & killall -9 gzclient


rospy.init_node('mobile_base_handler', anonymous=False)
rospy.loginfo("MobileBaseHandler initialized")

goal_pub = rospy.Publisher('/robot/move_base_simple/goal', PoseStamped, queue_size=10)

# Publish the goal position
goal = PoseStamped()
goal.header.stamp = rospy.Time.now()
goal.header.frame_id = "robot_map"

goal.pose.position.x = 1
goal.pose.position.y = 0
goal.pose.position.z = 0

goal.pose.orientation.x = 0
goal.pose.orientation.y = 0
goal.pose.orientation.z = 0
goal.pose.orientation.w = 1

rospy.loginfo(f"Moving robot to: {goal.pose}")

goal_pub.publish(goal)

