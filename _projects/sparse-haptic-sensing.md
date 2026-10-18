---
title: Robust and Affordable Haptic Sensation with Sparse Sensor Configuration
area: previous
image: images/projects/sparse-haptic-sensing/teaser.webp
description: A low-cost, robust method for inferring haptic forces on the surface of 3D robot limbs from a few internal strain sensors, using machine learning and optimized sensor placement.
status: previous
---

{% include figure.html image="images/projects/sparse-haptic-sensing/fig1.webp" %}

During the rapid development of robot technologies, actuators and sensors have become increasingly compact and powerful. Nevertheless, robots are still far from matching human capabilities especially when it comes to touch sensation. For this, haptic sensors have to be robust to sustain long-lasting experiments. Besides robustness, another important aspect of robotic hardware is its price, availability, and performance. A low cost makes robotic technologies widely accessible and thus facilitates research.

In this project, we aim at providing a low-cost, robust and sufficiently precise method for inferring haptic forces on the surface of 3D robot limbs. Instead of applying dense array-shaped sensors, we opt for a small number of sensors measuring internal deformation. This offers a couple of conceptual advantages:

1. The system is robust to environmental impacts because sensors are placed internally;
2. The surface shape can be freely designed;
3. Only a few channels have to be read out which reduces both the energy consumption and the data rate.

On the downside, a measurement of the sensors does not directly correspond to the impacting force. Instead, an inference mechanism is required to estimate the force. We propose a data-driven approach using machine learning algorithms to perform this inference efficiently. To require as few sensors as possible, we employ several optimization schemes to determine optimal sensor placement.

The contributions of this project are as follows: On the theory side, we propose a new way of implementing a whole surface haptic sensor and provide a method for determining the optimal number and position of sensors using finite element method. On the application side, we provide a method to assemble the strain gauges, designed a hardware system to systematically collect data and demonstrated the sensing system on a robotic limb.
