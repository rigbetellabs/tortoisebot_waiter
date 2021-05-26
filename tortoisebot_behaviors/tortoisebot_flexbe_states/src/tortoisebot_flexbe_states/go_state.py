#!/usr/bin/env python
import rospy 
from sensor_msgs.msg import LaserScan #Obtaining LaserScan type message is defined in sensor_msgs 
from nav_msgs.msg import Odometry #obtaining the odom details i.e position of tortoisebot
from tf.transformations import euler_from_quaternion ##batining the orientation of the tortoisebot
from geometry_msgs.msg import Point, Twist  # Getting the twist
from math import atan2
from math import sqrt
from flexbe_core import EventState, Logger
from flexbe_core.proxy import ProxySubscriberCached, ProxyPublisher


class GoState(EventState):
    def __init__(self,xgoal,ygoal):

        super(GoState,self).__init__(outcomes=['done','failed'])
        self._xgoal=xgoal
        self._ygoal=ygoal
            
        self.vel_topic='/cmd_vel' # It advised to store the topic as string
        self.scan_topic='/scan'   
            
        self.odom_topic='/odom'
        self.pub=ProxyPublisher({self.vel_topic:Twist})
        self.scan_subl=ProxySubscriberCached({self.scan_topic:LaserScan})
        self.scan_subl.set_callback(self.scan_topic,self.scan_callback)
        self.scan_subo=ProxySubscriberCached({self.odom_topic:Odometry})
        self.scan_subo.set_callback(self.odom_topic,self.odom_callback)
    #Here we are subscribing to required data. We define the outputs of the state machine
    #for example done and failed in this case. We are subscribing to odom and laserscan topics

    

    def execute(self,userdata):
        self.xcurrent = self.newOdom.pose.pose.position.x
        self.ycurrent = self.newOdom.pose.pose.position.y
        self.rot_q =  self.newOdom.pose.pose.orientation
        (self.roll, self.pitch, self.theta) = euler_from_quaternion([self.rot_q.x, self.rot_q.y, self.rot_q.z,self.rot_q.w])
        
        
        self.inc_x = self.goal.x -self.xcurrent
        self.inc_y = self.goal.y -self.ycurrent
        self.angle_to_goal = atan2(self.inc_y, self.inc_x)
        self.phi=self.angle_to_goal-self.theta
        self.dist=(sqrt((self.inc_y**2)+(self.inc_x**2)))
        self.a= self.data.ranges[0]
        self.s= self.data.ranges[90]
        self.d= self.data.ranges[270]
        self.f= self.data.ranges[360]
        self.k= self.data.ranges[180]
        if self.dist >0.2:
            
        
            if self.a>0.8  and self.s>0.8 and self.d>0.8 and self.k>0.8 and self.f>0.8 :
            


                self.cmd_pub.angular.z=(self.angle_to_goal-self.theta)
                self.cmd_pub.linear.x=0.15
                #self.pub.publish(self.vel_topic,self.cmd_pub)
            
            else:
                self.cmd_pub.angular.z=0.5
                

        
        

        
        elif self.dist<0.1:
                          #self.cmd_pub.angular.z=0
                          #self.cmd_pub.linear.x=0
                          return 'done'
            
        else:
            'failed'
        
        self.pub.publish(self.vel_topic,self.cmd_pub)        
        
    def scan_callback(self,data):
              self.data=data #sensor data

    def odom_callback(self,newOdom):
              self.newOdom=newOdom # odometry data


    


    def on_enter(self,userdata):
        Logger.loginfo('On enter')
        #This state is executed first when we start flexbe
        self.cmd_pub=Twist()
        self.goal=Point()
        self.goal.x=self._xgoal
        self.goal.y=self._ygoal
       
        self.xcurrent = self.newOdom.pose.pose.position.x
        self.ycurrent = self.newOdom.pose.pose.position.y
        self.rot_q =  self.newOdom.pose.pose.orientation
        (self.roll, self.pitch, self.theta) = euler_from_quaternion([self.rot_q.x, self.rot_q.y, self.rot_q.z,self.rot_q.w])
        
        
        self.inc_x = self.goal.x -self.xcurrent
        self.inc_y = self.goal.y -self.ycurrent
        self.angle_to_goal = atan2(self.inc_y, self.inc_x)
        self.phi=self.angle_to_goal-self.theta
        self.dist=(sqrt((self.inc_y**2)+(self.inc_x**2)))
        self.a= self.data.ranges[0]
        self.s= self.data.ranges[90]
        self.d= self.data.ranges[270]
        self.f= self.data.ranges[360]
        self.k= self.data.ranges[180]
       
            
    
        
        
       
                            
        
     
            
            
    def on_exit(self,userdata):
           self.cmd_pub.linear.x=0
           self.pub.publish(self.vel_topic,self.cmd_pub)
           

