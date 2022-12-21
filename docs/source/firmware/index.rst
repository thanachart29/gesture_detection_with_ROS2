.. MBSE-2022-1/Firmware-Team documentation master file, created by
   sphinx-quickstart on Mon Dec  5 15:21:19 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

MBSE-2022-1/Firmware-Team Documentation
=======================================
**MEMBERS**

#. Nattapat Jatuwong   63340500011 (Mobile Robot)
#. Paphada  Prasongsuk 63340500033 (Gripper)
#. Sorapas  Weerakul   63340500064 (Mobile Robot)

RoboCup@Home Requirement
------------------------
SAFE NAVIGATION (indoors, with obstacle avoidance)

Mobile Robot Requirement
------------------------
- **The robot must automatically move to the position specified by the user** 

  * Firmware system must calculate the current robot's pose for navigation
  
    + Pose is calculated using wheel odometry from the robot twist
  
  * The robot must move at a safe speed for its surroundings 
    
    + The robot must move at a linear velocity no more than 0.1335 m/s
 
  * The robot must have a manual control for quick setup and repositioning
    
    + Users must control the robot with Teleop twist keyboard on ROS2.
 
  * Firmware system must be able to interface between ROS2

    + ROS2 must send a velocity command to make the robot move at a desired speed
    + The microcontroller must be able to send the robot's pose and imu raw data to ROS2
    + Communication between devices must be implemented with a frequency greater than or equal to 20 Hz
 

Gripper Requirement
-------------------
- **The gripper must be able to pick up items without dropping them and the user can control the opening/closing of the gripper**
  
  * Firmware system must apply the gripper's force to properly pick up objects
  
    + Use a sensor such as present load from DYNAMIXEL to measure the force used to pick up objects
  
  * Firmware system must be able to interface between ROS2
    
    + ROS2 must command the gripper to pick up or release an object

System Architecture
-------------------
- **Firmware Architecture**

   .. image:: /images/firmware_architecture.png

  * Hardwares and Connection
  
    + :doc:`Microcontroller </pages/microcontroller>`
    + :doc:`Hub Motor and Driver </pages/hub-motor-and-driver>`
    + :doc:`IMU Sensor </pages/imu-sensor>`

  * Microcontroller Subsystem

    + :doc:`Hub Motor Interface </pages/hub-motor-interface>`
    + :doc:`IMU Interface </pages/imu-interface>`
    + :doc:`Wheel Velocity Estimation </pages/wheel-velocity-estimation>`
    + :doc:`Forward Kinematics </pages/forward-kinematics>`
    + :doc:`Inverse Kinematics </pages/inverse-kinematics>`
    + :doc:`Wheel Odematry Computation </pages/wheel-odometry-computation>`
    + :doc:`ROS2 Interface </pages/ros2-interface>`

.. _ros2Arc:

- **ROS2 Architecture**

   .. image:: /images/ros2_architecture.png
      
  * :doc:`ROS2 Setup </pages/ros2-setup>`
  
    + Calibration and xicro installation
    + Microcontroller port check
  
  * :doc:`Xicro Package </pages/xicro-package>`
  * :doc:`Calibration Package </pages/calibration-package>`
  * :doc:`Steps to open ROS2 nodes </pages/step-to-open>`

.. toctree::
   :maxdepth: 3
   :caption: Hardwares and Connection:
   :hidden:

   pages/microcontroller
   pages/hub-motor-and-driver
   pages/imu-sensor

.. toctree::
   :maxdepth: 3
   :caption: Microcontroller Subsystem:
   :hidden:

   pages/hub-motor-interface
   pages/imu-interface
   pages/wheel-velocity-estimation
   pages/forward-kinematics
   pages/inverse-kinematics
   pages/wheel-odometry-computation
   pages/ros2-interface

.. toctree::
   :maxdepth: 3
   :caption: ROS2:
   :hidden:

   pages/ros2-setup
   pages/xicro-package
   pages/calibration-package
   pages/step-to-open

.. toctree::
   :maxdepth: 3
   :caption: Gripper:
   :hidden:

   pages/hardware-gripper
   pages/control-algorithm

.. toctree::
   :maxdepth: 3
   :caption: Test and Evaluation:
   :hidden:

   pages/process-timing
   pages/wheel-odometry
   pages/gripper-experiment
   pages/summary

Links
=====

* Source code 1: https://github.com/MBSE-2022-1/Firmware-Team
* Source code 2: https://github.com/VeroAlfa/firmware
* Firmware-only Documentation: https://firmware-docs.readthedocs.io/en/latest/
* Presentation: `Canva <https://www.canva.com/design/DAFJLsuDONk/y8OhFXQYMBOMdz5iGOFIEg/view?utm_content=DAFJLsuDONk&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink>`_