#!/usr/bin/env python
import rospy 
from sensor_msgs.msg import LaserScan # LaserScan type message is defined in sensor_msgs
from geometry_msgs.msg import Twist 

def callback(dt):
    
    print '-------------------------------------------'
    print 'Range data at 0 deg:   {}'.format(dt.ranges[0])
    print 'Range data at 15 deg:  {}'.format(dt.ranges[15])
    print 'Range data at 345 deg: {}'.format(dt.ranges[345])
    print '-------------------------------------------'
    thr1 = 0.8 # Laser scan range threshold
    thr2 = 0.8
    if dt.ranges[0]>thr1 and dt.ranges[15]>thr2 and dt.ranges[345]>thr2: 
                                                                         
									 
        move.linear.x = 0.5 
        move.angular.z = 0.0 
    else:
        move.linear.x = 0.0 # stop
        move.angular.z = 0.5 # rotate counter-clockwise
        if dt.ranges[0]>thr1 and dt.ranges[15]>thr2 and dt.ranges[345]>thr2:
            move.linear.x = 0.5
            move.angular.z = 0.0
    pub.publish(move) # publish the move object


move = Twist() # Creates a Twist message type object
rospy.init_node('obstacle_avoidance_node') # Initializes a node
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
                            				 
sub = rospy.Subscriber("/scan", LaserScan, callback)  
                                                      
						      

rospy.spin() 

