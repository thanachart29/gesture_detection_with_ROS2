.. _manipulation:

Manipulation
#################

.. raw:: html

    <h1 align="center">
      <div>
        <div style="position: relative; padding-bottom: 0%; overflow: hidden; max-width: 100%; height: auto;">
          <iframe width="560" height="315" src="https://www.youtube.com/embed/0JdI6uxSKN8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </div>
      </div>
    </h1>



Overview
**********

The manipulation node is used to control the UR3e robotics arm to carry the luggage by moving to pose that the Object detection node has sent and putting the luggage down when the CACAO robot reaches to destination. In the video, we are showing how UR3e robot moves to goal pose and grabs the luggage.

 .. figure:: ./docs/images/Manipulator_Architecture.jpg
     :width: 480
     :align: center
     :alt: Manipulator Architecture
     
     Figure 1: Manipulator Architecture

Manipulation Concepts
""""""""""""""""""""""

In the Manipulator node, we have two ability behavior.

1. Grab Object: is ability behavior for grab object of manipulator

   Workflow of Grab Object behavior

   - Receive pose

      Receive goal position in XYZ axis from Object Detection node. In this version of the manipulation node, we fixed the orientation of UR3e for grabbing the luggage only. 

      The frame of camera and UR3e is:

      .. figure:: ./docs/images/The_frame_of_camera_and_UR3e.jpg
          :width: 480
          :align: center
          :alt: The frame of camera and UR3e

          Figure 2: The frame of camera and UR3e


   - Enable service

      Waiting for Software Integration call service /enable_mani_grab to start grab object ability behavior.

   - Check limit workspace

      Checking position from Object Detection is over the workspace of UR3e and check position is damaged to the CACAO robot. Suppose the position from Object Detection is over workspace or can collide CACAO robot. In that case, Manipulator node will call function ‘Pose to Navigation’ for requiring Navigation node to navigate CACAO robot to position that manipulator can garb object in workspace. 

   - Set TCP pose

      Set the end effector offset and end effector frame of UR3e using the function from ur_rtde. 

   - Move to goal pose

      If manipulation can control in workspace, the node will send scripts to control the UR3e pose using ur_rtde. In this version, we use only moveJ (joint space path) to control UR3e for avoiding singularity and make UR3e have more workspace for move.

   - Pose to Navigation

      If position is over workspace, the node will calculate position and send it to Navigation node for required Navigation node to navigate the robot to position that manipulator can grab an object in workspace.

   - Gripper Control

      Control gripper using UR-scripts. After gripper grab, object manipulation will move while holding the object to home pose and send ‘success’ status to System Integration.


2. Release Object: is ability behavior for release object of manipulator

   Workflow of Release Object behavior

   - Enable Service
   - Move to goal pose
   - Gripper Control

Installation
*************

1. Set up UR3e
2. Set up IP address
3. Set up your computer
4. 

Example
*********


API Reference
***************


Problem and future plan
*************************
