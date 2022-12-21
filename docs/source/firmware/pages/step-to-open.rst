========================
Steps to open ROS2 nodes
========================

Open Xicro node
---------------

.. code-block::

    ros2 run xicro_pkg xicro_node_sub_N_pub_ID_3_stm32.py

Open Calibration node
---------------------

.. code-block::

    ros2 run calibration calibration_node.py
    ros2 action send_goal /calibrate calibration_interfaces/action/Calibrate "num: 500"

Open Navigation message publisher node
--------------------------------------

.. code-block::

    ros2 run xicro_pkg nav_msg_publisher.py

Open Teleop twist keyboard node
-------------------------------

.. code-block::
    
    ros2 run teleop_twist_keyboard teleop_twist_keyboard