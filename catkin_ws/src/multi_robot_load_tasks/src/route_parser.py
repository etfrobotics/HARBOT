#!/usr/bin/env python3
"""
A ROS node that loads a JSON file describing robot routes,
iterates over its data, and creates a mock plan for each robot.

For each customer waypoint in a robot’s route, the node creates a MOVE command
(using the waypoint's coordinates and a fixed orientation) followed by a constant
PICKPLACE command.

Additionally, if the last waypoint in the route is a depot, a final MOVE command is added
so that the robot returns to the depot.
"""

import rospy
import json
import os

from std_msgs.msg import String


def load_plan_json(json_file_path):
    """
    Loads and parses the JSON file.
    """
    if not os.path.isfile(json_file_path):
        rospy.logerr("File not found: %s", json_file_path)
        return None

    with open(json_file_path, 'r') as f:
        try:
            data = json.load(f)
            rospy.loginfo("Successfully loaded JSON file.")
            return data
        except Exception as e:
            rospy.logerr("Failed to load JSON: %s", str(e))
            return None

def create_mock_plan_from_json(plan_data):
    """
    Iterates through the JSON data structure and builds a plan for each robot.
    
    """

    mock_plan = {}

    move_orientation = "0.0 0.0 0.0 0.0 1.0"

    fixed_pickplace = "-0.4 0.0 0.7 -0.00192 0.98355 -0.18062 0.00037445 -0.5 0.0 1.0 -0.0019288 0.98355 -0.18062 0.00037"


    for robot in plan_data.get("robots", []):
        robot_id = robot.get("robot_id", "unknown")
        commands = []
        route = robot.get("route", [])

        x_offset = 0
        y_offset = 0

        scale = 5/0.3
        # Process the intermediate waypoints.
        # Assuming the first waypoint is the starting depot and the last is the returning depot,
        # we iterate over the waypoints in between.
        for waypoint in route[1:-1]:
            if waypoint.get("type", "").lower() == "customer":
                x = waypoint["coordinates"]["x"]*scale + x_offset
                y = waypoint["coordinates"]["y"]*scale + y_offset
                # Create the MOVE command using the waypoint's coordinates.
                move_cmd = "MOVE {:.2f} {:.2f} {}".format(x, y, move_orientation)
                # Create the corresponding PICKPLACE command.
                pickplace_cmd = "PICKPLACE {}".format(fixed_pickplace)
                commands.append(move_cmd)
                commands.append(pickplace_cmd)


        if route:
            last_wp = route[-1]
            if last_wp.get("type", "").lower() == "depot":
                depot_x = last_wp["coordinates"]["x"]*scale + x_offset
                depot_y = last_wp["coordinates"]["y"]*scale + y_offset
                depot_move_cmd = "MOVE {:.2f} {:.2f} {}".format(depot_x, depot_y, move_orientation)
                commands.append(depot_move_cmd)

     
        mock_plan["robot{}".format(robot_id)] = "\n".join(commands)

    return mock_plan

def main():
    rospy.init_node('plan_parser_node', anonymous=True)

    pub = rospy.Publisher("/multi_robot_planner", String, queue_size=10)


    # Get the JSON file path from the ROS parameter server (default: "plan.json")
    json_file = rospy.get_param("~json_file", "/home/ruzamladji/catkin_ws/src/multi_robot_load_tasks/src/optimization_plans/Scenario_01.json")
    rospy.loginfo("Using plan file: %s", json_file)

    # Load and parse the JSON file.
    plan_data = load_plan_json(json_file)
    if plan_data is None:
        rospy.logerr("Exiting because the JSON file could not be loaded.")
        return

    # Build the mock plan by iterating through the JSON data.
    mock_plan = create_mock_plan_from_json(plan_data)



    rospy.sleep(1.0)
    

    pub.publish(json.dumps(mock_plan))

  
    for robot, commands in mock_plan.items():
        rospy.loginfo("Plan for %s:\n%s", robot, commands)

   
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
