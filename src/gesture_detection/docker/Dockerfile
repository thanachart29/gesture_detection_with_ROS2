FROM ubuntu:20.04

RUN apt-get update -y
ENV ROS_DISTRO foxy
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN /bin/bash -c "python3 -m pip install --upgrade pip"

FROM osrf/ros:foxy-desktop

WORKDIR /usr/app/src

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get dist-upgrade -y
RUN apt install git -y
RUN apt-get install git libssl-dev libusb-1.0-0-dev libudev-dev pkg-config libgtk-3-dev -y
RUN apt-get install libglfw3-dev libgl1-mesa-dev libglu1-mesa-dev at -y
RUN apt -y install udev

RUN git clone https://github.com/IntelRealSense/librealsense.git

WORKDIR /usr/app/src/librealsense

#RUN mv /bin/sh /bin/sh_tmp && ln -s /bin/bash /bin/sh
#RUN rm /bin/sh && mv /bin/sh_tmp /bin/sh

RUN ./scripts/setup_udev_rules.sh
RUN ./scripts/patch-realsense-ubuntu-lts.sh; exit 0
RUN mkdir build
WORKDIR /usr/app/src/librealsense/build
RUN cmake ../ -DBUILD_EXAMPLES=true -DBUILD_GRAPHICAL_EXAMPLES=false
RUN make uninstall && make clean && make -j8 && make install


RUN mkdir -p /usr/app/src/ros2_ws/src
WORKDIR /usr/app/src/ros2_ws/src/
RUN git clone https://github.com/IntelRealSense/realsense-ros.git -b ros2-beta

WORKDIR /usr/app/src/ros2_ws/

RUN apt-get install python3-rosdep -y
RUN rosdep init; exit 0
RUN rosdep update
RUN rosdep install -i --from-path src --rosdistro $ROS_DISTRO --skip-keys=librealsense2 -y

RUN echo 'source /opt/ros/foxy/setup.bash' >> /root/.bashrc
RUN /bin/bash -c "source /opt/ros/foxy/setup.bash"

RUN mv /bin/sh /bin/sh_tmp && ln -s /bin/bash /bin/sh
RUN source /opt/ros/${ROS_DISTRO}/setup.bash; colcon build
RUN rm /bin/sh && mv /bin/sh_tmp /bin/sh

RUN echo 'source /usr/app/src/ros2_ws/install/local_setup.bash' >> /root/.bashrc
RUN /bin/bash -c "source /usr/app/src/ros2_ws/install/local_setup.bash"

FROM nvidia/cuda:11.2.0-cudnn8-devel-ubuntu20.04
FROM tensorflow/tensorflow:latest-gpu-jupyter

WORKDIR /usr/app/src
RUN mkdir -p /usr/app/src/tesnsorflow_test/src
WORKDIR /usr/app/src/tesnsorflow_test/src

COPY test_tensorflow.py ./
#CMD ["python3", "./test_tensorflow.py"]