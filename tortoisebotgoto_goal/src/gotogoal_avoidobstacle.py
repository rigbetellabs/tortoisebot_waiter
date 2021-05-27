#!/usr/bin/env python
import rospy 
from sensor_msgs.msg import LaserScan # LaserScan type message is defined in sensor_msgs
from geometry_msgs.msg import Twist 
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point, Twist
from math import atan2
from math import sqrt
import sys


arg1 = sys.argv[1]
arg2 = sys.argv[2]




x = 0.0
y = 0.0 
theta = 0.0
goal = Point()
goal.x = float(sys.argv[1])
goal.y = float(sys.argv[2])
a=0
s=0
d=0


def newOdom(msg):
    global x
    global y
    global theta

    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    

    rot_q = msg.pose.pose.orientation
    (roll, pitch, theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])
    
def callback(dt):
    global a
    global s
    global d
   
    global f
    global k
    a= dt.ranges[0]
    s= dt.ranges[90]
    d= dt.ranges[270]
    f= dt.ranges[360]
    k= dt.ranges[180]

    
    
    print ('-------------------------------------------')
    print ('Range data at 0 deg:   {}'.format(dt.ranges[0]))
    print ('Range data at 90 deg:  {}'.format(dt.ranges[90]))
    print ('Range data at 270 deg:  {}'.format(dt.ranges[270]))
    print ('Range data at  360deg: {}'.format(dt.ranges[360]))
    print ('-------------------------------------------')
       


move = Twist()
rospy.init_node('obstacle_avoidance_node') # Initializes a node
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)  # Publisher object which will publish "Twist" type messages
sub = rospy.Subscriber("/scan", LaserScan, callback )  
sub = rospy.Subscriber("/odom", Odometry, newOdom)
r = rospy.Rate(4)






while not rospy.is_shutdown():
    inc_x = goal.x -x
    inc_y = goal.y -y
    angle_to_goal = atan2(inc_y, inc_x)
    dist=(sqrt((inc_y**2)+(inc_x**2)))
    
    if a>0.8  and s>0.8 and d>0.8 and k>0.8 and f>0.8 :
        move.angular.z=angle_to_goal-theta 
        move.linear.x=0.15
        print('go to goal')
        print(dist)
        
       
                            
        
            
    else:
        move.linear.x=0
        move.angular.z=0.3     
        print('obstacle is there')

    if dist<0.1:
        move.angular.z=0
        move.linear.x=0  
        print('I reached goal')  







    
    
    
        
           
        
        
    
    
        


        
           
    
    pub.publish(move)
    r.sleep()    






 # Creates a Twist message type object

                                                      
						      

rospy.spin() 
