#!/home/pumid/Desktop/athome/bin/python3

import launch
import launch_ros
import py_trees
import py_trees_ros.trees
import py_trees_ros.publishers
import py_trees_ros.subscribers
import py_trees.console as console
import rclpy
import sys
from std_msgs.msg import Empty

from detect_pointed import PointedGestureCmd
from detect_start_cmd import StartGestureCmd

def find_people_root()-> py_trees.behaviour.Behaviour:
    root = py_trees.composites.Sequence(name="Pointed Gesture")
    # root = py_trees.composites.Selector(name="Find People")

    # peopleDetect_sub = py_trees_ros.subscribers.EventToBlackboard(
    #     name = "PeopleDetect_sub",
    #     topic_name = "/is_people_sub",
    #     qos_profile=py_trees_ros.utilities.qos_profile_unlatched(),
    #     variable_name="event_isPeople"
    # )

    # peopleDetect_pub = py_trees_ros.publishers.FromBlackboard(
    #     name = "PeopleDetect_pub",
    #     topic_name = "/is_people_pub",
    #     qos_profile=py_trees_ros.utilities.qos_profile_unlatched(),
    #     topic_type= Empty,
    #     blackboard_variable="PeopleDetect"
    # )

    root.add_children([StartGestureCmd()])
    root.add_children([PointedGestureCmd()])
    return root

def tutorial_main():
    """
    Entry point for the demo script.
    """
    rclpy.init(args=None)
    root = find_people_root()

    tree = py_trees_ros.trees.BehaviourTree(
        root=root,
        unicode_tree_debug=True
    )
    try:
        tree.setup(timeout=15.0)
    except py_trees_ros.exceptions.TimedOutError as e:
        console.logerror(console.red + "failed to setup the tree, aborting [{}]".format(str(e)) + console.reset)
        tree.shutdown()
        rclpy.shutdown()
        sys.exit(1)
    except KeyboardInterrupt:
        # not a warning, nor error, usually a user-initiated shutdown
        console.logerror("tree setup interrupted")
        tree.shutdown()
        rclpy.shutdown()
        sys.exit(1)

    tree.tick_tock(period_ms=1000.0)

    try:
        rclpy.spin(tree.node)
    except KeyboardInterrupt:
        pass

    tree.shutdown()
    rclpy.shutdown()

tutorial_main()