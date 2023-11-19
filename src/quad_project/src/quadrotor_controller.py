#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped, Pose, Point


def callback_get_pose(msg):
    # rospy.loginfo(str(msg.pose.position))
    # Publish pose and quad number with custom msg type
    pose_publisher.publish(msg.pose.position)


if __name__ == '__main__':
    rospy.init_node('quadrotor', anonymous=True)
    
    quadrotor_number = rospy.get_param('/quadrotor_number')

    pose_publisher = rospy.Publisher('/uav' + str(quadrotor_number) + '/pose', Point, queue_size=10)
    pose_subscriber = rospy.Subscriber('/uav' + str(quadrotor_number) + '/ground_truth_to_tf/pose', PoseStamped, callback_get_pose)

    rospy.spin()
