#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

def callback(data):
    rospy.loginfo(data.data/0.15)

def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('li', Int32, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
