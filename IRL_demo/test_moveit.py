


import rospy
from robot_simple_command_manager_msgs.msg import CommandString
from robot_simple_command_manager_msgs.msg import CommandManagerStatus  
from time import sleep

import moveit_commander
import sys
from moveit_commander import RobotCommander, PlanningSceneInterface, MoveGroupCommander

# from std_msgs import PoseStamped

import actionlib

import franka_gripper.msg

rospy.init_node('cycle_positions_with_status_check', anonymous=False)


        # Initialize MoveIt Commander
robot = RobotCommander()
scene = PlanningSceneInterface()
group_name = "arm"  # Replace with your MoveIt group name
move_group = MoveGroupCommander(group_name)


def move_gripper(wid):

    client = actionlib.SimpleActionClient('/robot/arm/franka_gripper/move', franka_gripper.msg.MoveAction)

    client.wait_for_server()

    goal = franka_gripper.msg.MoveGoal(width=wid, speed=0.1)

    client.send_goal(goal)

    client.wait_for_result()

    return client.get_result()

# joint_goal_home = [-1.0 * 3.1415/180, -51.0 * 3.1415/180, 0.0 * 3.1415/180, -156.0 * 3.1415/180, -2.0 * 3.1415/180, 107.0 * 3.1415/180, 48.0 * 3.1415/180]

# move_group.go(joint_goal_home, wait=True)
# sleep(5)
# move_group.stop()

# joint_goal_1 = [-3.0 * 3.1415/180, 0.0 * 3.1415/180, 3.0 * 3.1415/180, -98.0 * 3.1415/180, -2.0 * 3.1415/180, 98.0 * 3.1415/180, 43.0 * 3.1415/180]
# move_group.go(joint_goal_1, wait=True)
# sleep(5)
# move_group.stop()

#                     #Gripper
# move_gripper(0)
# sleep(2)
                    
# joint_goal_2 = [-4.0 * 3.1415/180, -31.0 * 3.1415/180, 5.0 * 3.1415/180, -104.0 * 3.1415/180, -2.0 * 3.1415/180, 74.0 * 3.1415/180, 47.0 * 3.1415/180]

# move_group.go(joint_goal_2, wait=True)
# sleep(5)
# move_group.stop()  


# joint_goal_3 = [0.0 * 3.1415/180, 34.0 * 3.1415/180, 0.0 * 3.1415/180, -72.0 * 3.1415/180, -5.0 * 3.1415/180, 108.0 * 3.1415/180, 48.0 * 3.1415/180]
# move_group.go(joint_goal_3, wait=True)
# sleep(5)
# move_group.stop()

move_gripper(0.1)
# sleep(2)

# joint_goal_home = [-1.0 * 3.1415/180, -51.0 * 3.1415/180, 0.0 * 3.1415/180, -156.0 * 3.1415/180, -2.0 * 3.1415/180, 107.0 * 3.1415/180, 48.0 * 3.1415/180]

# move_group.go(joint_goal_home, wait=True)
# sleep(5)
# move_group.stop()

# sleep(15)