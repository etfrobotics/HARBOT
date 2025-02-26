#!/usr/bin/env bash

roslaunch rbkairos_sim_bringup rbkairos_complete.launch &

sleep 20

roslaunch multi_robot_load_tasks multi_robot.launch &

sleep 5

roslaunch multi_robot_load_tasks route_planner.launch

# Look at a way for this to be done with different windows