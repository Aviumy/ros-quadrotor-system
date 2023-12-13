#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan


def callback_get_uav_scan(msg):
    scan_publisher.publish(msg)


if __name__ == '__main__':
    rospy.init_node('uav_scan_to_scan', anonymous=False)

    scan_publisher = rospy.Publisher('/scan', LaserScan, queue_size=10)
    uav_scan_subscriber = rospy.Subscriber('/uav1/scan', LaserScan, callback_get_uav_scan)

    rospy.spin()
