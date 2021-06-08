# tortoisebot_waiter
In hotels we have to send robot to multiple tables. Hence we can't manually run scripts everytime for changing goals. 
We can use a statemachine which will send the robot to different goals.

Install flexbe before testing:

Installing flexbe into src folder of your workspace

git clone https://github.com/team-vigir/flexbe_behavior_engine.git 

git clone https://github.com/FlexBE/flexbe_app.git

New packages:
tortoisebotgoto_goal this packege contains python script for navigating to a goal using movebase. 

Enter the coordinate where you want sent the robot 

rosrun tortoisebotgoto_goal.py gottogoal.py x-coordinate y-coordinate

for example 
r
osrun tortoisebotgoto_goal.py gottogoal.py -0.4 0.3


Flexbe states:
Flexbe allows us to simplify the intricate robot behaviour. You can use gotogoal behaviour for navigating tortoisebot to multiple goals. 
MOVEBASESATE- This state allows us to navigate the robot to a goal.You can navigate the robot by adding as many states you want. However you need to add waypoints in Pose2D format. Currently there are few waypoints defiened as per the playground but you can add more waypoints if required. 
How to add more state?
select tortoisebot behavior from the flexbe gui.
and from that navigation_to_goal behaviour
Click on state machine editor.
Click on add state and select movebasestate
Since there is already one behaviour present for your refrence.
Remember to build the workspace using catkin _make before using Flexbe app

How to use flexbe:.
 roslaunch tortoisebot_gazebo tortoisebot_playground.launch
 roslaunch tortoisebot_firmware server_bringup.launch
 roslaunch tortoisebot_navigation tortoisebot_navigation.launch
 roslaunch flexbe_app flexbe_full.launch
 
 select tortoisebot behavior from the flexbe gui.
 and from that navigation_to_goal behaviour
 














