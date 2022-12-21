==============
ROS2 Interface
==============

Implemention (Core M4)
----------------------

.. code-block:: c++

    xicro_begin(&huart3);
    while (1)
    {
        xicro_spin_node();
        shared_ptr->cmd_vel_linear = xicro_get_linvel();
        shared_ptr->cmd_vel_angular = xicro_get_angvel();
        if (shared_ptr->nav_pub_flag)
        {
            xicro_publish_nav(shared_ptr->robot_x, shared_ptr->robot_y, 0, shared_ptr->robot_qx, shared_ptr->robot_qy, shared_ptr->robot_qz,
                    shared_ptr->robot_qw, shared_ptr->robot_linvel, 0, 0, 0, 0, shared_ptr->robot_angvel);
            shared_ptr->nav_pub_flag = 0;
        }
        if (shared_ptr->imu_pub_flag)
        {
            xicro_publish_imu(shared_ptr->imu_qx, shared_ptr->imu_qy, shared_ptr->imu_qz, shared_ptr->imu_qw, shared_ptr->imu_gx, shared_ptr->imu_gy,
                    shared_ptr->imu_gz, shared_ptr->imu_ax, shared_ptr->imu_ay, shared_ptr->imu_az);
            shared_ptr->imu_pub_flag = 0;
        }
    }

Runtime Test
------------

| Xicro odometry runtime: 2 ms
| Xicro imu runtime: 2 ms