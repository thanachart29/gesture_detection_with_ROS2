#### can change to ros desktop
ARG ROS_BASE_IMAGE=dustynv/ros:foxy-ros-base-l4t-r35.1.0
FROM ${ROS_BASE_IMAGE}

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
            python3-pip \
		  python3-dev \
		  libopenblas-dev \
		  libopenmpi-dev \
            openmpi-bin \
            openmpi-common \
		  gfortran \
		  libomp-dev \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

RUN pip3 install --no-cache-dir setuptools Cython wheel
RUN pip3 install --no-cache-dir --verbose numpy


##### pytorch
ARG PYTORCH_URL=https://nvidia.box.com/shared/static/ssf2v7pf5i245fk4i0q926hy4imzs2ph.whl
ARG PYTORCH_WHL=torch-1.11.0-cp38-cp38-linux_aarch64.whl
RUN wget --quiet --show-progress --progress=bar:force:noscroll --no-check-certificate ${PYTORCH_URL} -O ${PYTORCH_WHL} && \
    pip3 install --no-cache-dir --verbose ${PYTORCH_WHL} && \
    rm ${PYTORCH_WHL}

##### torch vision
# default torchvision v0.12.0
ARG TORCHVISION_VERSION=v0.12.0
ARG TORCH_CUDA_ARCH_LIST="11.2"
RUN printenv && echo "torchvision version = $TORCHVISION_VERSION" && echo "TORCH_CUDA_ARCH_LIST = $TORCH_CUDA_ARCH_LIST"
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
		  git \
		  build-essential \
            libjpeg-dev \
		  zlib1g-dev \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean


RUN git clone https://github.com/pytorch/vision torchvision && \
    cd torchvision && \
    git checkout ${TORCHVISION_VERSION} && \
    python3 setup.py install && \
    cd ../ && \
    rm -rf torchvision

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
		  software-properties-common \
		  apt-transport-https \
		  ca-certificates \
		  gnupg \
		  lsb-release \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean



