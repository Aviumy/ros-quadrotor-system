#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64
from std_srvs.srv import SetBool, SetBoolResponse


counter = 0


def callback_number(msg):
    global counter
    counter += msg.data
    publish_number_count()


def publish_number_count():
    msg = Int64()
    msg.data = counter
    publisher.publish(msg)


def handle_reset_number_count(request):
    message = ''
    if request.data:
        global counter
        counter = 0
        message = 'Counter was reset.'
    else:
        message = 'Counter was not reset.'
    rospy.loginfo(message)
    return SetBoolResponse(success=True, message=message)


if __name__ == '__main__':
    rospy.init_node('number_counter')
    rospy.loginfo('number_counter started.')

    publisher = rospy.Publisher('/number_count', Int64, queue_size=10)
    subscriber = rospy.Subscriber('/number', Int64, callback_number) 
    service = rospy.Service('/reset_number_count', SetBool, handle_reset_number_count)

    rospy.spin()

    rospy.loginfo('number_counter stopped.')
