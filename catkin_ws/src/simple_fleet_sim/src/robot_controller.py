#!/usr/bin/env python3
import rospy
import math
import json
import tf
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

class RobotController:
    """
    A simple proportional controller that commands a differential-drive robot
    to move towards a specified (x, y) with a target yaw.
    """

    def __init__(self,
                 robot_id,
                 max_linear_speed=0.5,
                 max_angular_speed=1.0,
                 K_linear=0.5,
                 K_angular=1.0,
                 pos_tolerance=0.05,
                 yaw_tolerance=0.05):
        """
        :param robot_id: Unique identifier for the robot (e.g. "robot1").
        :param max_linear_speed: Max linear speed (m/s).
        :param max_angular_speed: Max angular speed (rad/s).
        :param K_linear: Proportional gain for distance control.
        :param K_angular: Proportional gain for angular control.
        :param pos_tolerance: Acceptable distance error to target.
        :param yaw_tolerance: Acceptable angular error to target orientation.
        """
        self.robot_id = robot_id
        self.max_linear_speed = max_linear_speed
        self.max_angular_speed = max_angular_speed
        self.K_linear = K_linear
        self.K_angular = K_angular
        self.pos_tolerance = pos_tolerance
        self.yaw_tolerance = yaw_tolerance

        # Current pose
        self.current_x = 0.0
        self.current_y = 0.0
        self.current_yaw = 0.0

        # Desired pose
        self.target_x = 0.0
        self.target_y = 0.0
        self.target_yaw = 0.0

        # Setup ROS infrastructure
        self.odom_sub = rospy.Subscriber(
            f"/{self.robot_id}/amcl_pose",
            Odometry,
            self.odom_callback
        )
        self.cmd_pub = rospy.Publisher(
            f"/{self.robot_id}/cmd_vel",
            Twist,
            queue_size=10
        )

        # Control timer
        self.control_timer = rospy.Timer(
            rospy.Duration(0.1),  # 10 Hz
            self.control_loop
        )

    def set_goal(self, x, y, yaw):
        """
        Set the robot’s target position and orientation.
        """
        self.target_x = x
        self.target_y = y
        self.target_yaw = yaw

    def odom_callback(self, msg):
        """
        Odometry callback: updates the robot’s current position and orientation.
        """
        self.current_x = msg.pose.pose.position.x
        self.current_y = msg.pose.pose.position.y

        # Extract yaw from quaternion
        orientation_q = msg.pose.pose.orientation
        quaternion = (
            orientation_q.x,
            orientation_q.y,
            orientation_q.z,
            orientation_q.w
        )
        _, _, yaw = tf.transformations.euler_from_quaternion(quaternion)
        self.current_yaw = yaw

    def control_loop(self, event):
        """
        Periodically compute the error to the target and publish a Twist command.
        """
        # Compute position error
        dx = self.target_x - self.current_x
        dy = self.target_y - self.current_y
        distance_error = math.sqrt(dx*dx + dy*dy)

        # Compute desired yaw (if you want to face the target point first)
        desired_yaw = math.atan2(dy, dx)
        yaw_error = desired_yaw - self.current_yaw
        # Normalize yaw error to [-pi, pi]
        yaw_error = math.atan2(math.sin(yaw_error), math.cos(yaw_error))

        # If you also want a final orientation, incorporate that eventually:
        final_yaw_error = self.target_yaw - self.current_yaw
        final_yaw_error = math.atan2(math.sin(final_yaw_error), math.cos(final_yaw_error))

        # Decide how to handle the orientation vs. position. 
        # Option A: first orient towards the target, then move forward.
        # Option B: move while turning. 
        # This example moves while turning for simplicity.

        # Compute linear and angular velocity using P-controllers
        linear_speed = self.K_linear * distance_error
        # We want to incorporate final orientation if we are close enough in position
        # For instance, if close to the target position, we orient to target_yaw
        if distance_error < 0.2:
            # If close enough, reduce speed and focus on orientation
            linear_speed = 0.0
            yaw_error = final_yaw_error

        # Angular speed for orientation
        angular_speed = self.K_angular * yaw_error

        # Saturate speeds
        linear_speed = max(min(linear_speed, self.max_linear_speed), -self.max_linear_speed)
        angular_speed = max(min(angular_speed, self.max_angular_speed), -self.max_angular_speed)

        # Publish twist
        twist_msg = Twist()
        twist_msg.linear.x = linear_speed
        twist_msg.angular.z = angular_speed
        self.cmd_pub.publish(twist_msg)

    def goal_reached(self):
        """
        Check if the robot is within tolerance of the target pose.
        """
        # Position check
        dist = math.sqrt((self.target_x - self.current_x)**2 +
                         (self.target_y - self.current_y)**2)
        if dist > self.pos_tolerance:
            return False

        # Orientation check
        yaw_diff = self.target_yaw - self.current_yaw
        yaw_diff = math.atan2(math.sin(yaw_diff), math.cos(yaw_diff))
        if abs(yaw_diff) > self.yaw_tolerance:
            return False

        return True


def main():
    # rospy.init_node("robot_controller")
    # Example usage: a single RobotController
    # If you want multiple from command line, you can parse arguments or read from param server.
    robot_id = rospy.get_param("~robot_id", "robot")
    # controller = RobotController(robot_id=robot_id)

    # Example only: set a static goal from parameters or code
    target_x = rospy.get_param("~target_x", 1.0)
    target_y = rospy.get_param("~target_y", 0.0)
    target_yaw = rospy.get_param("~target_yaw", 0.0)


    rospy.init_node("robot_controller")
    controller = RobotController(robot_id=robot_id)
    controller.set_goal(target_x, target_y, target_yaw)

    rospy.loginfo(f"[{robot_id}] Going to: ({target_x}, {target_y}, yaw={target_yaw})")

    rospy.spin()


if __name__ == '__main__':
    main()
