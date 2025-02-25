#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import os

class PositionLoader:
    def __init__(self):
        rospy.init_node('position_loader', anonymous=True)
        self.task_pub = rospy.Publisher('/task_stream', String, queue_size=10)
        self.finished_sub = rospy.Subscriber('/finished_stream', String, self.task_finished_callback)
        self.tasks = []
        self.current_task_index = 0

        # self.task_loc = rospy.get_param("moj_task") > debagovati
        # print(os.getcwd())
        # self.task_loc = "/home/etfrobot/catkin_ws/src/mobile_manipulation/config/tasks.txt"
        self.task_loc = "/home/ruzamladji/catkin_ws/src/mobile_manipulation/src/tasks.txt"

        if self.task_loc:
            self.load_tasks(self.task_loc)  # Update with the correct path
        else:
            print("Warning: Parameter not loaded, loading dummy parameters")
            # self.load_tasks("tasks.txt")

        self.task_in_progress = False
        self.curr_task = None

    def load_tasks(self, file_path):
        with open(file_path, 'r') as file:
            self.tasks = file.readlines()

    def task_finished_callback(self, msg):
        rospy.loginfo(f"Received completion signal for task: {msg.data}")
        self.task_in_progress = False

    def stream_tasks(self):
        rate = rospy.Rate(10)  # 1 Hz
        while not rospy.is_shutdown():
            if not self.task_in_progress and self.current_task_index < len(self.tasks):
                task = self.tasks[self.current_task_index].strip()
                self.task_pub.publish(task)
                rospy.loginfo(f"Published task: {task}")
                self.task_in_progress = True
                self.current_task_index += 1
                self.curr_task = task
            self.task_pub.publish(self.curr_task)
            print(self.curr_task)
            rate.sleep()

if __name__ == '__main__':
    loader = PositionLoader()
    try:
        loader.stream_tasks()
    except rospy.ROSInterruptException:
        pass
