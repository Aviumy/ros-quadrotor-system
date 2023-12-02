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

    for i in range(1, quadrotor_count + 1):
        enable_motors('/uav' + str(i) + '/enable_motors')
