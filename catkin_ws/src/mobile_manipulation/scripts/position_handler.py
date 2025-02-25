#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from mobile_manipulation.srv import MoveTask, MoveTaskRequest, PickPlaceTask, PickPlaceTaskRequest  


class PositionLoader:
    def __init__(self):
        rospy.init_node('position_loader', anonymous=True)

        # Service clients
        rospy.wait_for_service('move_task_service')
        rospy.wait_for_service('pickplace_service')
        self.move_service_client = rospy.ServiceProxy('move_task_service', MoveTask)
        self.pickplace_service_client = rospy.ServiceProxy('pickplace_service', PickPlaceTask)

        rospy.loginfo("PositionLoader initialized and ready to execute commands")

    def execute_command(self, command):
        """Execute a single command by calling the appropriate service."""
        args = command.strip().split()
        task_type = args[0]

        if task_type == "MOVE":
            self.execute_move_command(args[1:])
        elif task_type == "PICKPLACE":
            self.execute_pickplace_command(args[1:])
        else:
            rospy.logwarn(f"Unknown task type: {task_type}")

    def execute_move_command(self, args):
        """Execute a MOVE command by calling the move_task_service."""
        try:
            move_request = MoveTaskRequest()
            move_request.x = float(args[0])
            move_request.y = float(args[1])
            move_request.z = float(args[2])
            move_request.qx = float(args[3])
            move_request.qy = float(args[4])
            move_request.qz = float(args[5])
            move_request.qw = float(args[6])

            rospy.loginfo(f"Calling MOVE service with: {move_request}")
            response = self.move_service_client(move_request)

            if response.success:
                rospy.loginfo("MOVE command executed successfully")
            else:
                rospy.logerr(f"MOVE command failed: {response.message}")

        except Exception as e:
            rospy.logerr(f"Error executing MOVE command: {e}")

    def execute_pickplace_command(self, args):
        """Execute a PICKPLACE command by calling the pickplace_service."""
        try:
            pickplace_request = PickPlaceTaskRequest()
            # Start pose
            pickplace_request.start_x = float(args[0])
            pickplace_request.start_y = float(args[1])
            pickplace_request.start_z = float(args[2])
            pickplace_request.start_qx = float(args[3])
            pickplace_request.start_qy = float(args[4])
            pickplace_request.start_qz = float(args[5])
            pickplace_request.start_qw = float(args[6])

            # End pose
            pickplace_request.end_x = float(args[7])
            pickplace_request.end_y = float(args[8])
            pickplace_request.end_z = float(args[9])
            pickplace_request.end_qx = float(args[10])
            pickplace_request.end_qy = float(args[11])
            pickplace_request.end_qz = float(args[12])
            pickplace_request.end_qw = float(args[13])

            rospy.loginfo(f"Calling PICKPLACE service with: {pickplace_request}")
            response = self.pickplace_service_client(pickplace_request)

            if response.success:
                rospy.loginfo("PICKPLACE command executed successfully")
            else:
                rospy.logerr(f"PICKPLACE command failed: {response.message}")

        except Exception as e:
            rospy.logerr(f"Error executing PICKPLACE command: {e}")

    def load_and_execute_tasks(self, task_list):
        """Load and execute a list of tasks sequentially."""
        rospy.loginfo("Starting task execution")
        for command in task_list:
            rospy.loginfo(f"Executing command: {command}")
            self.execute_command(command)
        rospy.loginfo("All tasks executed")


if __name__ == '__main__':
    try:
        # Sample task list; replace with actual input mechanism if needed
        task_list = [
            "MOVE 0.0 0.0 0.0 0.0 0.0 0.0 1.0",
            "PICKPLACE -0.4 0.0 0.7 0.0 0.71 0.0 0.71 -0.5 0.0 0.7 0.0 0.71 0.0 0.71"
        ]

        loader = PositionLoader()
        loader.load_and_execute_tasks(task_list)

    except rospy.ROSInterruptException:
        rospy.loginfo("PositionLoader interrupted")
