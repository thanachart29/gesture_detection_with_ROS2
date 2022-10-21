# #### can change to ros desktop
# ARG ROS_BASE_IMAGE=dustynv/ros:foxy-ros-base-l4t-r35.1.0
# FROM ${ROS_BASE_IMAGE}

# RUN apt-get update && \
#     apt-get install -y --no-install-recommends \
#             python3-pip \
# 		  python3-dev \
# 		  libopenblas-dev \
# 		  libopenmpi-dev \
#             openmpi-bin \
#             openmpi-common \
# 		  gfortran \
# 		  libomp-dev \
#     && rm -rf /var/lib/apt/lists/* \
#     && apt-get clean

# RUN pip3 install --no-cache-dir setuptools Cython wheel
# RUN pip3 install --no-cache-dir --verbose numpy


# ##### pytorch
# ARG PYTORCH_URL=https://nvidia.box.com/shared/static/ssf2v7pf5i245fk4i0q926hy4imzs2ph.whl
# ARG PYTORCH_WHL=torch-1.11.0-cp38-cp38-linux_aarch64.whl
# RUN wget --quiet --show-progress --progress=bar:force:noscroll --no-check-certificate ${PYTORCH_URL} -O ${PYTORCH_WHL} && \
#     pip3 install --no-cache-dir --verbose ${PYTORCH_WHL} && \
#     rm ${PYTORCH_WHL}

# ##### torch vision
# # default torchvision v0.12.0
# ARG TORCHVISION_VERSION=v0.12.0
# ARG TORCH_CUDA_ARCH_LIST="11.2"
# RUN printenv && echo "torchvision version = $TORCHVISION_VERSION" && echo "TORCH_CUDA_ARCH_LIST = $TORCH_CUDA_ARCH_LIST"
# RUN apt-get update && \
#     apt-get install -y --no-install-recommends \
# 		  git \
# 		  build-essential \
#             libjpeg-dev \
# 		  zlib1g-dev \
#     && rm -rf /var/lib/apt/lists/* \    
#     && apt-get clean


# RUN git clone https://github.com/pytorch/vision torchvision && \
#     cd torchvision && \
#     git checkout ${TORCHVISION_VERSION} && \
#     python3 setup.py install && \
#     cd ../ && \
#     rm -rf torchvision

# RUN apt-get update && \
#     apt-get install -y --no-install-recommends \
# 		  software-properties-common \
# 		  apt-transport-https \
# 		  ca-certificates \
# 		  gnupg \
# 		  lsb-release \
#     && rm -rf /var/lib/apt/lists/* \
#     && apt-get clean

# ##### tensorflow
# ENV DEBIAN_FRONTEND=noninteractive
# ARG HDF5_DIR="/usr/lib/aarch64-linux-gnu/hdf5/serial/"
# ARG MAKEFLAGS=-j$(nproc)

# RUN printenv

# RUN apt-get update && \
#     apt-get install -y --no-install-recommends \
#           python3-pip \
# 		  python3-dev \
# 		  gfortran \
# 		  build-essential \
# 		  liblapack-dev \ 
# 		  libblas-dev \
# 		  libhdf5-serial-dev \
# 		  hdf5-tools \
# 		  libhdf5-dev \
# 		  zlib1g-dev \
# 		  zip \
# 		  unzip \
# 		  libjpeg8-dev \
# 		  autoconf \ 
# 		  automake \
# 		  libtool \
# 		  curl \
# 		  make \
# 		  g++ \
#     && rm -rf /var/lib/apt/lists/* \
#     && apt-get clean

# RUN pip3 install --no-cache-dir setuptools Cython wheel

# ARG PROTOBUF_VERSION=3.19.4
# ARG PROTOBUF_URL=https://github.com/protocolbuffers/protobuf/releases/download/v${PROTOBUF_VERSION}
# ARG PROTOBUF_DIR=protobuf-python-${PROTOBUF_VERSION}
# ARG PROTOC_DIR=protoc-${PROTOBUF_VERSION}-linux-aarch_64
# ENV PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=cpp

# RUN cd /tmp && \
#     wget --quiet --show-progress --progress=bar:force:noscroll --no-check-certificate ${PROTOBUF_URL}/$PROTOBUF_DIR.zip && \
#     wget --quiet --show-progress --progress=bar:force:noscroll --no-check-certificate ${PROTOBUF_URL}/$PROTOC_DIR.zip && \
#     unzip ${PROTOBUF_DIR}.zip -d ${PROTOBUF_DIR} && \
#     unzip ${PROTOC_DIR}.zip -d ${PROTOC_DIR} && \
#     cp ${PROTOC_DIR}/bin/protoc /usr/local/bin/protoc && \
#     cd ${PROTOBUF_DIR}/protobuf-${PROTOBUF_VERSION} && \
#     ./autogen.sh && \
#     ./configure --prefix=/usr/local && \
#     make -j$(nproc) && \
#     make check -j4 && \
#     make install && \
#     ldconfig && \
#     cd python && \
#     python3 setup.py build --cpp_implementation && \
#     python3 setup.py test --cpp_implementation && \
#     python3 setup.py bdist_wheel --cpp_implementation && \
#     cp dist/*.whl /opt && \
#     pip3 install dist/*.whl && \
#     cd ../../../ && \
#     rm ${PROTOBUF_DIR}.zip && \
#     rm ${PROTOC_DIR}.zip && \
#     rm -rf ${PROTOBUF_DIR} && \
#     rm -rf ${PROTOC_DIR}

# RUN pip3 show protobuf && \
#     protoc --version

# RUN pip3 install --no-cache-dir --verbose numpy==1.19.4
# RUN H5PY_SETUP_REQUIRES=0 pip3 install --no-cache-dir --verbose h5py==3.1.0
# RUN pip3 install --no-cache-dir --verbose future==0.18.2 mock==3.0.5 keras_preprocessing==1.1.2 keras_applications==1.0.8 gast==0.4.0 futures pybind11
# RUN pip3 install -U numpy grpcio absl-py py-cpuinfo psutil portpicker six mock requests gast h5py astor termcolor protobuf keras-applications keras-preprocessing wrapt google-pasta setuptools testresources

# ARG TENSORFLOW_URL=https://developer.download.nvidia.com/compute/redist/jp/v502/tensorflow/tensorflow-2.9.1+nv22.09-cp38-cp38-linux_aarch64.whl
# ARG TENSORFLOW_WHL=tensorflow-2.9.1+nv22.09-cp38-cp38-linux_aarch64.whl
# RUN wget --quiet --show-progress --progress=bar:force:noscroll --no-check-certificate ${TENSORFLOW_URL} -O ${TENSORFLOW_WHL} && \
#     pip3 install --no-cache-dir --verbose ${TENSORFLOW_WHL} && \
#     rm ${TENSORFLOW_WHL}

# ##### OpenCV with CUDA
# ARG OPENCV_URL=https://nvidia.box.com/shared/static/5v89u6g5rb62fpz4lh0rz531ajo2t5ef.gz
# ARG OPENCV_DEB=OpenCV-4.5.0-aarch64.tar.gz

# COPY jetson-containers/scripts/opencv_install.sh /tmp/opencv_install.sh
# RUN cd /tmp && ./opencv_install.sh ${OPENCV_URL} ${OPENCV_DEB}


# ##### PyCUDA
# ENV PATH="/usr/local/cuda/bin:${PATH}"
# ENV LD_LIBRARY_PATH="/usr/local/cuda/lib64:${LD_LIBRARY_PATH}"
# RUN echo "$PATH" && echo "$LD_LIBRARY_PATH"

# RUN pip3 install --no-cache-dir --verbose pycuda six

# ###### open_cv
# #ARG OPENCV_VERSION="4.6.0"
# #
# #COPY jetson-containers/scripts/opencv_install_deps.sh opencv_install_deps.sh
# #RUN ./opencv_install_deps.sh
# #RUN ln -s /usr/include/$(uname -i)-linux-gnu/cudnn_version_v8.h /usr/include/$(uname -i)-linux-gnu/cudnn_version.h
# #
# #ARG CUDA_ARCH_BIN=""
# #ARG ENABLE_NEON="OFF"
# #
# #RUN git clone --depth 1 --branch ${OPENCV_VERSION} https://github.com/opencv/opencv.git && \
# #    git clone --depth 1 --branch ${OPENCV_VERSION} https://github.com/opencv/opencv_contrib.git && \
# #    cd opencv && \
# #    mkdir build && \
# #    cd build && \
# #    echo "configuring OpenCV ${OPENCV_VERSION}, CUDA_ARCH_BIN=${CUDA_ARCH_BIN}, ENABLE_NEON=${ENABLE_NEON}" && \
# #    cmake \
# #        -D CPACK_BINARY_DEB=ON \
# #	   -D BUILD_EXAMPLES=OFF \
# #        -D BUILD_opencv_python2=OFF \
# #        -D BUILD_opencv_python3=ON \
# #	   -D BUILD_opencv_java=OFF \
# #        -D CMAKE_BUILD_TYPE=RELEASE \
# #        -D CMAKE_INSTALL_PREFIX=/usr/local \
# #        -D CUDA_ARCH_BIN=${CUDA_ARCH_BIN} \
# #        -D CUDA_ARCH_PTX= \
# #        -D CUDA_FAST_MATH=ON \
# #        -D CUDNN_INCLUDE_DIR=/usr/include/$(uname -i)-linux-gnu \
# #        -D EIGEN_INCLUDE_PATH=/usr/include/eigen3 \
# #	   -D WITH_EIGEN=ON \
# #        -D ENABLE_NEON=${ENABLE_NEON} \
# #        -D OPENCV_DNN_CUDA=ON \
# #        -D OPENCV_ENABLE_NONFREE=ON \
# #        -D OPENCV_EXTRA_MODULES_PATH=/opt/opencv_contrib/modules \
# #        -D OPENCV_GENERATE_PKGCONFIG=ON \
# #        -D WITH_CUBLAS=ON \
# #        -D WITH_CUDA=ON \
# #        -D WITH_CUDNN=ON \
# #        -D WITH_GSTREAMER=ON \
# #        -D WITH_LIBV4L=ON \
# #        -D WITH_OPENGL=ON \
# #	   -D WITH_OPENCL=OFF \
# #	   -D WITH_IPP=OFF \
# #        -D WITH_TBB=ON \
# #	   -D BUILD_TIFF=ON \
# #	   -D BUILD_PERF_TESTS=OFF \
# #	   -D BUILD_TESTS=OFF \
# #	   ../
# #	   
# #RUN cd opencv/build && make -j$(nproc)
# #RUN cd opencv/build && make install
# #RUN cd opencv/build && make package
# #RUN cd opencv/build && tar -czvf OpenCV-${OPENCV_VERSION}-$(uname -i).tar.gz *.deb

ARG BASE_IMAGE=nvcr.io/nvidia/l4t-base:r35.1.0
ARG ROS2_IMAGE=dustynv/ros:foxy-ros-base-l4t-r35.1.0
#ARG ROS2_IMAGE=dustynv/rosfoxy-desktop-l4t-r35.1.0
ARG PYTORCH_IMAGE=nvcr.io/nvidia/l4t-pytorch:r35.1.0-pth1.11-py3
ARG TENSORFLOW_IMAGE=nvcr.io/nvidia/l4t-tensorflow:r35.1.0-tf2.9-py3
ARG JETPACK_IMAGE=nvcr.io/nvidia/l4t-jetpack:r35.1.0
ARG PYTHON3_VERSION=3.8

FROM ${PYTORCH_IMAGE} as pytorch
FROM ${TENSORFLOW_IMAGE} as tensorflow
FROM ${JETPACK_IMAGE} as jetpack
FROM ${ROS2_IMAGE} as ros2
FROM ${BASE_IMAGE}

ENV DEBIAN_FRONTEND=noninteractive
ENV CUDA_HOME="/usr/local/cuda"
ENV PATH="/usr/local/cuda/bin:${PATH}"
ENV LD_LIBRARY_PATH="/usr/local/cuda/lib64:${LD_LIBRARY_PATH}"
ENV LLVM_CONFIG="/usr/bin/llvm-config-9"
RUN printenv
ENV ROS_DISTRO=foxy
ENV ROS_ROOT=/opt/ros/${ROS_DISTRO}
ENV ROS_PYTHON_VERSION=3

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
          python3-pip \
		python3-dev \
		python3-matplotlib \
		build-essential \
		gfortran \
		git \
		cmake \
		curl \
		libopenblas-dev \
		liblapack-dev \
		libblas-dev \
		libhdf5-serial-dev \
		hdf5-tools \
		libhdf5-dev \
		zlib1g-dev \
		zip \
		libjpeg8-dev \
		libopenmpi3 \
		openmpi-bin \
		openmpi-common \
		protobuf-compiler \
		libprotoc-dev \
		llvm-9 \
		llvm-9-dev \
		libffi-dev \
		libsndfile1 \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# protobuf from TF containers
ENV PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=cpp

COPY --from=tensorflow /usr/local/bin/protoc /usr/local/bin
COPY --from=tensorflow /usr/local/lib/libproto* /usr/local/lib/
COPY --from=tensorflow /usr/local/include/google /usr/local/include/google


# python packages from TF/PyTorch/ROS2 containers
COPY --from=pytorch /usr/local/lib/python2.7/dist-packages/ /usr/local/lib/python2.7/dist-packages/
COPY --from=pytorch /usr/local/lib/python3.8/dist-packages/ /usr/local/lib/python3.8/dist-packages/

COPY --from=tensorflow /usr/local/lib/python2.7/dist-packages/ /usr/local/lib/python2.7/dist-packages/
COPY --from=tensorflow /usr/local/lib/python3.8/dist-packages/ /usr/local/lib/python3.8/dist-packages/

# COPY --from=ros2 /opt/ros/${ROS_DISTRO} /opt/ros/${ROS_DISTRO}

# # CUDA and Cudnn and TnensorRT from jetpack
RUN apt-get update && apt-get install -y --no-install-recommends \
    sudo \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Install nvidia-cuda-dev for CUDA developer packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    nvidia-cuda-dev \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Install nvidia-cudnn8-dev for CuDNN developer packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    nvidia-cudnn8-dev \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Install nvidia-tensorrt-dev for TensorRT developer packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    nvidia-tensorrt-dev \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

#
# Install nvidia-vpi-dev for VPI developer packages
# Use nvidia-vpi if need VPI runtime only
#
RUN apt-get update && apt-get install -y --no-install-recommends \
    nvidia-vpi-dev \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean


# Install nvidia-opencv-dev for OpenCV developer packages
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     nvidia-opencv-dev \
#     && rm -rf /var/lib/apt/lists/* \
#     && apt-get clean


# Install Multimedia API samples & libs
RUN apt-get update && apt-get download nvidia-l4t-jetson-multimedia-api \
    && dpkg-deb -R ./nvidia-l4t-jetson-multimedia-api_*_arm64.deb ./mm-api \
    && cp -r ./mm-api/usr/src/jetson_multimedia_api /usr/src/jetson_multimedia_api \
    && ./mm-api/DEBIAN/postinst \
    && rm -rf ./nvidia-l4t-jetson-multimedia-api_*_arm64.deb ./mm-api

#Update libraries
RUN ldconfig 

# Setup environment variables
ENV CUDA_HOME="/usr/local/cuda"
ENV PATH="/usr/local/cuda/bin:${PATH}"
ENV LD_LIBRARY_PATH="/usr/local/cuda/lib64:${LD_LIBRARY_PATH}"

# COPY --from=jetpack /usr/local/cuda/ usr/local/cuda/
# COPY --from=jetpack /usr/local/cuda-11/ usr/local/cuda-11/
# COPY --from=jetpack /usr/local/cuda-11.4/ usr/local/cuda-11.4/

# COPY --from=jetpack /usr/src/tensorrt/ /usr/src/tensorrt/
# COPY --from=jetpack /usr/src/cudnn_samples_v8/ /usr/src/cudnn_samples_v8/
# COPY --from=jetpack /usr/src/jetson_multimedia_api/ /usr/src/jetson_multimedia_api/

# python pip packages
RUN pip3 install --no-cache-dir --ignore-installed pybind11 
RUN pip3 install --no-cache-dir --verbose onnx
RUN pip3 install --no-cache-dir --verbose scipy
RUN pip3 install --no-cache-dir --verbose scikit-learn
RUN pip3 install --no-cache-dir --verbose pandas
RUN pip3 install --no-cache-dir --verbose pycuda
RUN pip3 install --no-cache-dir --verbose numba


# #
# # CuPy
# #
# ARG CUPY_VERSION=v10.2.0
# ARG CUPY_NVCC_GENERATE_CODE="arch=compute_53,code=sm_53;arch=compute_62,code=sm_62;arch=compute_72,code=sm_72;arch=compute_87,code=sm_87"

# RUN git clone -b ${CUPY_VERSION} --recursive https://github.com/cupy/cupy cupy && \
#     cd cupy && \
#     pip3 install --no-cache-dir fastrlock && \
#     python3 setup.py install --verbose && \
#     cd ../ && \
#     rm -rf cupy


# #
# # PyCUDA
# #
# RUN pip3 uninstall -y pycuda
# RUN pip3 install --no-cache-dir --verbose pycuda six


# # 
# # install OpenCV (with CUDA)
# #
# ARG OPENCV_URL=https://nvidia.box.com/shared/static/5v89u6g5rb62fpz4lh0rz531ajo2t5ef.gz
# ARG OPENCV_DEB=OpenCV-4.5.0-aarch64.tar.gz

# COPY scripts/opencv_install.sh /tmp/opencv_install.sh
# RUN cd /tmp && ./opencv_install.sh ${OPENCV_URL} ${OPENCV_DEB}


# #
# # JupyterLab
# #
# RUN pip3 install --no-cache-dir --verbose jupyter jupyterlab && \
#     pip3 install --no-cache-dir --verbose jupyterlab_widgets
    
# RUN jupyter lab --generate-config
# RUN python3 -c "from notebook.auth.security import set_password; set_password('nvidia', '/root/.jupyter/jupyter_notebook_config.json')"

# CMD /bin/bash -c "jupyter lab --ip 0.0.0.0 --port 8888 --allow-root &> /var/log/jupyter.log" & \
# 	echo "allow 10 sec for JupyterLab to start @ http://$(hostname -I | cut -d' ' -f1):8888 (password nvidia)" && \
# 	echo "JupterLab logging location:  /var/log/jupyter.log  (inside the container)" && \
# 	/bin/bash

##### ROS-desktop install
RUN apt update && sudo apt install locales && \
	locale-gen en_US en_US.UTF-8 && \
	update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8 && \
	export LANG=en_US.UTF-8 && \
	locale && \
	apt-cache policy | grep universe

RUN apt install software-properties-common -y && \
	add-apt-repository universe

RUN apt update && sudo apt install curl gnupg2 lsb-release
RUN	curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key  -o /usr/share/keyrings/ros-archive-keyring.gpg
RUN mv /bin/sh /bin/sh_tmp && ln -s /bin/bash /bin/sh
RUN	echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(source /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
RUN rm /bin/sh && mv /bin/sh_tmp /bin/sh

RUN apt update && \
 	apt upgrade -y

RUN	apt install ros-foxy-desktop -y

RUN /bin/bash -c "source /opt/ros/foxy/setup.bash"
RUN echo 'source /opt/ros/foxy/setup.bash' >> /root/.bashrc

RUN apt install ros-foxy-turtlesim -y
RUN apt-get update
RUN apt-get install -qqy x11-apps

#### install ros-realsense
# WORKDIR /usr/app/src

# RUN apt-get update -y
# RUN apt-get upgrade -y
# RUN apt autoremove -y
# RUN apt-get dist-upgrade -y
# RUN apt install git -y
# RUN apt-get install git libssl-dev libusb-1.0-0-dev libudev-dev pkg-config libgtk-3-dev -y
# RUN apt-get install libglfw3-dev libgl1-mesa-dev libglu1-mesa-dev at -y
# RUN apt -y install udev

# RUN git clone https://github.com/IntelRealSense/librealsense.git

# WORKDIR /usr/app/src/librealsense

# RUN ./scripts/setup_udev_rules.sh
# RUN ./scripts/patch-realsense-ubuntu-lts.sh; exit 0
# RUN mkdir build
# WORKDIR /usr/app/src/librealsense/build
# RUN cmake ../ -DBUILD_EXAMPLES=true -DBUILD_GRAPHICAL_EXAMPLES=false
# RUN make uninstall && make clean && make -j8 && make install


# RUN mkdir -p /usr/app/src/ros2_ws/src
# WORKDIR /usr/app/src/ros2_ws/src/
# RUN git clone https://github.com/IntelRealSense/realsense-ros.git -b ros2-beta

# WORKDIR /usr/app/src/ros2_ws/

# RUN apt-get install python3-rosdep -y
# RUN rosdep init; exit 0
# RUN rosdep update

# RUN echo 'source /opt/ros/foxy/install/setup.bash' >> /root/.bashrc
# RUN /bin/bash -c "source /opt/ros/foxy/install/setup.bash"
# RUN rosdep install -i --from-path src --rosdistro $ROS_DISTRO --skip-keys=librealsense2 -y
# RUN mv /bin/sh /bin/sh_tmp && ln -s /bin/bash /bin/sh
# RUN source /opt/ros/${ROS_DISTRO}/install/setup.bash; colcon build
# RUN rm /bin/sh && mv /bin/sh_tmp /bin/sh

# RUN echo 'source /usr/app/src/ros2_ws/install/local_setup.bash' >> /root/.bashrc
# RUN /bin/bash -c "source /usr/app/src/ros2_ws/install/local_setup.bash"

# COPY test_tensorflow.py ./