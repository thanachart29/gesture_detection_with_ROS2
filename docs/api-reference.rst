API Reference for CATOCT
========

Initializing parameters
--------

In case you want to generate your own trajectory, you can try assigning your via points, velocity limits, and acceleration limits. Note that the initial position is defined separately from the via points. This represents the current joint state of the robotics manipulator.::

   from trajectory import Trajectory
   import numpy as np
 
   n = 3
   N = 10
   q_0 = np.random.rand(n,1)
   q = np.random.rand(n,N)
   v_max = [1]*n
   a_max = [0.1]*n

Constructing a "Trajectory" object
--------

CATOCT provides a class definition called "Trajectory", which holds several functionalities related to trajectory generation. Constructing a "Trajectory" requires  via_points as well as velocity and acceleration limits.::

   traj = Trajectory()
   traj.set_position(q)
   traj.set_bound(v_max,a_max)
   
Optimizing a trajectory
--------

Once you have constructed a trajectory that, you can run optimization by calling "time_optimal" on the initial guessed position.::

   traj.time_optimal(q_0)
   
"time_optimal" will attempt to solve optimization. Due to the uniqueness of the problem, it will always return optimization result. 

Evaluating a trajectory at a point
--------

CATOCT also provides a method called "evaluate" to evaluate the optimized trajectroy based on any time vector. We can generate a time vector using numpy's linspace and visualize the evaluated trajectory using matplotlib.::

   t = np.linspace(0,np.sum(traj.duration),1000)
   q_t,v_t,a_t = traj.evaluate(t)

   import matplotlib.pyplot as plt

   # visualization
   fig,axs = plt.subplots(3)
   axs[0].plot(t,q_t)
   axs[0].plot(np.cumsum(traj.duration),traj.position,'r*',linewidth=1,markersize=10)
   axs[1].plot(t,v_t)
   axs[1].plot(np.cumsum(traj.duration),traj.velocity,'r*',linewidth=1,markersize=10)
   axs[2].plot(t,a_t)
   axs[2].plot(np.cumsum(traj.duration),traj.acceleration,'r*',linewidth=1,markersize=10)
   plt.show()


.. image:: pic/example.png
  :width: 1000
  :alt: Alternative text
