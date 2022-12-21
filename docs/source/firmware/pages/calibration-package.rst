===================
Calibration Package
===================

Calibration subscriber
----------------------
  
* Publish Topic

  + /imu/data (sensor_msgs/msg/Imu)
  + /wheel/odometry (nav_msgs/msg/Odometry)

* Subscribe Topic

  + /imu_stm32 (xicro_interfaces/msg/Imu)

* Number of samples: 500
* Data: [msg.linear_acceleration.x, msg.linear_acceleration.y, msg.linear_acceleration.z, msg.angular_velocity.x, msg.angular_velocity.y, msg.angular_velocity.z]

.. code-block:: python3

    class Calibration(Node):
        def __init__(self,action_server):
            super().__init__('calibration_subscriber')
            self.sensor_sub = self.create_subscription(Imu,'/imu_stm32',self.sensor_callback,10)
            self.action_server = action_server
            self.isEnable = False
            self.counter = 0
            self.num_sample = 100
        def sensor_callback(self,msg:Imu):
            temp = [msg.linear_acceleration.x, msg.linear_acceleration.y, msg.linear_acceleration.z, msg.angular_velocity.x, msg.angular_velocity.y, msg.angular_velocity.z]
            self.action_server.sensor_data = temp

Calibration server
------------------

* Action Server

  + /calibrate

* Output Yaml file

  + calibration/config/sensor_properties.yaml

* Sampling duration per action + Calibration process: 5-10 s

.. code-block:: python3

    class CalibrationActionServer(Node):
        def __init__(self):
            super().__init__('calibration_server')
            self.rate = self.create_rate(10)
            self.action_server = ActionServer(self,Calibrate,'/calibrate',self.execute_callback)
            self.sensor_data = Float64MultiArray()
            self.collected_data = []
            
        def execute_callback(self,goal_handle):
            self.get_logger().info(f'Executing action...')
            self.collected_data = []
            feedback_msg = Calibrate.Feedback()
            num = goal_handle.request.num
            for i in range(num):
                self.collected_data.append(self.sensor_data)
                feedback_msg.data = self.sensor_data
                goal_handle.publish_feedback(feedback_msg)
                self.rate.sleep()
            # get result to succeed
            goal_handle.succeed()
            data_array = np.array(self.collected_data)
                
            # return absolute distance as result
            result = Calibrate.Result()
            result.mean = np.mean(data_array,0).tolist()
            shape = np.cov(data_array.T).shape
            result.covariance = np.reshape(np.cov(data_array.T),(shape[0]*shape[1])).tolist()
            calibration_path = get_package_share_directory('calibration')
            file = os.path.join(calibration_path,'config','sensor_properties.yaml')
            with open(file,'w') as f:
                yaml.dump({'mean': result.mean, 'covariance': result.covariance},f)
            os.system("gedit "+file)
            return result