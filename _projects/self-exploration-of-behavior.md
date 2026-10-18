---
title: Self-exploration of Behavior
area: previous
image: images/projects/self-exploration-of-behavior/teaser.webp
description: How robots can generate structured behavior without any reward or objective, using differential extrinsic plasticity (DEP) to explore and learn a repertoire of behavioral primitives.
status: previous
---

{% include figure.html image="images/projects/self-exploration-of-behavior/fig1.webp" caption="Hexapod simulated robot with 18 DoF (a). Thanks to the DEP-controller with repelling potential the robot is able to discover 48 attractor behaviors displayed in the space of velocities (b). The behaviors can later be replayed (c). The SUBMODES system can extract models of behavioral primitives B(t) from such self-explored behavior using unexpected increases in prediction error e(t) (d)." %}

Humans and other animals need to learn behavior from exploring their sensorimotor capabilities. In this project we aim to understand how robotic systems can generate structured behavior, without specifying any reward nor objective function. Instead, the systems should explore behavior purely based on their embodiment and their interactions with the environment.

One way to bootstrap a goal-free explorative process is to use differential extrinsic plasticity (DEP). DEP is a biologically plausible synaptic mechanism that can be used within very simple neural network controllers. When applying the DEP-controller to embodied agents, highly coordinated, rhythmic behaviors can emerge. These behaviors correspond to attractors of a dynamical system. When combining DEP with a "repelling potential" an agent can actively explore all its attractor behaviors in a systematic way. As a result, highly complex robotic systems, e.g., a Hexapod robot (Fig. a), discover a variety of meaningful behaviors (Fig. b), such as various modes of locomotion.

{% include figure.html image="images/projects/self-exploration-of-behavior/dep.webp" caption="Differential extrinsic plasticity (DEP) in a neural network controller and emerging behaviors of simulated robots." width="600px" %}

Such self-organizing behavior can be used to discover and learn a repertoire of behavioral primitives from scratch. Our SUBMODES system explores behavior using the DEP-controller. During exploration, internal models are trained to predict the motor commands and the resulting sensory consequences of the performed behavior. The SUBMODES system uses an unexpected increase in prediction error to detect transitions between behaviors and switch between internal models (Fig. d). In this way, the system is able to systematically structure its sensorimotor experience on-line into compositional models of behavior that can later be used for planning and control.
