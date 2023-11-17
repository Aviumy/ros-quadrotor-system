#!/usr/bin/env python

import rospy
from rospy_tutorials.srv import AddTwoInts


if __name__ == '__main__':
    rospy.init_node('add_two_ints_client')
    rospy.loginfo('add_two_ints_client started.')

    rospy.wait_for_service('add_two_ints')

    try:
        client = rospy.ServiceProxy('/add_two_ints', AddTwoInts)
        response = client(10, 20)
        rospy.loginfo('Sum is ' + str(response.sum))
    except rospy.ServiceException as e:
        rospy.logwarn('Service failed: ' + str(e))
