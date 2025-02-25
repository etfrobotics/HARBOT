#!/usr/bin/env python3

import rospy
import sys
from robot_controllers import RobotController

if __name__ == '__main__':
    # rospy.init_node('spawn_robot', anonymous=True)

    # Get robot_id from launch file parameter
    robot_id = rospy.get_param("~robot_id", "robot")

    if not robot_id:
        rospy.logerr("No robot_id provided! Use _robot_id:=robotX in the launch file.")
        sys.exit(1)

    try:
        handler = RobotController(robot_id)
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo(f"Robot {robot_id} Controller shutting down")
