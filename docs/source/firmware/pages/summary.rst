================
Firmware Summary
================

Problems and Solutions
----------------------

Hub Motor Interface
~~~~~~~~~~~~~~~~~~~

* Since the current hub motor driver circuit is not implemented in the PCB, the CAN bus is easily affected by interference. As a result, it was not possible to transmit data at 1 MHz, so it was reduced to 500 kHz
* The speed reading from the motor can be write and read with a resolution of only 0.36621 rpm/bit, resulting in the speed commanded to the motor and the obtained value to be within ±0.36621 rpm, which is a large value in the 0 - 15 rpm operating range
* Reading position and speed values ​​from a polling function has the chance to cause the MCU to get stuck in an infinite loop, so it has to write a timeout when the called value does not return
* When the robot ramps up, it causes the driver to display a red fault indicator on the driver and causes all motor operations to be suspended

IMU Interface
~~~~~~~~~~~~~

* When reading the value of the IMU for less than 1 minute, the IMU will not be able to send data back to the board, and the runtime will increase from 7 ms to 200 ms. This will cause the board to freeze and cause other processes to fail as well. Causing the need to replace the IMU

Wheel Velocity Estimation
~~~~~~~~~~~~~~~~~~~~~~~~~

* Position were used to estimate the speed of each wheel since the resolution was 0.0878 degree/pulse. However, because the estimated speed was much less than the speed commanded to the motor, cutting position off temporary is needed

Microcontroller-ROS2 Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Since the standard ROS2 messages nav_msgs/Odometry, sensor_msgs/Imu, and geometry_msgs/Twist are very large messages, both in variable bit size and in the number of data in the array, result in the maximum transmission frequency of 10 Hz. Creating a custom message in xicro interfaces includes xicro_interfaces/Odometry, xicro_interfaces/Imu and xicro_interfaces/DiffDriveTwist To extract only the information necessary for the mobile robot and to remove the constant covariance matrix from all messages, it is possible to send information up to ROS2 at a frequency of 100 Hz

Gripper
~~~~~~~

* A gripper has a problem in the mechanical part, the gripper goes to the wrong position according to the experiment ‘Testing an appropriate force with other object’. Therefore a present load from DYNAMIXEL may change after a mechanical part has been fixed

Suggestion for Future Development
---------------------------------

Hub Motor Interface
~~~~~~~~~~~~~~~~~~~

* If the runtime of reading from the motor is required to be less than before The hub motor driver circuit can be improved to withstand more noise by making a PCB and using a shield cable to support transmission with a frequency of 1 MHz instead of 500 kHz
* Write a function for fault diagnosis when Overload, Under-voltage, Over-voltage, Encoder falling, Over-current, Overheat from Heart-beat message occur and handle appropriately
* Maybe change motor driver

Wheel Odometry
~~~~~~~~~~~~~~

* For a more accurate estimation of the robot's position, the Wheel velocity estimation can be improved by changing the Q, R matrices to achieve a more actual velocity. Or may consider returning to use the position value together as well
* Wheel odometry equation may be improved.
* Conduct an experiment to find a pose covariance matrix

Gripper
~~~~~~~

* After fixing in the mechanical part, all of the experiments will have to be retaken for checking a change of present load