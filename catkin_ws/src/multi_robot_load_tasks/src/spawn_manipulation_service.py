#!/usr/bin/env python3

import rospy
import sys
from robot_controllers import ManipulationHandler

if __name__ == '__main__':
    # Get robot_id from launch file parameter
    robot_id_param = "robot_id"  # Construct the correct parameter path
    robot_id = rospy.get_param(robot_id_param)  # Use the full path

    # rospy.loginfo(f"Robot ID: {robot_id}")


    if not robot_id:
        rospy.logerr("No robot_id provided! Use _robot_id:=robotX in the launch file.")
        sys.exit(1)

    try:
        rospy.sleep(5) # Wait for the MOVEIT to start
        handler = ManipulationHandler(robot_id)
        handler.run()
    except rospy.ROSInterruptException:
        rospy.loginfo(f"Robot {robot_id} Controller shutting down")