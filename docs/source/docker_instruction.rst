Using Docker Instruction
*************************

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
