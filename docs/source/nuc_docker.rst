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