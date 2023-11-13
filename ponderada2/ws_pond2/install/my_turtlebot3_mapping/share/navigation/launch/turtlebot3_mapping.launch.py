from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, ExecuteProcess, RegisterEventHandler, LogInfo
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch.event_handlers import OnProcessExit
 
gazebo = IncludeLaunchDescription(PythonLaunchDescriptionSource([os.path.join(get_package_share_directory('turtlebot3_gazebo'), 'launch'), '/turtlebot3_world.launch.py']))

teleop = Node(
    package = 'turtlebot3_teleop',
    executable = 'teleop_keyboard',
    output = 'screen',
    prefix = 'xterm -e',
)

nav2 = IncludeLaunchDescription(PythonLaunchDescriptionSource([os.path.join(get_package_share_directory('turtlebot3_cartographer'), 'launch'), '/cartographer.launch.py']), launch_arguments={'use_sim_time': 'True'}.items())

map_saver = RegisterEventHandler(
                OnProcessExit(
                    target_action=teleop,
                    on_exit=[
                        LogInfo(msg=('closing teleop window and saving the map')),
                        ExecuteProcess(
                           cmd= ["ros2", "run", "nav2_map_server", "map_saver_cli", "-f", "./pond_map"],
                           output="screen"
                            )
                    ]
                )
)
                        
def generate_launch_description():
    return LaunchDescription([
        gazebo,
        teleop,
        nav2,
        map_saver
    ])
