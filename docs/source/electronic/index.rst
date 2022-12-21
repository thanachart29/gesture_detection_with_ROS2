.. _electronic_system:

Electronic System
######################

Requirement
----------------------------------

**Functional requirements**

- The robot’s electrical system must enable all robot devices and equipment to function.

- All electrical components of the robot must have a protection system.

**Performance requirements**

- Battery of the robot when the robot operates at full load , the robot must last more than 3 hours.

- Charging time from 0-100 battery percentage must not exceed 2 times the duration of operating time (6 hours).

- The robot’s electrical system can supply a continuous current about 60A.

**Physical requirements**

- The robot must be a charging socket for easy charging.

**Interface requirements**

- The robot must have a panel that can be used to turn the robot on and off 

- The robot must have an analog display that can be used to measure the current of the robot.

- The robot must have a system to display the state of charge of the battery.

**operational requirements**

- The robot must be able to distinguish between the base and the body of the robot.

- The robot must easily be equipped with an enabling system when it comes to separating the work between the base and the body of the robot.

- The robot must have a backup system in case something crashes or doesn’t work.

System architecture
^^^^^^^^^^^^^^^^^^^^

.. image:: ./images/1.png
    :width: 480
    :align: center

|

From this diagram , it shows an overview of the entire electrical system of the robot. There are 7 subsystems consisting of battery management system , electrical sensors , electrical safety system , electrical control system , power management system , Low-level devices and High-level devices. 

First, this system has a battery as an input of the entire system. The input contains voltage and current , also voltage and current signal will be connected to electrical sensors with the function of measuring voltage and current of battery to estimate state of charge of battery and calculate load of the entire robot. 

Most important thing in the electrical system is the protection system. The main function consists of short circuit protection and overcurrent protection. This system is controlled by mechanical devices such as circuit breakers and electrical devices such as microcontrollers in electrical control systems.

After passing the protection system, it will be connected to a power management system which can regulate and stabilize voltage from battery , separate phase of current for many devices and turn the robot on and off.

Electrical control system is also an important system of the robot. Inside this system is a high performance microcontroller which is responsible for processing and controlling many devices. The main function consists of choosing a mode of operation , doing some action when the emergency button has been pressed and sending data to other sections.

The last system is low-level and high level devices that require electricity to operate. Each device requires a different form of electricity such as alternative current devices and direct current devices.

Overall robot’s schematic diagram
""""""""""""""""""""""""""""""""""

.. image:: ./images/2.png
    :width: 480
    :align: center

|

In part of overall robot’s schematic diagram notice that this schematic diagram looks similar to system architecture, but there will be some differences, for example , both electrical protection system and power management system are integrated into one system , but it will be divided in the form of installation at the base and the body of the robot instead. Electrical control system will be divided into the microcontroller part (ECS) and the panel part instead. Battery management systems and electrical sensors are integrated into one system. And finally, high-level and low-level devices are separated by the type of electricity to be used instead. Such as 24VDC devices , 5VDC devices and 220VAC devices.


.. toctree::
   :maxdepth: 1
   :hidden:
   
   docs/battery_management_system.rst