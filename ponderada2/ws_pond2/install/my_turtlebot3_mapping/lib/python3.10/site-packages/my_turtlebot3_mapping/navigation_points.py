#! /usr/bin/env python3
import rclpy
from nav2_simple_commander.robot_navigator import BasicNavigator
from geometry_msgs.msg import PoseStamped
from tf_transformations import quaternion_from_euler
import tf_transformations
from math import pi

def create_pose_stamped(navigator, pos_x, pos_y, rot_z):
    q_x, q_y, q_z, q_w = tf_transformations.quaternion_from_euler(0.0, 0.0, rot_z)
    pose = PoseStamped()
    pose.header.frame_id = 'map'
    pose.header.stamp = navigator.get_clock().now().to_msg()
    pose.pose.position.x = pos_x
    pose.pose.position.y = pos_y
    pose.pose.position.z = pos_x
    pose.pose.orientation.x = q_x
    pose.pose.orientation.y = q_y
    pose.pose.orientation.z = q_z
    pose.pose.orientation.w = q_w
    return pose

def main():
    rclpy.init()
    navigator = BasicNavigator()

    # Defina a pose inicial
    initial_pose = create_pose_stamped(navigator, 0.0, 0.0, 0.0)


    # Defina os waypoints
    waypoints = [
        create_pose_stamped(navigator, 4.0, 1.25, -0.00143),
        create_pose_stamped(navigator, 0.0, 0.0, 0.0),
        # Adicione mais waypoints conforme necessário
    ]

    navigator.waitUntilNav2Active()
    # Envie a pose inicial
    navigator.setInitialPose(initial_pose)

    # Faça o robô seguir os waypoints
    navigator.followWaypoints(waypoints)

    # Aguarde até que a tarefa esteja completa
    while not navigator.isTaskComplete():
        print(navigator.getFeedback())

    # Desligue o nó do ROS
    rclpy.shutdown()

if __name__ == '__main__':
    main()
