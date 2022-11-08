CATOCT
========

CATOCT is a toolbox for generating a continuous-acceleration time-optimal cubic trajectory.
Given a sequence of (multiple-degree-of-freedom) via points in joint space and limits on the magnitude of both velocity and acceleration of each degree of freedom, 
the goal is to generate a piece-wise cubic trajectory that is time-optimal and satisfies both velocity and acceleration constraints. The trajectory must be 
continuous in position, velocity, and acceleration.

.. image:: pic/example.png
  :width: 1000
  :alt: Alternative text
.. toctree::
   :maxdepth: 1
   :caption: Getting Started

   rationale.rst
   installation.rst
   docker.rst
   Examples <https://github.com/tchoopojcharoen/catoct/tree/main/examples>
   CONTRIBUTING.md
