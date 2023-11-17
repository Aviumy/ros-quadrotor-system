#!/usr/bin/env python

import rospy
from my_robot_msgs.msg import HardwareStatus
# from my_robot_msgs.srv import ComputeDiskArea


if __name__ == '__main__':
    rospy.init_node('hardware_status_publisher')
    # rospy.loginfo('Node started.')

    publisher = rospy.Publisher('/my_robot/hardware_status', HardwareStatus, queue_size=10)
    rate = rospy.Rate(2)

    while not rospy.is_shutdown():
        msg = HardwareStatus()
        msg.temperature = 20
        msg.are_motors_up = True
        msg.debug_message = "Everything runs fine"
        publisher.publish(msg)
        rate.sleep()

    # rospy.loginfo('Node stopped.')
