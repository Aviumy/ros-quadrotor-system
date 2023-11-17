#!/usr/bin/env python

import rospy

if __name__ == '__main__':
    rospy.init_node('my_first_python_node')
    rospy.loginfo('my_first_python_node started.')
    
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        rospy.loginfo('Test')
        rate.sleep()
