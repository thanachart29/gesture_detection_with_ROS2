CACAO camera
#############

eiei zaza we use d455 camera naja

|

.. _[1]:

----------------------------

Usage instruction
********************

* Basic launch ros-realsens2_camera

    .. code-block:: console

        ros2 launch realsense2_camera rs_launch.py \
                    rgb_camera.profile:=640x480x30 \
                    depth_module.profile:=640x480x30 \
                    pointcloud.enable:=true

    .. note::

        *Add parameter guide*

        Set RGB camera parameter: rgb_camera.profile:=<width>x<heigh>x<FPS>

        Set depth camera parameter: depth_module.profile:=<width>x<heigh>x<FPS>

        Enable pointclound: pointcloud.enable:=true



* launch realsense2 in RVIZ

    .. code-block:: console

        ros2 launch realsense2_description view_model.launch.py \
                    model:=test_d455_camera.urdf.xacro

* the following command will contain topic as listed below:

    * /camera/aligned_depth_to_color/camera_info
    * /camera/aligned_depth_to_color/image_raw
    * /camera/color/camera_info
    * /camera/color/image_raw
    * /camera/color/metadata
    * /camera/depth/camera_info
    * /camera/depth/color/points
    * /camera/depth/image_rect_raw
    * /camera/depth/metadata
    * /camera/extrinsics/depth_to_color

|

----------------------------

Installation
*************

.. _[2]:

ROS2 Wrapper for Intel® RealSense™ Devices support kernel version 4.[4, 8,10,13,15], 4.16(2) , 4.18, 5.[0, 3, 4, 8]
To check your kernel version:

.. code-block:: console

    uname -r

----------------------------

.. _[3]:

* Install the latest Intel® RealSense™ SDK 2.0

    * Make Ubuntu Up-to-date

        .. code-block:: console

            sudo apt-get update && sudo apt-get upgrade && sudo apt-get dist-upgrade
            sudo update-grub && sudo reboot

    * Download/Clone librealsense github repository

        .. code-block:: console

            git clone https://github.com/IntelRealSense/librealsense.git

    * Prepare Linux Backend and the Dev. Environment

        .. code-block:: console

            sudo apt-get install git libssl-dev libusb-1.0-0-dev libudev-dev pkg-config libgtk-3-dev
            sudo apt-get install libglfw3-dev libgl1-mesa-dev libglu1-mesa-dev at


    * Run Intel Realsense permissions script from librealsense root directory

        .. code-block:: console

            cd librealsense
            ./scripts/setup_udev_rules.sh


    * Build and apply patched kernel modules for

        .. code-block:: console

            ./scripts/patch-realsense-ubuntu-lts.sh


    * Building librealsense2 SDK

        .. code-block:: console

            mkdir build && cd build
            cmake ../ -DBUILD_EXAMPLES=true -DBUILD_GRAPHICAL_EXAMPLES=false
            make uninstall && make clean && make -j8 && make install

.. _[4]:

* Install Intel® RealSense™ ROS2 wrapper from sources

    * Create a ROS2 workspace

        .. code-block:: console

            mkdir -p ~/ros2_ws/src && cd ~/ros2_ws/src/


    * Clone the latest ROS2 Intel® RealSense™ wrapper

        .. code-block:: console

            git clone https://github.com/IntelRealSense/realsense-ros.git -b ros2-beta
            cd ~/ros2_ws

    * Install dependencies

        .. code-block:: console

            sudo apt-get install python3-rosdep -y
            sudo rosdep init
            rosdep update
            rosdep install -i --from-path src --rosdistro $ROS_DISTRO --skip-keys=librealsense2 -y
        
        .. note::

            If error occurred on line 4 change command to
            `rosdep install -i --from-path src --ignore-src -r -y --rosdistro foxy`



    * Build and Terminal environment

        .. code-block:: console

            colcon build
            ##### example for foxy distro 
            ROS_DISTRO=foxy
            source /opt/ros/foxy/setup.bash && cd ~/ros2_ws
            . install/local_setup.bash




|

---------------------------

Reference
**********

`[1]`_ : https://github.com/IntelRealSense/realsense-ros/tree/ros2-development

`[2]`_ : https://github.com/IntelRealSense/librealsense/releases/tag/v2.51.1

`[3]`_ : https://github.com/IntelRealSense/librealsense/blob/master/doc/installation.md

`[4]`_ : https://github.com/IntelRealSense/realsense-ros/tree/ros2-beta
