==================
Forward Kinematics
==================

Forward Velocity Kinematics
---------------------------

.. image:: /images/forward_kinematics.png
    :height: 505
    :width: 495
    :align: center

Covariance Matrix of 2D-Twist
-----------------------------

.. image:: /images/twist_covariance.png
    :height: 493
    :width: 440 
    :align: center

Implemention (Core M7)
----------------------

.. code-block:: c++

    void ForwardKinematic(float right_linvel, float left_linvel, float wheel_distance)
    {
        Robot_LinVel = (right_linvel + left_linvel)*0.5;
        Robot_AngVel = (right_linvel - left_linvel)/wheel_distance;
    }

Runtime Test
------------

.. code-block:: c++

    runstarttime = micros();
    //***************************************************************
    ForwardKinematic(estimated_rightvel, estimated_leftvel, 0.39377);
    //***************************************************************
    runtime = micros() - runstarttime;

Runtime: 0.003 ms