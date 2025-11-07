# Meetings Minutes

## Meeting 22.11.2025.

|                                                                             Task                                                                             |   Responsible   | Due |     Status    |
| :----------------------------------------------------------------------------------------------------------------------------------------------------------: | :-------------: | :-: | :-----------: |
|                                         Simulation environments for greenhouses                                  |            Nikola Ruzic, Syed Abbas Hussain          | 8.05.2025. | ⚠️ TO BE DONE |
|                                            Digital twin AL Silal                                                                 |                                     |             | ⚠️ TO BE DONE |
|                        Develop a PyBullet sim of the mob. manipulator                                                       |         Nikola Knezevic, Nikola Ruzic           |		 | ⚠️ TO BE DONE |
|                        Investigate ROSplan and PyRDDL integration layer with Pybullet                                        |         Nikola Knezevic, Nikola Ruzic           |		 | ⚠️ TO BE DONE |
|Continue the soft-gripper experiment by testing grasping performance on additional fruit shapes. Validate the gripper’s capability and consistency across varied object geometries.                                       |        Veljko           |		 | ⚠️ TO BE DONE |
|                        Tweak the reward function, communicate with ETF team for integration                                       |         Sumbal          |		 | ⚠️ TO BE DONE |





### Discussion Outcomes

- Nikola R: Talked about the results of the Integration Meeting 30.10.2025, the closed loop action integration and presented 
a conference ready paper titled: Application of Volumetric Grasping Networks for Fruit Manipulation with a Collaborative Robot
- Nikola K: Talked about the PybulletSim as the next diraction for robot simulation.
- Sumbal: Talked about the Jax planner Nikola R presented.
- Seyyed: Inquired about the sim detals
- Sumbal: Presented the new reward function, along with the the regrasping (replanning) actions.
- Veljko: Presented the results of grasp displasement based grasping probability for soft grippers.
- Sumbal: Inquired about the dropoff probability, Nikola Knez. talked about computing uncertainty for pick and toss or similar offloading tactics


### Additional Notes

ROSPlan
https://kcl-planning.github.io/ROSPlan/documentation/
Robotnik github
- https://github.com/RobotnikAutomation/robotnik_simulation
- https://github.com/RobotnikAutomation/rbkairos_sim




## Integration Meeting 30.10.2025.

- (Sumbal, Veljko,  R. Nikola) RDDL integration meeting

We have discussed about the minimum possible example of the RDDL multi-bin last mile logistics harvesting problem.

Topics of the Discussion

1. RDDL – Exploring how RDDL functions through a concrete example:
   	Current RDDL implementation includes a series of fruit locations, with one robot. The robot visits each of the locations and has a 95% chance
   	of successful picking operation. It retries the operation until it succeeds, and then it deposites the fruit to the other depo or agents.
   
   	Indentified an critical implementational issue, how can the agent synchronize with the real-world sensor data and know when it didn't succeed in the grasping operations?
   	As of now it is open ended, where the engine outputs actions each timestep as a json file, but if the robot doesn't signal a failed grasp to the planner,
   	the world model of the planner diverges from the real-world. The agent could think that the state of the world is different than it is, and this needs to
   	be changed each timestep (rerun of the plan)

3. Feedback Loop Analysis: Attempting to determine what a feedback loop of any kind would look like within the RDDL framework.

4. Implementation Perspective: Discussing how such a system could be implemented in practice — including suitable data types, such as matrices, lists, or other structures.

https://arxiv.org/html/2211.05939v5 - pyRDDLGym, practical way to integrate a feedback loop.
Beacuse this is a gym environment the following plans can be tested and used in a publications that
are ready to use with out-of-the-box planners:
1. JaxPlan: Planning through autodifferentiation

2. GurobiPlan: Planning through mixed discrete-continuous optimization

3. PROST: Monte Carlo Tree Search (MCTS)

4. Deep Reinforcement Learning (DQN, PPO, etc.): Popular Reinforcement Learning (RL) algorithms from Stable Baselines and RLlib

5. Symbolic Dynamic Programming: Exact Symbolic regression-based planning and policy evaluation

Two possible publications were dicsussed:
 
Motivating example1: Picking fruits in a field, if there is wind in some part of the field, it increases uncertainty of the grasping operation,
so that the planner should take that into account with the newly coputed lower probabilites of grasping.
Motivating example2: If there are lots of branches, there is a higher probability of robot collision so the robot should be more compliant, and the
planner should take that into account in the harvesting regions where the clutter is more prominent.

- Initial publication, where the main contribution would be the added feedback loop for the changing probabilities, a simple case with one of the robots,
and the evaluation experiment. The feedback loop would be ran once.

- Subsequent publications would include a time-horizon approach in computing the probabilities for robot-task-level actions. At each period ex. T=15mins The algorithm would
replan the actions using new probabilities dervied from sensor data (Mimicing the MPC approach).

IMPORTANT IMPLEMENTATION DETAL: RDDL engines output actions each timestep. Import implementation detail would include either a failed_action state or init file cganges which leads to a probability reruns.
RDDL backend needs to be investigated, along with the pyRDDLGym. 

Investigation outcome:
Documentation link: https://pyrddlgym.readthedocs.io/en/latest/introduction.html
Closed loop replanning: https://pyrddlgym.readthedocs.io/en/latest/notebooks/closed_loop_replanning_with_jaxplan.html

This can be used along with a simple 2D environment, along with a modeled mobile robot with omnidirectional drive.



## Meeting 9.10.2025.

|                                                                             Task                                                                             |   Responsible   | Due |     Status    |
| :----------------------------------------------------------------------------------------------------------------------------------------------------------: | :-------------: | :-: | :-----------: |
|                                         Simulation environments for greenhouses                                  |            Nikola Ruzic, Syed Abbas Hussain          | 8.05.2025. | ⚠️ TO BE DONE |
|                                            Digital twin AL Silal                                                                 |                                     |             | ⚠️ TO BE DONE |
|                         Make an Isaac Sim based simulation for the RBKAIROS robot                                                       |         Nikola Knezevic            |		 | ⚠️ TO BE DONE |
|                                                  Refactor project report and structure multiple manuscripts                                                  | Nikola Knezevic |     | ⚠️ TO BE DONE |
|                                           Continue soft gripper experimental setup and perform grasping validation                                           |   Veljko Todic  |     | ⚠️ TO BE DONE |
|                                           Formulate   the experiment for RDDL integration with mobile stiffness shaping                                      |   Nikola Ružić  |     | ⚠️ TO BE DONE |
| Extend RDDL planner to more than 20 locations; define preconditions and reward functions; investigate idle robot behavior; modify reward to include grasping |      Sumbal     |     | ⚠️ TO BE DONE |
|                                     Integrate unloading logic, multi-robot and multi-station behavior into RDDL use-case                                     |      Sumbal     |     | ⚠️ TO BE DONE |


### Discussion Outcomes

- Knez presented the 12-month report and the grasping-probability model.

- Discussed results from mobile manipulator stiffness shaping and agreed to refactor the project report into multiple manuscripts.

- Veljko reported successful initial grasping experiments with the soft gripper setup.

- Nikola presented a literature review and draft paper for the stiffness-shaping methodology.

- Sumbal showed an RDDL planner prototype handling 20 locations, with defined action preconditions and reward functions for fruit harvesting.

- Agreed to investigate robot idle behavior and extend the reward function to include grasp success rate.

- Discussed integration of unloading logic for multi-station and multi-robot cases within RDDL.

### Additional Notes

- (Sumbal, K. Nikola, R. Nikola) Have agreed upon a seperate RDDL integration meeting @ Thursday 30.10.2025. 4PM Abu Dhabi time.


## Meeting 9.10.2025.

|                                                     Task                                                     |             Responsible             |     Due     |    Status     |
| :----------------------------------------------------------------------------------------------------------: | :---------------------------------: | :---------: | :-----------: |
|                                         Simulation environments for greenhouses                              |            Nikola Ruzic, Syed Abbas Hussain          | 8.05.2025. | ⚠️ TO BE DONE |
|                                            Digital twin AL Silal                                             |                                     |             | ⚠️ TO BE DONE |
|                         Make an Isaac Sim based simulation for the RBKAIROS robot                             |         Nikola Knezevic            |		 | ⚠️ TO BE DONE |
|                         Look into R-DDL in detail and start formulating the problem given a use-case          |         Sumbal	                     |		 | ⚠️ TO BE DONE |
|            Formulate a plan for a journal submission.                                                         |       Nikola Ruzic	             |		 | ⚠️ TO BE DONE |
|          Polish the Gazebo integration and vizualization                                                      |       Syed	             |		 | ⚠️ TO BE DONE |
|            Perform the first half of the four week plan                                              	       |       Veljko Todic             |		 | ⚠️ TO BE DONE |



### Discussion Outcomes

- Agreed on a four week plan for conditional probabilistic modeling
- Discussed a journal submission and an experiment for the mobile stiffness shaping methodology.
- Agreed on switching the planning methodology from P-PDDL to Relational  Dynamic  Influence 
Diagram Language (RDDL)
- Agreed on the integration for a high-level scenario: mobile manipulators equipped with onboard collection devices will go to the farm, grasp the fruits and, upon reaching full capacity, proceed to the unloading station. They will unload and go for another trip if needed.
- Discussed the Gazebo integration of the multi-agent smart greenhouse simulation
- Discussed the integration of a smart compliant wrist and gripper design for agriculture
- Discussed tbe application of the smart gripper design in the multi-robot case
- 
### Additional Notes

RDDL Planner - an example - PROST

Online Probabilistic planner that repeatedly computes which action to 
take  in  the  current  state,  executes  that  action  by  interacting  with 
rddlsim, observes the resulting outcome, and updates the current state 
according to the outcome.

The language is state and action - fluent, meaning it better fits into
our paradigm of addaptable, action feedback based, reactive planner.

States, can be modeled by a fluent variable

Actions, can be modeled by a fluent variable

Fluent here means dynamic, evolves with new sensor data.

Each state-fluent variable needs to have a conditional probability function describing the evolution
from one to the other state.

Mobile stiffness shaping uses a mobile manipulator to optimize and plan the stiffness
acording to the user defined trajectory and manipulator interaction requirements. It utilizes 
all of the degrees of freedom to furfil the task.





## Meeting 14.08.2025.

|                                                     Task                                                     |             Responsible             |     Due     |    Status     |
| :----------------------------------------------------------------------------------------------------------: | :---------------------------------: | :---------: | :-----------: |
|                                         Simulation environments for greenhouses                              |            Nikola Ruzic, Syed Abbas Hussain          | 8.05.2025. | ⚠️ TO BE DONE |
|                                            Digital twin AL Silal                                             |                                     |             | ⚠️ TO BE DONE |
|                         Make an Isaac Sim based simulation for the RBKAIROS robot                             |         Nikola Ruzic               |		 | ⚠️ TO BE DONE |
|                         Make an Isaac Sim based simulation for the RBKAIROS robot                             |         Nikola Ruzic               |		 | ⚠️ TO BE DONE |
|                         Look into Probabilistic PDDL in detail and start formulating the problem          |         Sumbal	                     |		 | ⚠️ TO BE DONE |
|            Investigate stiffness values for the grasping actions and how these can be encoded into PDDL actions.	       |       Nikola Ruzic	             |		 | ⚠️ TO BE DONE |
|          Continue working on the experiments for logistics use case.	       |       Syed	             |		 | ⚠️ TO BE DONE |



### Discussion Outcomes
- Agreed on the high-level scenario: mobile manipulators equipped with onboard collection devices will go to the farm, grasp the fruits and, upon reaching full capacity, proceed to the unloading station. They will unload and go for another trip if needed.
- Probabilistic PDDL will be used to model the task planning part and to generate a policy-based plan.
- The objective can be to maximize goal reachability and the mission success rate.

### Additional Notes
- Determine how to tune the probabilities for the actions.
- Examine grasping constraints closely and define a well-structured global objective.
   One possible objective could be to minimize fruit waste in case the robot fails to grasp properly.


## Meeting 31.07.2025.

|                                                     Task                                                     |             Responsible             |     Due     |    Status     |
| :----------------------------------------------------------------------------------------------------------: | :---------------------------------: | :---------: | :-----------: |
|                                         Simulation environments for greenhouses                              |            Nikola Ruzic, Syed Abbas Hussain          | 8.05.2025. | ⚠️ TO BE DONE |
|                                            Digital twin AL Silal                                             |                                     |             | ⚠️ TO BE DONE |
|                         Make an Isaac Sim based simulation for the RBKAIROS robot                             |         Nikola Ruzic               |		 | ⚠️ TO BE DONE |
|                         Make an Isaac Sim based simulation for the RBKAIROS robot                             |         Nikola Ruzic               |		 | ⚠️ TO BE DONE |
|                         Research fit of Khalifa University (KU) within the proposed topics (Planning)          |         KU	                     |		 | ⚠️ TO BE DONE |
|                         Recommended application case (ETF & KU)				                 |       ETF & KU	             |		 | ⚠️ TO BE DONE |






- Discussions about previously done work that included:

- Dicusssion about the Proposal for KU-ETF research intersection within HARBOT project
	Research aspects to be considered as novelties within the proposed topics!:
	- action plan Vs policy
	- behavior trees for replaning, based on feedback loop as novelty
   
 - Al Silal approximate simulation environemt
 - 
 - ROS2 navigation task for autonomous navigation
 - Final campus demo for autonomous navigation
 - 
 - Non-deterministic PDDL research
 - Policy based PDDL formulation
 - Proposal evaulation
   

   	



## Meeting 8.05.2025.

|                                                     Task                                                     |             Responsible             |     Due     |    Status     |
| :----------------------------------------------------------------------------------------------------------: | :---------------------------------: | :---------: | :-----------: |
|                                         Integrate Q1 and Q2 reports for BU and KU                            |            Nikola Knezevic, Sumbal Malik          | 8.05.2025. | ✅ DONE |
|                                         Simulation environments for greenhouses                              |            Nikola Ruzic, Syed Abbas Hussain          | 8.05.2025. | ⚠️ TO BE DONE |
|                                       Multi robot bug fix, Map bug fix                                       |    Nikola Knezevic, Nikola Ruzic    |             | ⚠️ TO BE DONE |
|                                            Digital twin AL Silal                                             |                                     |             | ⚠️ TO BE DONE |
|                         Make an Isaac Sim based simulation for the RBKAIROS robot                             |         Nikola Ruzic               |		 | ⚠️ TO BE DONE |
|                       Formulate a concrete plan and literature review for robot skill acquisition.           |         Nikola Ruzic               | 8.05.2025. | ✅ DONE |
|                                         K1 + GO1 Initial simulation integration                              |         Syed Abbas Hussain          | 8.05.2025. | ✅ DONE |
|                   Upgrading the capabilities for the Multi-agent PDDL planning      				|         Sumbal Malik          | 8.05.2025. | ✅ DONE |
|                       Literature review report for robot skill acquisition.          		 |         Nikola Ruzic               | 22.05.2025. | ⚠️ TO BE DONE |
|                      Develop a simple case for the ellipsoid mobile-manipulator stiffness shaping      |         Nikola Ruzic               | 22.05.2025. | ⚠️ TO BE DONE |
|                   Enabling flexible docking for drones and robots   				|         Sumbal Malik          | 22.05.2025. | ⚠️ TO BE DONE |
|                   Further work on the GO1 + arm platform web portal and sim integration	|         Syed Abbas Hussain          | 22.05.2025. | ⚠️ TO BE DONE |





- Discussions about previously done work that included:

 
  	- Completed the manual and automatic control of the GO1 simulated robot, though the web portal.

     	- Integrated a multi-visit trip for the robot fleet
  	- Tested multiple trucks and auxiliary vehicles in the PDDL

	- Manipulator impedance control integration for the RBKAIROS robot
   	- Initial research and development plan formulated


  	  
  	   




## Meeting 24.04.2025.

|                                                     Task                                                     |             Responsible             |     Due     |    Status     |
| :----------------------------------------------------------------------------------------------------------: | :---------------------------------: | :---------: | :-----------: |
|                                         Finish Q2 report                                                     |            Nikola Knezevic          | 24.05.2025. | ✅ DONE |
|                                         Integrate Q1 and Q2 reports for BU and KU                            |            Nikola Knezevic, Sumbal Malik          | 8.05.2025. | ⚠️ TO BE DONE |
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
