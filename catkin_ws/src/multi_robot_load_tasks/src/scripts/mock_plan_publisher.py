import rospy
from std_msgs.msg import String
import json

rospy.init_node("mock_plan_publisher")
pub = rospy.Publisher("/robot/", String, queue_size=10)

mock_plan = {
    "robot1": "MOVE 1.0 2.0 0.0 0.0 0.0 0.0 1.0\nPICKPLACE 0.5 0.5 0.0 0.0 0.0 0.0 1.0 1.5 1.5 0.0 0.0 0.0 0.0 1.0",
    "robot2": "MOVE 2.0 3.0 0.0 0.0 0.0 0.0 1.0\nMOVE 3.5 4.0 0.0 0.0 0.0 0.0 1.0",
    "robot3": "PICKPLACE 1.0 1.0 0.0 0.0 0.0 0.0 1.0 2.0 2.0 0.0 0.0 0.0 0.0 1.0"
}

rospy.sleep(1)  # Ensure publisher is registered
pub.publish(json.dumps(mock_plan))
rospy.loginfo("Published mock plan")
