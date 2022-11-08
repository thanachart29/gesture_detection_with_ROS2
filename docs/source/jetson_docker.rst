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