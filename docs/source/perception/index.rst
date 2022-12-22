.. _perception:

Perception
#################

This subtopic includes overview, installation, use cases, API references, and subsystem verification of all perception technology the Cacao robot can perform right now. It breaks down into 4 sections as shown below.


+ :doc:`Object Perception <./docs/object_perception>`

The robot can perceive objects around the robot. For this use case, the team employs YOLOv5 model to detect a handbag when a person points the finger to the bag. 
 
+ :doc:`People Perception <./docs/people_perception>`

Using mediapipe and YOLOv5, the robot can detect people in the frame so it can follow people when doing tasks.

+ :doc:`Speech Perception <./docs/speech_perception>`

Utilizing Google speech recognition, the robot acknowledge basic commands and responds from human.

+ :doc:`Gesture Perception <./docs/gesture_perception>`

Using mediapipe, the robot can analyze human gestures and intentions. It uses this intent/entity analysis in the behavior tree to determine proper actions.

.. toctree::
   :maxdepth: 1
   :hidden:
   
   docs/object_perception.rst
   docs/people_perception.rst
   docs/speech_perception.rst
   docs/gesture_perception.rst
