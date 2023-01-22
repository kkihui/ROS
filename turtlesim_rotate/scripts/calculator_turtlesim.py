#!/usr/bin/env python

import rospy
from turtlesim_rotate.msg import data
from geometry_msgs.msg import Twist

class Calc:
    def __init__(self):
        rospy.Subscriber("/velocity_information",data, self.first_callback)
        self.pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        # Twist = linear Vector*3 & angular Vector*3 , set the initial state
        self.lx = 0
        self.ly = 0
        self.lz = 0
        self.ax = 0
        self.ay = 0
        self.az = 0
        
    def first_callback(self,info):
        self.lx = info.velo
        self.ly = 0
        self.lz = 0
        self.ax = 0
        self.ay = 0
        self.az = (info.velo / info.rad) * info.dir
        
        rospy.loginfo("-----")
        rospy.loginfo("velocity : %f",info.velo)
        rospy.loginfo("radius : %f",info.rad)
        rospy.loginfo("direction : %d",info.dir)
        rospy.loginfo("--Result of calculate--")
        rospy.loginfo("x component of linear velocity: %f",self.lx)
        rospy.loginfo("z component of angular velocity: %f",self.az)
    
    def second_publish(self):
        msg = Twist()
        msg.linear.x = self.lx
        msg.linear.y = self.ly
        msg.linear.z = self.lz
        msg.angular.x = self.ax
        msg.angular.y = self.ay
        msg.angular.z = self.az
        
        self.pub.publish(msg)
        
def main():
    rospy.init_node('calculator', anonymous=False)
    rate = rospy.Rate(1)
    
    calc = Calc()
    
    while not rospy.is_shutdown():
        calc.second_publish()
        rate.sleep()
        
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass