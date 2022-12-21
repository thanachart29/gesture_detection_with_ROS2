==============
Wheel Odometry
==============

Related Subsystem
-----------------

.. image:: /images/odometry_test.png
    :align: center

Objective
---------
Efficiency of the wheel odometry computation process of the robot was evaluated after integration of both high-level and low-lovel systems 
consisting of the main computational subsystems **Hub motor interface, Wheel velocity estimation, Forward kinematics, Wheel odometry computation** 
by measuring the tolerance of the robot current position (x, y)

Procedure
---------

#. Turn on manual robot control using teleop_twist_keyboard
#. Control the robot to move forward in the x-axis of the odom frame to 10 cm, 20 cm, 30 cm, 40 cm, and 50 cm for 10 times
#. Control the robot to move forward in the y-axis of the odom frame to 10 cm, 20 cm, 30 cm, 40 cm, and 50 cm for 10 times
#. Take the value (x, y) from topic: wheel/odometry then calculate tolerance compared to the actual distance traveled
#. Evaluate the efficiency of the wheel odometry process

Results
-------

X-axis of odom frame
~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: Displacement(cm),Trial 1,Trial 2,Trial 3,Trial 4,Trial 5,Trial 6,Trial 7,Trial 8,Trial 9,Trial 10,Error

    10,16.301,15.666,14.385,15.109,14.806,13.824,15.326,14.754,12.798,14.759,6.301
    20,24.148,25.648,24.634,25.608,23.975,24.009,27.571,26.895,24.896,25.131,7.571
    30,33.171,34.045,37.269,38.018,37.849,37.198,37.445,34.058,35.816,34.092,8.018
    40,41.120,45.389,47.653,47.928,44.554,48.872,46.679,47.987,49.983,41.452,9.983
    50,58.673,60.765,58.292,58.718,59.240,59.934,59.685,54.303,58.012,54.778,10.765

X-axis analysis
~~~~~~~~~~~~~~~
Wheel odometry calculations can give the robot position in the x-axis of the odom frame with a maximum tolerance of **10.765 cm**
within a displacement of 50 cm.

Y-axis of odom frame
~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: Displacement(cm),Trial 1,Trial 2,Trial 3,Trial 4,Trial 5,Trial 6,Trial 7,Trial 8,Trial 9,Trial 10,Error

    10,13.053,13.918,10.839,12.218,14.411,18.399,13.068,13.633,10.771,12.512,8.399
    20,24.618,26.900,21.512,21.728,28.835,27.147,27.358,25.806,26.171,28.651,8.835
    30,35.500,39.764,35.651,36.811,37.807,41.850,38.883,33.653,37.776,38.319,11.850
    40,48.260,47.996,44.945,46.897,51.780,48.071,53.822,45.850,48.139,50.887,13.822
    50,62.130,60.422,58.491,60.030,63.659,65.620,64.561,58.032,67.028,67.626,17.028

Y-axis analysis
~~~~~~~~~~~~~~~
Wheel odometry calculations can give the robot position in the x-axis of the odom frame with a maximum tolerance of **17.028 cm** 
within a displacement of 50 cm.