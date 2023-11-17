#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist, Vector3
from hector_uav_msgs.srv import EnableMotors


def enable_motors(service):
    rospy.wait_for_service(service)
    try:
        client = rospy.ServiceProxy(service, EnableMotors)
        response = client(True)
    except rospy.ServiceException as e:
        rospy.logwarn('Service failed: ' + str(e))


if __name__ == '__main__':
    rospy.init_node('quadrotors_group_flight_controller.py', anonymous=False)

    quadrotor_count = rospy.get_param('/quadrotor_count')
    publishers = []

    for i in range(1, quadrotor_count + 1):
        publishers.append(rospy.Publisher('/uav' + str(i) + '/cmd_vel', Twist, queue_size=10))
        enable_motors('/uav' + str(i) + '/enable_motors')

    publish_frequency = rospy.get_param('/cmd_vel_publish_frequency')
    rate = rospy.Rate(publish_frequency)

    while not rospy.is_shutdown():
        for i in range(quadrotor_count):
            msg = Twist()
            msg.linear = Vector3(z=1.0)
            publishers[i].publish(msg)

        rate.sleep()
