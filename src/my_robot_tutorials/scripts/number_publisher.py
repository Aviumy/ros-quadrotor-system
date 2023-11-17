#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64

if __name__ == '__main__':
    rospy.init_node('number_publisher', anonymous=True)
    rospy.loginfo('number_publisher started.')

    publisher = rospy.Publisher('/number', Int64, queue_size=10)

    publish_frequency = rospy.get_param('/number_publish_frequency')
    number_to_publish = rospy.get_param('/number_to_publish')

    rate = rospy.Rate(publish_frequency)

    while not rospy.is_shutdown():
        msg = Int64()
        msg.data = number_to_publish
        publisher.publish(msg)
        rate.sleep()

    rospy.loginfo('number_publisher stopped.')
