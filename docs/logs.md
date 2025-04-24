# Meetings Minutes

## Meeting 24.04.2025.

|                                                     Task                                                     |             Responsible             |     Due     |    Status     |
| :----------------------------------------------------------------------------------------------------------: | :---------------------------------: | :---------: | :-----------: |
|                                         Finish Q2 report                                                     |            Nikola Knezevic          | 24.05.2025. | ✅ DONE |
|                                         Finish Q2 report                                                     |            Nikola Knezevic, Sumbal Malik          | 8.05.2025. | ⚠️ TO BE DONE |
|                                         Simulation environments for greenhouses                              |            Nikola Ruzic, Syed Abbas Hussain          | 8.05.2025. | ⚠️ TO BE DONE |
|                                       Multi robot bug fix, Map bug fix                                       |    Nikola Knezevic, Nikola Ruzic    |             | ⚠️ TO BE DONE |
|                                            Digital twin AL Silal                                             |                                     |             | ⚠️ TO BE DONE |
|                                         K1 Perception                                                        |         Syed Abbas Hussain          | 24.04.2025. | ✅ DONE |
|                         Make an Isaac Sim based simulation for the RBKAIROS robot                             |         Nikola Ruzic               | 8.05.2025. | ⚠️ TO BE DONE |
|                   PDDL problem definition for the last mile logistics as interacting mobile manipulators      |         Sumbal Malik          | 24.04.2025. | ✅ DONE |
|                       Formulate a concrete plan and literature review for robot skill acquisition.           |         Nikola Ruzic               | 8.05.2025. | ⚠️ TO BE DONE |
|                                         K1 + GO1 Initial simulation integration                              |         Syed Abbas Hussain          | 8.05.2025. | ⚠️ TO BE DONE |
|                   Upgrading the capabilities for the Multi-agent PDDL planning      				|         Sumbal Malik          | 8.05.2025. | ⚠️ TO BE DONE |




- Discussions about previously done work that included:
	- Multi robot bug fix, Map bug fix , Multi-robot Gazebo simulation still has a namespace issue
	- Make an Isaac Sim based simulation for the RBKAIROS robot, URDF importer doesn't work with the whole robot, strategy is to split the base from the arm
 	- New Research directions - > whole body task-based planning, while taking into account the required parameters of a given robot skill (i.e whole-body stiffness shaping)
		- Can be useful for safe and streamlined skill execution like packing, carrying, picking …
		- Can take into account different soft grippers and manipulation aspects of the system application 
		- Success rate – proposed metric to be used as a benchmark to be connected to the high-level PDDL planners.
  	- Whole-body stiffness shaping - > generate x,y and theta values for the mobile-base to satisfy the stiffness constrains outside the robot stationary workspace.
 
  	- Completed the perception pipeline
  	- Initial testing with the KNN model for motion planning
  	- A switch to the more robust MoveIT motion planning pipeline based on perception

     	- Integrated a new type of agent (robot) into the PDDL formulation
  	- Integrated the maximum distance constraint for auxiliary vehicles
  	- Integrated the Cyclic and acyclic operations for auxiliary vehicles

   	- Upgrading the capabilities for the Multi-agent PDDL planning:
  		- Multiple truck and auxiliary vehicle testing
   	 	- Flexible docking for drones and robots
   	    	- Randomizing locations and distances
   	       	- Configuring different temporal planners (SGPlan, TFD)
  	  
  	   


	



## Meeting 10.04.2025.

|                                                     Task                                                     |             Responsible             |     Due     |    Status     |
| :----------------------------------------------------------------------------------------------------------: | :---------------------------------: | :---------: | :-----------: |
|                                         Finish Q1 report                                                     |            Nikola Knezevic          | 24.04.2025. | ✅ DONE |
|                                         Grasping strategies repo                                             |            Nikola Knezevic          | 24.04.2025. | ✅ DONE |
|                                         RAAD paper comments                                                  |  Nikola Knezevic, Nikola Ruzic, Sumbal Malik       | 25.03.2025. | ✅ DONE|
|                                         Simulation environments for greenhouses                              |            Nikola Ruzic, Sayed          | 24.04.2025. | ⚠️ TO BE DONE |
|                                       Multi robot bug fix, Map bug fix                                       |    Nikola Knezevic, Nikola Ruzic    | 24.04.2025. | ⚠️ TO BE DONE |
|                                            Digital twin AL Silal                                             |                                     |             | ⚠️ TO BE DONE |
|                                       Review the PDDL versions and related work.                            |            Sumbal Malik             | 24.04.2025. | ✅ DONE |
|                                         Provide a link to GO1 GitHub repo                                    |         Syed Abbas Hussain          | 24.04.2025. | ✅ DONE |
|                                         K1 Perception                                                        |         Syed Abbas Hussain          | 24.04.2025. | ⚠️ TO BE DONE |
|                         Make an Isaac Sim based simulation for the RBKAIROS robot                             |         Nikola Ruzic               | 24.04.2025. | ⚠️ TO BE DONE |
|                   PDDL problem definition for the last mile logistics as interacting mobile manipulators      |         Sumbal Malik          | 24.04.2025. | ⚠️ TO BE DONE |


- Discussions about previously done work that included:
	- PDDL problem definition for the last mile logistics as interacting mobile manipulators:
	The term "drone" should be replaced by "robot agent." In the current reports, there is no need for drones because they are just mobile robots or robot agents without kinematic and 		environmental constraints.

	- Possible type of constraints to be explored from the literature: 
	1. Payload - manipulation payload, mobile base payload
	2. Advanced:
		2.1 Environmental constraint (restrictions for specific type of robots or different max robot velocities) - this is important to demonstrate the need for different robot 			agents: legged robots and wheeled robots whose constraint is restricted for specific environments like stairs or rough terrain.
		2.2 Kinematic constraints in path planning due to the sliding constraint for wheeled robots/trucks and similar constraints for leged robots

	- Demonstration of the web-based control system for the GO1
	- Demonstration of the URDF file for the GO1 compatable ARM
	- Demonstration of a object detection algorithm for the perception capabilities of the GO1 manipulator
	- Multi-robot issue has been presented to the RBKAIROS manufacturer - > awating a response
	- Isaac Sim Ros control exploration
	- Isaac Sim RBKAIROS port and its possible uses has been discussed
	- Isaac Lab future application has been discussed


   


## Meeting 11.03.2025.

|                                                     Task                                                     |             Responsible             |     Due     |    Status     |
| :----------------------------------------------------------------------------------------------------------: | :---------------------------------: | :---------: | :-----------: |
|                                         Finish Q1 report                                                     |            Nikola Knezevic          | 25.03.2025. | ⚠️ TO BE DONE |
|                                         Grasping strategies repo                                             |            Nikola Knezevic          | 25.03.2025. | ⚠️ TO BE DONE |
|                                         RAAD paper comments                                                  |  Nikola Knezevic, Nikola Ruzic, Sumbal Malik       | 25.03.2025. | ⚠️ TO BE DONE |
|                                         Simulation environments for greenhouses                              |            Nikola Ruzic, Sayed          | 25.03.2025. | ⚠️ TO BE DONE |
|                                       Multi robot bug fix, Map bug fix                                       |    Nikola Knezevic, Nikola Ruzic    | 25.03.2025. | ⚠️ TO BE DONE |
|                                            Digital twin AL Silal                                             |                                     |             | ⚠️ TO BE DONE |
|                                       Review the PDDL versions and related work.                            |            Sumbal Malik             | 25.03.2025. | ⚠️ TO BE DONE |
|                                         Provide a link to GO1 GitHub repo                                    |         Syed Abbas Hussain          | 25.03.2025. | ⚠️ TO BE DONE |
|                                         K1 Perception                                                        |         Syed Abbas Hussain          | 25.03.2025. | ⚠️ TO BE DONE |

- Discussions about previously done work that included:

	- Still some work is needed to fix multi-robot usage in Gazebo—identified an issue with launch files and passing arguments through them.
	- Finalize the Q1 report—an initial version was presented at the meeting.
	- BU to provide the repositories used for grasping strategies.
	- RAAD paper—reviewer comments have been checked and agreed upon.
	- Formulated a Flexible Multi-Depot VRP using the Planning Domain Definition Language (PDDL).
	- Discussion on PDDL: evaluating its expressiveness in capturing all task constraints (payload, energy consumption, etc.), comparing its formulation with ILP, and analyzing different PDDL planners.
	- Demonstration of GO1 + K1 grasping a brick from a predefined position.
	- Perception and grasping for K1 are in progress.
	- Agreement needed on the simulation approach—will Al Silal provide the digital twin for the project, or should an open-source environment for greenhouses be found?
	- Discussion on two demo scenarios: one for last-mile delivery (physical) and one for the agrifood use case (simulation).



## Meeting 27.02.2025.

|                                                     Task                                                     |             Responsible             |     Due     |    Status     |
| :----------------------------------------------------------------------------------------------------------: | :---------------------------------: | :---------: | :-----------: |
| Refactor documentation, perform ROS2 integration testing, and automate ROS2/1 Bridge bring up with a script. |    Nikola Knezevic, Nikola Ruzic    | 13.03.2025. | ✅ DONE |
|                                       Multi robot bug fix, Map bug fix                                       |    Nikola Knezevic, Nikola Ruzic    | 13.03.2025. | ⚠️ TO BE DONE |
|                                            Digital twin AL Silal                                             |                                     |             | ⚠️ TO BE DONE |
|                                       PDDL example for multiple robots                                       |            Sumbal Malik             | 13.03.2025. | ⚠️ TO BE DONE |
|                            Explore how to integrate the PDDF with GO1 integration                            |         Syed Abbas Hussain          | 13.03.2025. | ✅ DONE |
|                                         Provide a link to GO1 GitHub repo                                    |         Syed Abbas Hussain          | 13.03.2025. | ⚠️ TO BE DONE |

- Discussions about previously done work that included:

  - The report template will be provided once received. KU RSO has been contacted, and we are awaiting the template. In the meantime, BU will begin drafting the report in free form until the official template is available.
  - Bags fix: Timing, gripping, single robot simulation/real behaviour, ROS1
  - There are still issues with multiple robots and the launch file—specifically, the robot_id is not propagating as expected through the launch files. Move_base works but MoveIt not.
  - Gazebo - MAP creating needs to be check: from time to time move_base stuck because of low quaility maps.
  - Research paper presented: [Heterogeneous Multi-robot Task Allocation and Scheduling via Reinforcement Learning](https://marmotlab.org/publications/73-RAL2025-HetMRTA.pdf)
  - Formulated a Flexible Multi-Depot VRP as Planning Domain Definition Language (PDDL).
  - Initial experiments with PDDL were conducted using BFWS and ENHSP planners.
  - Test and integration of R1 Arm and GO1 is done.
  - Presented Web integration and manipulator (jogging, reset to home, execute prerecodred movements, open/close gripper)
  - Presented arhitecture of GO1+ARM+LIDAR 


## Meeting 13.02.2025.

|                                                     Task                                                     |             Responsible             |     Due     |    Status     |
| :----------------------------------------------------------------------------------------------------------: | :---------------------------------: | :---------: | :-----------: |
|                                               Report template                                                |            Sumbal Malik             |      /      |   ✅ DONE  |
|            Fix the timing issue in the simulation and merge control for real and simulated system            |            Nikola Ruzic             | 27.02.2025. |   ✅ DONE  |
| Refactor documentation, perform ROS2 integration testing, and automate ROS2/1 Bridge bring up with a script. |    Nikola Knezevic, Nikola Ruzic    | 27.02.2025. | ⚠️ TO BE DONE |
|                                Explore the possibility of an IROS submission.                                |     Nikola Ruzic, Sumbal Malik      | 27.02.2025. | ⚠️ TO BE DONE |
|                                            Digital twin AL Silal                                             |                                     |             | ⚠️ TO BE DONE |
|                                              Unitry GO1 GitHub                                               |         Syed Abbas Hussain          | 27.02.2025. |   ✅ DONE  |
|                                   Joint GitHub organisation and structure                                    | Syed Abbas Hussain, Nikola Knezevic | 27.02.2025. |    ✅ DONE    |
|                            Explore how to integrate the PDDF with GO1 integration                            |         Syed Abbas Hussain          | 27.02.2025. | ⚠️ TO BE DONE |

- Discussions about previously done work that included:

  - The RAAD paper
  - Developed robot demo for the RBKAIROS robot

- TODO:

  - Fix the timing issue in the simulation and merge control for real and simulated systems.
  - Refactor documentation, perform ROS2 integration testing, and automate ROS2/1 Bridge bring up with a script.
  - Explore the possibility of an IROS submission [IROS Paper Submission Deadline: March 01, 2025].

- Possible IROS submission, where the work from the RAAD paper would be expanded upon. Additions would consist of including a parser for Planning Domain Definition Language (PDDL) to encapsulate different capabilities for the planning algorithm pipeline.

- Discussions about the Control dashboard for the Unitree GO1 legged robot. Implementation details. GitHub refactoring. Digital twin discussion.

## Meeting 03.02.2025.

|             Task              |        Responsible         |     Due     |    Status     |
| :---------------------------: | :------------------------: | :---------: | :-----------: |
| MKDOCS for GitHub repo HARBOT |      Nikola Knezevic       | 03.02.2025. |    ✅ DONE    |
| Log file for process tracing  |      Nikola Knezevic       | 03.02.2025. |    ✅ DONE    |
|        Report template        |        Sumbal Malik        |      /      | ⚠️ IN PROCESS |
| RAAD 2025 paper - First draft | Nikola Ruzic, Sumbal Malik | 07.02.2025. |    ✅ DONE    |

- Experimental scenarios:
  - One robot one depot
  - One robot multiple depots ( 3 depots )
  - Multiple robots - same depot
  - Multiple robots multiple depots
- Simulation parameters:
  - Up to 20 locations
  - Bin payload 1-10 Kg
  - Mobile platfrom payload 10 - 50 Kg
  - Manipulator payload 3 or 10 Kg
  - Robot speed 0.5-1.5 m/s
  - Simulation area 500x500m
  - Number of robots 1 or 3
