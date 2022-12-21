===============
Microcontroller
===============

According to ZLAC706-CAN hub motor driver, the simplest way to control speed of both motors and to achieve position/speed
feedback for state estimation is Controller Area Network (CAN Bus) which is different from normal single-ended communication
like I2C or SPI because of its logic level and some additional setup to perform perfect communication. This makes the method
of communication unpopular to be installed on general purpose microcontroller like STM32F411RE. But in the same high performance
mcu family, there is a STM32H745ZI dual core mcu which has CAN peripheral called FDCAN. So we decided to use this mcu as our main
controller as it has all features we need and dual cores make it easy to prioritize tasks.

Why STM32H745ZI?
----------------
- FDCAN Peripheral is available for Controller Area Network (CAN) device communication
- Being a dual-core MCU, tasks can be managed separately for each core in order to reduce the overall runtime of the system, or to 
  manage unrelated tasks separately, such as having M7 perform kinematics matrix calculations and M4 delivering data up to ROS2
- Can check the performance of one core from another core if one of the cores is malfunctioning
- Has more peripheral numbers than STM32F411RE
- Development board NUCLEO-H745ZI-Q is available for immediate use

NUCLEO-H745ZI-Q
---------------

.. image:: /images/nucleo-h745zi-q.jpg