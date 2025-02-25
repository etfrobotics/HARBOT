#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped

class MobileBaseHandler:
    def __init__(self):
        rospy.init_node('mobile_base_handler', anonymous=False)
        rospy.loginfo("MobileBaseHandler init")
        self.task_sub = rospy.Subscriber('/task_stream', String, self.task_callback)
        self.finished_pub = rospy.Publisher('/finished_stream', String, queue_size=10)
        self.goal_pub = rospy.Publisher('/robot/move_base_simple/goal', PoseStamped, queue_size=10)
        self.world_offset = [0, 0, 0]
        self.curr_task = None
        self.task_processed = False

    def task_callback(self, msg):
        task = msg.data.strip().split()
        if task[0] == "MOVE":
            self.curr_task = task
            self.task_processed = True

    def handle_move_task(self, task):
        x, y, z, qx, qy, qz, qw = map(float, task[1:])

        goal = PoseStamped()
        goal.header.stamp = rospy.Time.now()
        goal.header.frame_id = "robot_map"

        goal.pose.position.x = x 
        goal.pose.position.y = y 
        goal.pose.position.z = z 

        goal.pose.orientation.x = qx
        goal.pose.orientation.y = qy
        goal.pose.orientation.z = qz
        goal.pose.orientation.w = qw

        rospy.loginfo(f"Moving robot to: {goal.pose}")
        self.goal_pub.publish(goal)
        rospy.sleep(10)  # Simulate movement duration > Ovo videti kako da se doradi (mozda nova funckija koja gleda da li je robot u blizini targeta)
        self.finished_pub.publish(f"MOVE_COMPLETED {task[1]} {task[2]}")
        rospy.loginfo("Move task completed")

    def run(self):
        rate = rospy.Rate(10)  # 1 Hz
        while not rospy.is_shutdown():

            if (self.task_processed):
                self.handle_move_task(self.curr_task)
                self.task_processed = False
            else:
                rate.sleep()


if __name__ == '__main__':
    loader = MobileBaseHandler()
    try:
        loader.run()
    except rospy.ROSInterruptException:
        pass

    
