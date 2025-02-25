#!/usr/bin/env python3

import rospy
import moveit_commander
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
from mobile_manipulation.srv import PickPlaceTask, PickPlaceTaskResponse  # Replace 'your_package' with your package name
import sys


class ManipulationHandler:
    def __init__(self):
        rospy.init_node('manipulation_handler', anonymous=True)

        # Initialize MoveIt Commander
        moveit_commander.roscpp_initialize(sys.argv)
        self.robot = moveit_commander.RobotCommander(robot_description='/robot/robot_description', ns="robot")
        self.group = moveit_commander.MoveGroupCommander("ur5_arm", robot_description='/robot/robot_description', ns="robot")

        self.finished_pub = rospy.Publisher('/finished_stream', String, queue_size=10)

        # Create a service for pick-and-place tasks
        self.service = rospy.Service('pickplace_service', PickPlaceTask, self.handle_pickplace_task)

        rospy.loginfo("ManipulationHandler initialized and ready for tasks")

    def handle_pickplace_task(self, req):
        """Handles the pick-and-place task via service request."""
        try:
            # Extract start and end poses from the request
            start_pose = [req.start_x, req.start_y, req.start_z, req.start_qx, req.start_qy, req.start_qz, req.start_qw]
            end_pose = [req.end_x, req.end_y, req.end_z, req.end_qx, req.end_qy, req.end_qz, req.end_qw]

            # Move to the start position
            self.move_arm_to(start_pose)

            # Move to the end position
            self.move_arm_to(end_pose)

            # Publish task completion
            self.finished_pub.publish(f"PICKPLACE_COMPLETED {req.start_x} {req.start_y} {req.end_x} {req.end_y}")
            rospy.loginfo("Pick-and-place task completed")

            return PickPlaceTaskResponse(success=True, message="Task completed successfully")
        except Exception as e:
            rospy.logerr(f"Error during pick-and-place task: {e}")
            return PickPlaceTaskResponse(success=False, message=str(e))

    def move_arm_to(self, pose_data):
        """Moves the robotic arm to the specified pose."""
        pose = PoseStamped()
        pose.header.frame_id = "robot_base_footprint"
        pose.header.stamp = rospy.Time.now()
        pose.pose.position.x, pose.pose.position.y, pose.pose.position.z = pose_data[:3]
        pose.pose.orientation.x, pose.pose.orientation.y, pose.pose.orientation.z, pose.pose.orientation.w = pose_data[3:]
        self.group.set_pose_target(pose)
        self.group.go(wait=True)
        rospy.loginfo(f"Moved to pose: {pose.pose}")

    def run(self):
        rospy.loginfo("ManipulationHandler service is running")
        rospy.spin()


if __name__ == '__main__':
    handler = ManipulationHandler()
    try:
        handler.run()
    except rospy.ROSInterruptException:
        pass
