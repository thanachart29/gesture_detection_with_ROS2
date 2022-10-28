FROM nvidia/cuda:11.2.0-cudnn8-devel-ubuntu20.04

ENV ROS_DISTRO foxy
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -y
RUN apt -y install python3
RUN apt -y install python3-pip
RUN /bin/bash -c "python3 -m pip install --upgrade pip"
RUN apt-get update && apt-get install -y lsb-release && apt-get clean all
RUN apt-get upgrade -y && apt-get install apt-utils
RUN apt-get update && apt-get -y install sudo
##### ROS-desktop install
RUN apt update && apt install locales && \
	locale-gen en_US en_US.UTF-8 && \
	update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8 && \
	export LANG=en_US.UTF-8 && \
	locale && \
	apt-cache policy | grep universe

RUN apt install software-properties-common -y && \
	add-apt-repository universe

RUN apt update && apt-get upgrade -y && apt install curl gnupg2 lsb-release -y
RUN	curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key  -o /usr/share/keyrings/ros-archive-keyring.gpg
RUN mv /bin/sh /bin/sh_tmp && ln -s /bin/bash /bin/sh
RUN	echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(source /etc/os-release && echo $UBUNTU_CODENAME) main" | tee /etc/apt/sources.list.d/ros2.list > /dev/null
RUN rm /bin/sh && mv /bin/sh_tmp /bin/sh

RUN apt update && \
 	apt upgrade -y

RUN	apt install ros-foxy-desktop -y

RUN /bin/bash -c "source /opt/ros/foxy/setup.bash"
RUN echo 'source /opt/ros/foxy/setup.bash' >> /root/.bashrc

RUN apt install ros-foxy-turtlesim -y
RUN apt-get update
RUN apt-get install -qqy x11-apps

##### install intel realsense
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
RUN apt install python3-colcon-common-extensions -y
RUN source /opt/ros/${ROS_DISTRO}/setup.bash; colcon build
RUN rm /bin/sh && mv /bin/sh_tmp /bin/sh
RUN echo 'source /usr/app/src/ros2_ws/install/local_setup.bash' >> /root/.bashrc
RUN /bin/bash -c "source /usr/app/src/ros2_ws/install/local_setup.bash"

##### install additional library
WORKDIR /usr/app/src
RUN apt-get install portaudio19-dev python3-pyaudio -y
RUN apt-get install swig -y
RUN pip3 uninstall serial
RUN pip3 install torch==1.11.0
RUN pip3 install torchvision==0.12.0
RUN pip3 install torchaudio==0.11.0
RUN pip3 install tensorFlow==2.9.1
RUN pip3 install Tensorboard==2.9.1
COPY requirements.txt ./
RUN pip3 install -r requirements.txt

##### install navigation package
RUN apt-get update && apt-get upgrade -y
RUN apt install ros-foxy-navigation2 -y
RUN apt install ros-foxy-nav2-bringup -y
RUN apt install ros-foxy-turtlebot3* -y
RUN /bin/bash -c "source /opt/ros/foxy/setup.bash"
RUN /bin/bash -c "export TURTLEBOT3_MODEL=waffle"
RUN /bin/bash -c "export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/opt/ros/foxy/share/turtlebot3_gazebo/models"
####### exceptfirmware package

##### workspace
RUN mkdir -p /usr/app/src/cacao_ws
WORKDIR /usr/app/src/cacao_ws