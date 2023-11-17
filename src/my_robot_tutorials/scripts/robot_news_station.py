#!/usr/bin/env python

import rospy
from std_msgs.msg import String

if __name__ == '__main__':
    rospy.init_node('robot_news_station')
    rospy.loginfo('robot_news_station started.')

    publisher = rospy.Publisher('/robot_news', String, queue_size=10)
    rate = rospy.Rate(2)

    while not rospy.is_shutdown():
        msg = String()
        msg.data = 'Hello from radio station!'
        publisher.publish(msg)
        rate.sleep()

    rospy.loginfo('robot_news_station stopped.')
