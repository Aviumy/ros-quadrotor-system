#!/usr/bin/env python

import rospy
from std_msgs.msg import String


def callback_robot_news(msg):
    rospy.loginfo('Message received: ' + str(msg))


if __name__ == '__main__':
    rospy.init_node('smartphone', anonymous=True)
    rospy.loginfo('smartphone started.')

    subscriber = rospy.Subscriber('/robot_news', String, callback_robot_news)    

    rospy.spin()
