#!/usr/bin/env python3

import rospy
import sys
from robot_controllers import MobileBaseHandler

if __name__ == '__main__':
    # Get robot_id from launch file parameter



        # Retrieve robot_id using its full path
    # robot_name = rospy.get_name()  # Gets the node name like "/robot/robot1_move_service"
    robot_id_param = "robot_id"  # Construct the correct parameter path
    robot_id = rospy.get_param(robot_id_param)  # Use the full path

    # rospy.loginfo(f"Robot ID: {robot_id}")
    # robot_id = rospy.get_param("~robot_id")
    
    # init_pose_x = rospy.get_param("~init_pose_x", 76.67)
    # init_pose_y = rospy.get_param("~init_pose_y", 5)
    # init_pose_z = rospy.get_param("~init_pose_z", 0)

    # rospy.init_node(f'{robot_id}_mobilebase_controller', anonymous=True)

    # init_pose = [float(init_pose_x), float(init_pose_y), float(init_pose_z)])

    if not robot_id:
        rospy.logerr("No robot_id provided! Use _robot_id:=robotX in the launch file.")
        sys.exit(1)

    try:
        handler = MobileBaseHandler(robot_id)
        handler.run()
    except rospy.ROSInterruptException:
        rospy.loginfo(f"Robot {robot_id} Controller shutting down")