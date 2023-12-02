#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped, Pose, Point, Twist, Vector3
from math import sqrt
from quad_project_msgs.msg import DistancesToOtherQuadrotors


def callback_get_pose(msg):
    frame_id = msg.header.frame_id  # frame_id format: "uav1/xxx"
    number = int(frame_id.split('/')[0].replace('uav', ''))
    all_poses[number - 1] = msg.pose.position


if __name__ == '__main__':
    rospy.init_node('quadrotor', anonymous=True)

    quadrotor_number = rospy.get_param('/quadrotor_number')
    quadrotor_count = rospy.get_param('/quadrotor_count')

    all_poses = [None for _ in range(quadrotor_count)]
    distances = [None for _ in range(quadrotor_count)]

    pose_subscribers = []
    for i in range(1, quadrotor_count + 1):
        pose_subscribers.append(rospy.Subscriber('/uav' + str(i) + '/ground_truth_to_tf/pose', PoseStamped, callback_get_pose))

    vel_publisher = rospy.Publisher('/uav' + str(quadrotor_number) + '/cmd_vel', Twist, queue_size=10)
    distances_publisher = rospy.Publisher('/uav' + str(quadrotor_number) + '/distances', DistancesToOtherQuadrotors, queue_size=10)

    publish_frequency = rospy.get_param('/controller_publish_frequency')
    rate = rospy.Rate(publish_frequency)

    while not rospy.is_shutdown():
        vel_msg = Twist()
        vel_msg.linear = Vector3(z=1.0)
        vel_publisher.publish(vel_msg)

        self_pose = all_poses[quadrotor_number - 1]
        for i in range(quadrotor_count):
            if all_poses[i] is not None:
                distance = sqrt(
                    (all_poses[i].x - self_pose.x) ** 2 +
                    (all_poses[i].y - self_pose.y) ** 2 +
                    (all_poses[i].z - self_pose.z) ** 2
                )
                distances[i] = distance
        
        message = DistancesToOtherQuadrotors()
        message.quadrotor_number = quadrotor_number
        message.distances = distances
        distances_publisher.publish(message)
        

        rate.sleep()
