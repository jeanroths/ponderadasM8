from launch import LaunchDescription, LaunchService
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, ExecuteProcess, RegisterEventHandler, LogInfo
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch.event_handlers import OnProcessExit, OnProcessStart

gazebo = IncludeLaunchDescription(PythonLaunchDescriptionSource([os.path.join(get_package_share_directory('turtlebot3_gazebo'), 'launch'), '/turtlebot3_world.launch.py']))

saved_map = IncludeLaunchDescription(PythonLaunchDescriptionSource([os.path.join(get_package_share_directory('turtlebot3_navigation2'), 'launch'), '/navigation2.launch.py']), launch_arguments={'use_sim_time': 'True', 'map':'pond_map.yaml'}.items())

#/Github/ponderadasM8/ponderada2/ws_pond2/src/my_turtlebot3_mapping/launch/pond_map.yaml
navigation_points = Node(
       package = 'my_turtlebot3_mapping',
       executable = 'navigation_points',
       output = 'screen'
  )

def generate_launch_description():
    return LaunchDescription([
        navigation_points,
        saved_map,
        gazebo
    ])
