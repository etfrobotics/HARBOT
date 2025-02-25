#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import String

# Declare global variables
global task, x, y, z, qx, qy, qz, qw
dt = "MOVE 0.0 0.0 0.0 0.0 0.0 0.0 1.0"
task = dt.strip().split()
x, y, z, qx, qy, qz, qw = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0


def task_callback(data):
    global task, x, y, z, qx, qy, qz, qw  # Declare these variables as global
    task = data.data.strip().split()
    if task[0] == "MOVE":
        x, y, z, qx, qy, qz, qw = map(float, task[1:])
        # rospy.loginfo(f"Updated task to: {x}, {y}, {z}, {qx}, {qy}, {qz}, {qw}")


# Initialize the ROS node
rospy.init_node('move_robot_to_goal', anonymous=True)

# Define publishers and subscribers
goal_pub = rospy.Publisher('/robot/move_base_simple/goal', PoseStamped, queue_size=10)
finished_pub = rospy.Publisher('/finished_stream', String, queue_size=10)
task_sub = rospy.Subscriber('/task_stream', String, task_callback)

# Main loop
# rate = rospy.Rate(1)  # Set a rate of 1 Hz
while True:
    rospy.loginfo(f"x: {x}, y: {y}, z: {z}, qx: {qx}, qy: {qy}, qz: {qz}, qw: {qw}")

    goal = PoseStamped()
    goal.header.stamp = rospy.Time.now()
    goal.header.frame_id = "robot_map"  # or "odom" based on your setup
    goal.pose.position.x = x
    goal.pose.position.y = y
    goal.pose.position.z = z
    goal.pose.orientation.x = qx
    goal.pose.orientation.y = qy
    goal.pose.orientation.z = qz
    goal.pose.orientation.w = qw
    goal_pub.publish(goal)
    rospy.loginfo("Goal sent!")
    rospy.sleep(10) # needs to be changed to check if the distance has been reached
    finished_pub.publish(f"MOVE_COMPLETED {task[1]} {task[2]}")
    rospy.sleep(2)





