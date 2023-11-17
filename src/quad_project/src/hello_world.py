#!/usr/bin/env python

import rospy
from std_msgs.msg import String

if __name__ == '__main__':
    rospy.init_node('test_node', anonymous=False)
    rospy.loginfo('Hello world!')

    publisher = rospy.Publisher('/hello_world', String, queue_size=10)

    publish_frequency = rospy.get_param('/hello_world_publish_frequency')

    rate = rospy.Rate(publish_frequency)

    while not rospy.is_shutdown():
        msg = String()
        msg.data = 'Hello world!'
        publisher.publish(msg)
        rate.sleep()
