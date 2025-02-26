#!/usr/bin/env python3
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


class PositionCycler(object):
    def __init__(self):
        # Initialize this node
        rospy.init_node('cycle_positions_with_status_check', anonymous=False)

        # Positions you want to cycle (x, y, theta)
        self.positions = [
            "GOTO -0.5 2 0",  # Example position 1
            "GOTO -0.5 -0.82 1.57",  # Example position 2
            "GOTO 0.0 0.0 0.0",    # Example position 3
        ]
        
        # Index to track which position command is being published
        self.current_index = -1
        
        # Last known status code from /robot/command_manager/status
        self.current_status_code = None
        
        # Publisher: to send commands
        self.cmd_pub = rospy.Publisher(
            '/robot/command_manager/command', 
            CommandString, 
            queue_size=1
        )
        
        # Subscriber: to check movement status
        self.status_sub = rospy.Subscriber(
            '/robot/command_manager/status', 
            CommandManagerStatus,  # or CommandStatus if different
            self.status_callback
        )

       
        # Initialize MoveIt Commander
        self.robot = RobotCommander()
        self.scene = PlanningSceneInterface()
        self.group_name = "arm"  # Replace with your MoveIt group name
        self.move_group = MoveGroupCommander(self.group_name)
    

        self.joint_goal_home = [-1.0 * 3.1415/180, -51.0 * 3.1415/180, 0.0 * 3.1415/180, -156.0 * 3.1415/180, -2.0 * 3.1415/180, 107.0 * 3.1415/180, 48.0 * 3.1415/180]

        self.move_group.go(self.joint_goal_home, wait=True)
        self.move_group.stop()
        sleep(1)


    def move_gripper(self, wid):

        client = actionlib.SimpleActionClient('/robot/arm/franka_gripper/move', franka_gripper.msg.MoveAction)

        client.wait_for_server()

        goal = franka_gripper.msg.MoveGoal(width=wid, speed=0.1)

        client.send_goal(goal)

        client.wait_for_result()

        return client.get_result()


    def status_callback(self, msg):
        """
        This callback is triggered whenever a new status message is published
        on /robot/command_manager/status.
        
        We assume the status message has:
         - msg.command (e.g. 'GOTO 0.0 0.0 0.0')
         - msg.code    (e.g. 'ACTIVE', 'SUCCEEDED', or 'FAILED')
         - msg.msg     (optional text info like "Goal reached.")
         
        Adjust this based on your actual status message fields.
        """
        self.current_status_code = msg.code

        # If we're in the middle of executing a command and the new status is SUCCEEDED, 
        # we can proceed to the next command.
        # if self.command_in_progress and msg.code == "SUCCEEDED":
        #     rospy.loginfo("[Status] Movement finished: %s", msg.command)
        #     self.command_in_progress = False




    def run(self):
        """
        Main run loop:
         1. If no command is in progress, publish the next 'GOTO' command.
         2. Wait for the robot to report 'ACTIVE', then eventually 'SUCCEEDED'.
         3. Once 'SUCCEEDED', send the next command, etc.
        """
        while not rospy.is_shutdown():
            # If no command in progress, send the next position
            
            # sleep()

            if not self.current_status_code == 'ACTIVE':


                if self.current_index == 1: 
                    
                    joint_goal_1 = [-3.0 * 3.1415/180, 0.0 * 3.1415/180, 3.0 * 3.1415/180, -98.0 * 3.1415/180, -2.0 * 3.1415/180, 98.0 * 3.1415/180, 43.0 * 3.1415/180]
                    self.move_group.go(joint_goal_1, wait=True)
                    # sleep(1)
                    self.move_group.stop()

                    #Gripper
                    self.move_gripper(0)
                    # sleep(2)
                    
                    joint_goal_2 = [-4.0 * 3.1415/180, -31.0 * 3.1415/180, 5.0 * 3.1415/180, -104.0 * 3.1415/180, -2.0 * 3.1415/180, 74.0 * 3.1415/180, 47.0 * 3.1415/180]

                    self.move_group.go(joint_goal_2, wait=True)
                    # sleep(1)
                    self.move_group.stop()  

                    # sleep(2)

                elif self.current_index == 2:
 
                    joint_goal_3 = [0.0 * 3.1415/180, 34.0 * 3.1415/180, 0.0 * 3.1415/180, -72.0 * 3.1415/180, -5.0 * 3.1415/180, 108.0 * 3.1415/180, 48.0 * 3.1415/180]
                    self.move_group.go(joint_goal_3, wait=True)
                    # sleep(1)
                    self.move_group.stop()

                    self.move_gripper(0.1)
                    # sleep(2)

                    self.move_group.go(self.joint_goal_home, wait=True)
                    self.move_group.stop()

                    # sleep(2)
                elif self.current_index == 0:
                    sleep(1)
                    
            

                # Publish the next command
                next_cmd = self.positions[self.current_index]
                command_msg = CommandString()
                command_msg.command = next_cmd
                self.cmd_pub.publish(command_msg)
                
                # rospy.loginfo("[PositionCycler] Sending command: %s", next_cmd)
                
                # self.command_in_progress = True
                # Move to the next position in a cycle
                self.current_index = (self.current_index + 1) % len(self.positions)
            sleep(2)
            print(self.current_index)    
            
            # Sleep a little to avoid spamming
            # s1elf.rate.sleep()

def main():
    try:
        cycler = PositionCycler()
        cycler.run()
    except rospy.ROSInterruptException:
        pass

if __name__ == '__main__':
    main()
