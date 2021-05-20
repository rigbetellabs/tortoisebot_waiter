# tortoisebot_waiter
In hotels we have to send robot to multiple tables. Hence we can't manually run scripts everytime for changing goals. 
We can use a statemachine which will send the robot to different goals.

----------------------------------------------------------------------------------------------------------------------------
Install flexbe before testing:
Installing flexbe into src folder of your workspace
git clone https://github.com/team-vigir/flexbe_behavior_engine.git 
git clone https://github.com/FlexBE/flexbe_app.git
-------------------------------------------------------------------------------------------------------------------
New packages:
tortoisebotgoto_goal- There are three different scripts in the src folder for this package.
goto_goal.py  
gotogoal_avoidobstacle.py
obstacle_avoiding.py
Each can used by typing the command:
rosrun tortoisebotgoto_goal goto_goal.py (use for navigating goal without avoiding obstacle)
rosrun tortoisebotgoto_goal gotogoal_avoidobstacle.py (use for navigating to goal while avoiding obstacle)
rosrun tortoisebotgoto_goal obstacle_avoiding.py (use for avoiding  obstacle with a constant linear velocity)
------------------------------------------------------------------------------------------------------------------------------------

Flexbe states:
Flexbe allows us to simplify the intricate robot behaviour. You can use gotogoal behaviour for navigating tortoisebot to multiple goals. 
Currently robot can go to two goals using this behavior while avoiding the obstacle. However, you can always add more states if you want to navigate to more goals.
Remember to build the workspace using catkin _make before using Flexbe app
How to use flexbe:.
 roslaunch tortoisebot_gazebo tortoisebot_playground.launch
 roslaunch flexbe_app flexbe_full.launch
 And load the tortoisebot behavior which will be available by default.
 ---------------------------------------------------------------------------------------------------------------------------------------













