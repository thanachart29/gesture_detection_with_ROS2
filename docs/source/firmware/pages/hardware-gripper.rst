================
Hardware Gripper
================

Dynamixel Selection and U2D2
----------------------------
According to the mechanical team, DYNAMIXEL MX-64R can give enough Torque to drive a gripper. DYNAMIXEL MX-64 has a function to check present 
position and present load. therefore, It is easy to use for implement a control algorithm

.. image:: /images/gripper_hard1.png
    :width: 150
    :height: 210
    :align: center

Other than DYNAMIXEL MX-64R, U2D2 is select to control and operate DYNAMIXEL with PC

.. image:: /images/gripper_hard2.png
    :width: 182
    :height: 185
    :align: center

Device Setup
------------
In order to use the gripper, U2D2 will be connected to the USB port of the PC with the enclosed USB cable. We use a 4 Pin RS-485 connector 
to link up with DYNAMIXEL MX-64R and an external power supply 12V for provide power to DYNAMIXEL MX-64R

.. image:: /images/gripper_hard3.png
    :align: center

Force Sensing Resistor and Microcontroller
------------------------------------------

.. image:: /images/gripper_hard4.png
    :width: 309
    :height: 177
    :align: center

In order to use the gripper, U2D2 will be connected to the USB port of the PC with the enclosed USB cable. We use a 4 Pin RS-485 connector 
to link up with DYNAMIXEL MX-64R and an external power supply 12V for provide power to DYNAMIXEL MX-64R    

Instead of dynamixel load, FSR402 are selected. By using voltage divider circuit,A voltage from a circuit can be used to measure a resistance 
from FSR402 by following a datasheet

.. image:: /images/gripper_hard5.png
    :align: center

To read data from the sensor, a microcontroller is used. NUCLEO-L412KB is an appropriate microcontroller board because it has a small size and 
has an ADC channel for reading data.

.. image:: /images/gripper_hard6.png
    :width: 553
    :height: 376
    :align: center

Now our Gripper is using DYNAMIXEL present load only because it doesn't have to pick a fragile thing. 

| **References:**
| [1] https://emanual.robotis.com/docs/en/dxl/mx/mx-64/#control-table-data-address
| [2] https://emanual.robotis.com/docs/en/parts/interface/u2d2/
