==================
Inverse Kinematics
==================

Inverse Velocity Kinematics
---------------------------

.. image:: /images/inverse_kinematics.png
    :height: 175
    :width: 359
    :align: center

.. image:: /images/inverse_matrix.png
    :height: 246
    :width: 472  
    :align: center

Implemention (Core M7)
----------------------

.. code-block:: c++

    void InverseKinematic(float cmd_linvel, float cmd_angvel, float wheel_distance, float wheel_radius)
    {
        float right_speed, left_speed;	// unit: m/s
        right_speed = cmd_linvel + cmd_angvel*wheel_distance*0.5;
        left_speed = cmd_linvel - cmd_angvel*wheel_distance*0.5;
        // m/s to rpm
        RightMotor_CmdVel = (right_speed * 60) / (wheel_radius * 2 * M_PI);
        LeftMotor_CmdVel = (left_speed * 60) / (wheel_radius * 2 * M_PI);
        // Saturate motor if speed is too much
        uint8_t sat_value = 15;
        if (fabs(RightMotor_CmdVel) > sat_value){
            if (RightMotor_CmdVel > 0){
                RightMotor_CmdVel = sat_value;
            }
            else if (RightMotor_CmdVel < 0){
                RightMotor_CmdVel = -sat_value;
            }
        }
        if (fabs(LeftMotor_CmdVel) > sat_value){
            if (LeftMotor_CmdVel > 0){
                LeftMotor_CmdVel = sat_value;
            }
            else if (LeftMotor_CmdVel < 0){
                LeftMotor_CmdVel = -sat_value;
            }
        }
    }

Runtime Test
------------

.. code-block:: c++

    runstarttime = micros();
    //****************************************************************
    InverseKinematic(cmd_vel_linear, cmd_vel_angular, 0.39377, 0.085);
    //****************************************************************
    runtime = micros() - runstarttime;

Runtime: 0.004 ms