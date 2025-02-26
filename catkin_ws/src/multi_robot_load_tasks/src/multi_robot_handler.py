#!/usr/bin/env python3

import rospy
import json
from std_msgs.msg import String

class MultiRobotHandler:
    def __init__(self):
        rospy.init_node('multi_robot_handler', anonymous=True)

        # Robot IDs
        # self.robot_ids = ['robot_b', 'robot_c']s

        #TODO: add as a param
        self.robot_ids = ['robot', 'robot_b', 'robot_c']

        # Publishers for each robot's plan topic
        self.publishers = {robot_id: rospy.Publisher(f'/{robot_id}/plan', String, queue_size=10) for robot_id in self.robot_ids}

        # Subscribe to the planner's topic
        rospy.Subscriber('/multi_robot_planner', String, self.plan_callback)

        rospy.loginfo("MultiRobotHandler initialized and ready")

    def plan_callback(self, msg):
        """Receives the global plan and distributes it to each robot."""
        try:
            planned_actions = json.loads(msg.data)
            rospy.loginfo(f"Received planned actions: {planned_actions}")

            for robot_id, plan in planned_actions.items():
                if robot_id in self.publishers:
                    self.publishers[robot_id].publish(plan)

                    rospy.loginfo(f"Published plan for {robot_id}: {plan}")
                else:
                    rospy.logwarn(f"Unknown robot ID: {robot_id}")

        except json.JSONDecodeError as e:
            rospy.logerr(f"Error decoding JSON: {e}")

if __name__ == '__main__':
    try:
        MultiRobotHandler()
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo("MultiRobotHandler shutting down")
