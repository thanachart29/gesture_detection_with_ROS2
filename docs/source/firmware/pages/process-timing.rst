==============
Process Timing
==============

STM32 Process Timing
--------------------

* Core M7 Runtime: 1.226+0.059+0.003+0.006+0.004+0.022+7.463 = **8.783 ms**
* Core M4 Runtime: 2+2 = **4 ms**
* Sampling frequency: **100 Hz**

.. image:: /images/stm32_timing.png
    :align: center

ROS2 Publish Timing
-------------------

* Topic: /wheel/odometry **(Rate: 100 Hz)**
* Topic: /imu/data **(Rate: 100 Hz)**

.. image:: /images/publish_time.png
    :align: center