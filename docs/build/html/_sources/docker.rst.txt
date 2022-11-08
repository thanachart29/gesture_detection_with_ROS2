Cacao Docker
==============

Cacao's Robot contains 2 processor unit that is Intel NUC and a Jetson Xavier NX developer kit. 
Two processors have different objectives first Jetson Xavier NX developer kit using for running the machine learning models 
and Intel NUC using for Navigation. 
Both processors do not have the same python environment, 
therefore, Cacao's team is building the docker images for executing software in the same environment as Cacao's processor

|

----------------------------

Jetson Xavier Docker Image
==========================

docker repository: https://hub.docker.com/repository/docker/thanachart29/jetson_athome

--------------------------

Jetson Xavier package 
""""""""""""""""""""""""
you can find all package at `<https://github.com/MBSE-2022-1/Software-Team/blob/docker/jetson_python_library.txt>`__ 

requirement package included:

#. System

    * OS: ubuntu focal fossa 20.04.5 LTS
    * Architecture: arm64/v8
    * CUDA: 11.4
    * Python 3.8.10
    * Default work directory : /usr/app/src/cacao_ws

#. Library

    * ROS2-foxy-desktop
    * PyTorch v1.11.0
    * torchvision v0.12.0
    * torchaudio v0.11.0
    * TensorFlow 2.9.1
    * Protobuf 3.19.4
    * Numpy 1.23.1
    * OpenCV 4.6.0.66
    * PyYAML 5.3.1
    * Pillow 9.2.0
    * Request 2.28.1
    * Tqdm 4.64.1
    * Tensorboard 2.9.1
    * Pandas 1.5.1
    * Mediapipe 0.8.11
    * SpeechRecognition 3.8.1
    * pocketsphinx 0.1.15
    * Pyaudio 0.2.11
    * Pyttsx3 0.29
    * Pybind11 2.10.0

.. _[1]:

[1] Enabling Jetson Containers on an x86 workstation (using qemu)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. code-block:: console

    $ sudo apt-get install qemu binfmt-support qemu-user-static
    # Check if the entries look good.
    $ sudo cat /proc/sys/fs/binfmt_misc/status
    >> enabled
    # See if /usr/bin/qemu-aarch64-static exists as one of the interpreters.
    $ cat /proc/sys/fs/binfmt_misc/qemu-aarch64
    >> enabled
    >> interpreter /usr/bin/qemu-aarch64-static
    >> flags: OCF
    >> offset 0
    >> magic 7f454c460201010000000000000000000200b700
    >> mask ffffffffffffff00fffffffffffffffffeffffff

Known limitation: Unfortunately you won’t be able to run any binary that calls into the NVIDIA driver on the x86 host.

|

-----------------------------

Inter NUC Docker Image
=======================

docker repository: https://hub.docker.com/repository/docker/thanachart29/nuc_athome

------------------------------

Inter NUC package
"""""""""""""""""""

you can find all package at `<https://github.com/MBSE-2022-1/Software-Team/blob/docker/nuc_python_library.txt>`__ 

requirement package included:

#. System

    * OS: ubuntu focal fossa 20.04.5 LTS
    * Architecture: x86_64
    * CUDA: 11.2
    * Python 3.8.10
    * Default work directory : /usr/app/src/cacao_ws

#. Library

    * ROS2-foxy-desktop
    * PyTorch v1.11.0
    * torchvision v0.12.0
    * torchaudio v0.11.0
    * TensorFlow 2.9.1
    * Protobuf 3.19.6
    * Numpy 1.23.1
    * OpenCV 4.6.0.66
    * PyYAML 5.3.1
    * Pillow 9.2.0
    * Request 2.28.1
    * Tqdm 4.64.1
    * Tensorboard 2.9.1
    * Pandas 1.5.1
    * Mediapipe 0.8.11
    * SpeechRecognition 3.8.1
    * pocketsphinx 0.1.15
    * Pyaudio 0.2.11
    * Pyttsx3 0.29
    * Pybind11 2.10.0

.. _[2]:

[2] Using Nvidia-container runtime (for using gpu on docker)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#. Setting up docker

    .. code-block:: console
        
        curl https://get.docker.com | sh \
            && sudo systemctl --now enable docker

#. Setting up NVIDIA Container Toolkit

    .. code-block:: console

        distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
            && curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
            && curl -s -L https://nvidia.github.io/libnvidia-container/$distribution/libnvidia-container.list | \
            sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
            sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list

#. Install the nvidia-docker2

    .. code-block:: console

        sudo apt-get update
        sudo apt-get install -y nvidia-docker2

#. Restart the Docker daemon after setting the default runtime:

    .. code-block:: console

        sudo systemctl restart docker

#. (optional) tested by running a base CUDA container

    .. code-block:: console

        sudo docker run --rm --gpus all nvidia/cuda:11.0.3-base-ubuntu20.04 nvidia-smi

|

---------------------------


Using Docker Instruction
========================

* first of all, install Docker following the `Docker install manuals <https://docs.docker.com/engine/install/ubuntu/>`_
* Pull docker images

    * Jetson Xavier Images 

        .. code-block:: console

            docker pull thanachart29/jetson_athome:latest
    
    * Intel NUC Images

        .. code-block:: console

            docker pull thanachart29/nuc_athome:latest

* Run a command in a new containers

    .. code-block:: console

        docker run [OPTIONS] IMAGE [COMMAND] [ARG...]

    * Enable display from host: [OPTIONS] = --privileged --env DISPLAY=unix$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix
    * Enable GPU from host: [OPTIONS] = --gpus all
    * Enable audio from host: [OPTIONS] = --group-add audio

    For example
    
        .. code-block:: console

            docker run --rm -it --privileged 
                                --env DISPLAY=unix$DISPLAY  
                                -v /tmp/.X11-unix:/tmp/.X11-unix 
                                –gpus all –group-add audio <image name>

* Run with bash command

    .. code-block:: console

        docker run --rm -it <image name>

    .. note::
        using --rm option for remove the container when it exits

* Execute scripts from local hosts to run inside container

    .. code-block:: console

        docker run -i <image name> <python3, e.g.> < <path to scripts>

    OR

    .. code-block:: console

        docker run -itd <image name>
        docker exec -i <container ID> <python3, e.g.> <  <path to scripts>
    
* Basically, run ros package in docker

    .. code-block:: console

        docker run -itd <image name>
        docker cp <host file/directory> <container ID>:<container directory>
        docker exec -itd <container ID> /bin/bash

    .. note::
        This command will copy your directory to container and you can use terminal as superuser

|

--------------

Reference
==========

`[1]`_ : https://github.com/NVIDIA/nvidia-docker/wiki/NVIDIA-Container-Runtime-on-Jetson

`[2]`_ : https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html