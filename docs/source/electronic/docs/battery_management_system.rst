.. _battery_management_system:

Battery Management System
############################

schematic diagram
*****************

.. image:: ./images/3.png
    :width: 480
    :align: center

|

This battery management system comes from a combination of the original battery management system and electrical sensors. Therefore, we can divide this system into 3 parts.

- Multiple-cell battery

    From the performance requirement that the robot's battery operate at full load must last more than 3 hours , charging time about 6 hours and supply continuous current about 60A . First we need to calculate the current load of the fully operational robot. And from the calculations, the results are shown below this table.

.. image:: ./images/3.png
    :width: 480
    :align: center

|

- Battery Voltage level selection

    From the table above, when we know how much power that a robot uses. Then, we will choose the voltage of the battery that we will use with our robot. By selecting voltage we must consider about current flow in the system and the device in the robot.

.. image:: ./images/4.png
    :width: 480
    :align: center

|

    So, we choose a battery with 24V voltage because 12V makes the current in the system flow too high and 48V will make the battery unnecessarily large. But 24V will make the current available in the system meet the set requirements at about 60A.

- Battery capacity selection

    From voltage level selection, we will use a 24V battery with 62.625A supply current at full operation. If we need to use this robot for 3 hours, we will use battery at least 

    Capacity = Current  hours of use = 62.625  3 = 187.875 Ah

.. note:: In this project, we use a custom battery of 220Ah capacity because of store production restrictions.

- Battery type selection

    From the performance requirement that supply continuous current is about 60A and charging time about 6 hours. So, discharge rate and charge rate of the battery is

    .. math:: 

        Discharge rate = \frac{supply current}{capacity} = 62.625187.875 = 0.33 C \\
        Charge rate = \frac{1}{charging time} = 16 = 0.17 C

    In terms of robot usage and its application, it makes us choose to use NMC batteries (Lithium Nickel Manganese Cobalt Oxide Batteries) because NMC batteries have a high specific energy or power. This limitation of either ‘energy’ or ‘power’ makes them more common for use in power tools or electric vehicles. (Specific power is power per unit mass, and specific energy is energy content per unit mass.) 

- Battery characteristics

.. image:: ./images/5.png
    :width: 480
    :align: center

|

    From the table above, the result can be summarized as follows:

    - The NMC battery will fully charge at about 4.15 - 4.2 V.
    - The NMC battery has nominal voltage at about 3.75 - 3.55 V.
    - The NMC battery has a cut-off discharge voltage at below 2.95 V. 

- Number of cells of the battery

    From voltage level selection, we need to use a 24V battery as nominal voltage. So, The number  of cells of the battery is

    .. math:: Number of cells = \frac{Battery pack voltage}{nominal cell voltage}=243.5=6.86 =7 cells 