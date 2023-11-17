#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist, Vector3
from hector_uav_msgs.srv import EnableMotors


if __name__ == '__main__':
    rospy.init_node('quadrotor_flight_controller', anonymous=False)

    publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    rospy.wait_for_service('/enable_motors')
    try:
        client = rospy.ServiceProxy('/enable_motors', EnableMotors)
        response = client(True)
    except rospy.ServiceException as e:
        rospy.logwarn('Service failed: ' + str(e))

    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        msg = Twist()
        msg.linear = Vector3(z=1.0)

        publisher.publish(msg)

        rate.sleep()
