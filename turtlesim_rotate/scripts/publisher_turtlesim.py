#!/usr/bin/env python

import rospy
from turtlesim_rotate.msg import data

def whatisvelocity():
    pub = rospy.Publisher('velocity_information', data, queue_size=10)
    rospy.init_node('publisher', anonymous=False)
    msg = data()
    rate = rospy.Rate(1)
    
    while not rospy.is_shutdown():
        rospy.loginfo("-------------")
        rospy.loginfo("enter the velocity:")
        msg.velo = float(input())
        rospy.loginfo("enter the radius:")
        msg.rad = float(input())
        rospy.loginfo("enter the direction (1 = ccw, -1= cw): ")
        msg.dir = int(input())
        
        pub.publish(msg)
        
        rate.sleep()
    

if __name__ == '__main__':
    try:
        whatisvelocity()
    except rospy.ROSInterruptException:
        pass