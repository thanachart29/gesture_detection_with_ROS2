#!/home/pumid/Desktop/athome/bin/python3

from launch import LaunchDescription
from launch.actions import ExecuteProcess,DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    launch_description = LaunchDescription()
    image_pub = Node(
        package='gesture_detection',
        executable='image_publisher.py',
    )
    launch_description.add_action(image_pub)
    model = Node(
        package='gesture_detection',
        executable='gesture_detection.py',
    )
    launch_description.add_action(model)
    return launch_description

