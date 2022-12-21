=============
Xicro Package
=============

`Xicro <https://github.com/imchin/Xicro>`_ is ROS2 package for microcontroller interface originally made for replacing micro-ROS. 
Xicro allows the developers to use the generated libraries for the microcontrollers as well as auto-generated node that intrepreter
information from/to the microcontrollers via UART. In this documentation, Xicro is used for transmit navigation message from microcontroller
to ROS2 including Odometry and Imu measurement. Also from ROS2 to microcontroller including Twist for robot velocity command.


Create custom message for microcontroller interface
---------------------------------------------------
In the ``xicro_interfaces/msg`` directory, create 3 new files for navigation message including ``Odometry.msg``, ``Imu.msg`` and 
``DiffDriveTwist.msg`` then write below codes to each file to create custom message.

Type: xicro_interfaces/msg/Odometry

.. code-block::

    xicro_interfaces/Pose pose
    xicro_interfaces/Twist twist

Type: xicro_interfaces/msg/Imu

.. code-block::

    xicro_interfaces/Quaternion orientation  
    xicro_interfaces/Vector3 angular_velocity
    xicro_interfaces/Vector3 linear_acceleration

Type: xicro_interfaces/msg/DiffDriveTwist

.. code-block::

    float32 linear
    float32 angular

Setup parameter in setup_xicro.yaml
-----------------------------------
In xicro yaml file, Set Baudrate to ``576000`` for a highest transmission rate of Xicro, then declare topics for all navigation 
messages in ``Setup_Publisher`` and ``Setup_Subscriber``. Microcontroller port is set to ``/dev/ttyACM0`` from :ref:`Hardware setup <mcuport>`.

.. code-block:: yaml

    Idmcu: 3
    Namespace: "sub_N_pub"
    Port: "/dev/ttyACM0"
    generate_library_Path: "xicro/libraries"
    Baudrate: 576000
    Setup_Publisher:  [ [1,"nav_stm32","xicro_interfaces/Odometry.msg"], [2,"imu_stm32","xicro_interfaces/Imu.msg"] ]
    Setup_Subscriber: [ [1,"cmd_vel_stm32","xicro_interfaces/DiffDriveTwist.msg"] ]
    Setup_Srv_client: []

Create xicro library for microcontroller
----------------------------------------
After yaml config, The stm32 library will be generated based on setup_xicro.yaml when run the following command:

.. code-block:: 

    ros2 run xicro_pkg generate_library.py stm32 stm32h7xx_hal.h

Stm32 library will be generated in ``~/xicro/libraries``. So you need to bring this ``.h`` and ``.cpp`` to your stm32 project.

Create xicro node
-----------------
The node will be generated based on setup_xicro.yaml when run the following command:

.. code-block:: 

    ros2 run xicro_pkg generate_xicro_node.py stm32

.. caution:: 
    After running the command, VScode will display the node that was created.
    Delete line 11 ``!Delete this line to verify the code.`` and save it The entry point is add auto by command.

Create navigation message publisher node
----------------------------------------
This node is not an native xicro node. It's made in ``xicro_pkg/scripts`` just to create interface node between microcontroller and ROS2 in order 
to publish and subscribe navigation message. These are all interface topics and files in ``nav_msg_publisher`` node:

- Navigation Interface
  
  * Publish Topic
  
    + /imu/data (sensor_msgs/msg/Imu)
    + /wheel/odometry (nav_msgs/msg/Odometry)
  
  * Subscribe Topic
  
    + /cmd_vel (geometry_msgs/msg/Twist)

- Microcontroller Interface
  
  * Publish Topic
  
    + /cmd_vel_stm32 (xicro_interfaces/msg/DiffDriveTwist)
  
  * Subscribe Topic
  
    + /imu_stm32 (xicro_interfaces/msg/Imu)
    + /nav_stm32 (xicro_interfaces/msg/Odometry)

- Imu Calibration Interface
  
  * Yaml file

    + calibration/config/sensor_properties.yaml

In ``nav_msg_publisher.py``, create yaml file interface to load imu sensor properties from calibration-package:

.. code-block:: python3

    # Load Imu calibration value from Yaml file
    calibration_gen_path = get_package_share_directory('calibration')
    path = os.path.join(calibration_gen_path,'config','sensor_properties.yaml')
    with open(path) as f:
        self.properties = yaml.load(f, Loader=yaml.loader.UnsafeLoader)
    
    print("Load IMU calibration file: 'sensor_properties.yaml' in share calibration package Success...")
    
    # Set imu calibration value from yaml file
    self.lin_acc_x_bias = self.properties['mean'][0]
    self.lin_acc_y_bias = self.properties['mean'][1]
    self.lin_acc_z_bias = self.properties['mean'][2]
    self.ang_vel_x_bias = self.properties['mean'][3]
    self.ang_vel_y_bias = self.properties['mean'][4]
    self.ang_vel_z_bias = self.properties['mean'][5]
    # Set imu variance from yaml file
    self.lin_acc_x_var = self.properties['covariance'][0]
    self.lin_acc_y_var = self.properties['covariance'][7]
    self.lin_acc_z_var = self.properties['covariance'][14]
    self.ang_vel_x_var = self.properties['covariance'][21]
    self.ang_vel_y_var = self.properties['covariance'][28]
    self.ang_vel_z_var = self.properties['covariance'][35]

After receiving imu message from microcontroller, create ``callback_imu_stm32`` to calibrate imu raw data with sensor properties 
and make standard ros2 imu message (sensor_msgs/msg/Imu)

.. code-block:: python3

    def callback_imu_stm32(self,msg:imu):
        # Assign value from imu msg to node internal value
        self.imu_orientation = msg.orientation
        self.imu_angular_velocity = msg.angular_velocity
        self.imu_linear_acceleration = msg.linear_acceleration
        # Publish Imu to navigation (with same rate of controller)
        imu_msg = Imu()
        imu_msg.header.frame_id="base_footprint"
        now = self.get_clock().now()
        imu_msg.header.stamp = now.to_msg()

        # Linear acceleration
        imu_msg.linear_acceleration.x = self.imu_linear_acceleration.x - self.lin_acc_x_bias
        imu_msg.linear_acceleration.y = self.imu_linear_acceleration.y - self.lin_acc_y_bias
        imu_msg.linear_acceleration.z = self.imu_linear_acceleration.z - self.lin_acc_z_bias
        
        # Angular velocity
        imu_msg.angular_velocity.x = self.imu_angular_velocity.x - self.ang_vel_x_bias
        imu_msg.angular_velocity.y = self.imu_angular_velocity.y - self.ang_vel_y_bias
        imu_msg.angular_velocity.z = self.imu_angular_velocity.z - self.ang_vel_z_bias

        # Orientation
        imu_msg.orientation.x = self.imu_orientation.x
        imu_msg.orientation.y = self.imu_orientation.y
        imu_msg.orientation.z = self.imu_orientation.z
        imu_msg.orientation.w = self.imu_orientation.w

        imu_msg.linear_acceleration_covariance =[self.lin_acc_x_var,0.0,0.0,0.0,self.lin_acc_y_var,0.0,0.0,0.0,self.lin_acc_z_var]
        imu_msg.angular_velocity_covariance=[self.ang_vel_x_var,0.0,0.0,0.0,self.ang_vel_y_var,0.0,0.0,0.0,self.ang_vel_z_var]
        imu_msg.orientation_covariance=[0.000000001,0.0,0.0,0.0,0.000000001,0.0,0.0,0.0,0.000000001]
    
        self.imu_publisher.publish(imu_msg)

After receiving odometry message from microcontroller, create ``callback_nav_stm32`` to fill original data with pose covariance and 
twist covariance to make standard odometry message (nav_msgs/msg/odometry)

.. code-block:: python3

    def callback_nav_stm32(self,msg:odom):
        # Assign value from odom msg to node internal value
        self.robot_pose = msg.pose
        self.robot_twist = msg.twist
        # Publish Odometry to navigation (with same rate of controller)
        odom_msg = Odometry()
        odom_msg.header.frame_id="odom"
        now = self.get_clock().now()
        odom_msg.header.stamp = now.to_msg()
        odom_msg.child_frame_id="base_footprint"

        # PoseWithCovariance
        odom_msg.pose.pose.position.x = self.robot_pose.position.x
        odom_msg.pose.pose.position.y = self.robot_pose.position.y
        odom_msg.pose.pose.position.z = self.robot_pose.position.z
        odom_msg.pose.pose.orientation.x = self.robot_pose.orientation.x
        odom_msg.pose.pose.orientation.y = self.robot_pose.orientation.y
        odom_msg.pose.pose.orientation.z = self.robot_pose.orientation.z
        odom_msg.pose.pose.orientation.w = self.robot_pose.orientation.w

        odom_msg.pose.covariance = [0.1, 0.0, 0.0, 0.0, 0.0, 0.0,
                                    0.0, 0.1, 0.0, 0.0, 0.0, 0.0,
                                    0.0, 0.0, 0.000000001, 0.0, 0.0, 0.0,
                                    0.0, 0.0, 0.0, 0.000000001, 0.0, 0.0,
                                    0.0, 0.0, 0.0, 0.0, 0.000000001, 0.0,
                                    0.0, 0.0, 0.0, 0.0, 0.0, 0.1,]
        # TwistWithCovariance
        odom_msg.twist.twist.linear.x = self.robot_twist.linear.x
        odom_msg.twist.twist.linear.y = self.robot_twist.linear.y
        odom_msg.twist.twist.linear.z = self.robot_twist.linear.z
        odom_msg.twist.twist.angular.x = self.robot_twist.angular.x
        odom_msg.twist.twist.angular.y = self.robot_twist.angular.y
        odom_msg.twist.twist.angular.z = self.robot_twist.angular.z

        odom_msg.twist.covariance = [0.00477649365, 0.0, 0.0, 0.0, 0.0, 0.0,
                                    0.0, 0.000000001, 0.0, 0.0, 0.0, 0.0,
                                    0.0, 0.0, 0.000000001, 0.0, 0.0, 0.0,
                                    0.0, 0.0, 0.0, 0.000000001, 0.0, 0.0,
                                    0.0, 0.0, 0.0, 0.0, 0.000000001, 0.0,
                                    0.0, 0.0, 0.0, 0.0, 0.0, 0.0530721471,]
        
        self.wheel_odometry_publisher.publish(odom_msg)

When navigation node send command velocity to control mobile robot, ``cmd_vel_callback`` will extract only linear velocity of x and 
angular velocity of z to make custom twist message then sent to microcontroller via Xicro.

.. code-block:: python3

    def cmd_vel_callback(self,msg:Twist):
        # Assign value from twist msg to node internal value
        self.robot_cmd_vel.linear = msg.linear.x
        self.robot_cmd_vel.angular = msg.angular.z
        # Publish DiffDriveTwist to robot (with same rate of command velocity)
        twist_msg = DiffDriveTwist()
        twist_msg = self.robot_cmd_vel
        self.robot_twist_publisher.publish(twist_msg)