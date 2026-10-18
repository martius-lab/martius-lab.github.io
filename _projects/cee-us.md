---
title: Curious Exploration via Structured World Models
subtitle: Zero-shot object manipulation (CEE-US)
area: intrinsically-motivated-learning
image: images/projects/cee-us/teaser.webp
description: Structured world models with relational inductive biases and information gain enable interaction-rich free play in multi-object environments and zero-shot solving of downstream tasks.
status: current
---

{% include figure.html image="images/projects/cee-us/fig1.webp" caption="Task-agnostic free-play for world-model learning. Planning to solve specific tasks zero-shot." %}

We propose to use structured world models to incorporate relational inductive biases and information gain to achieve interaction-rich exploration in compositional multi-object environments.

We consider predicted information gain as an internal drive to improve exploration efficiency and to learn capable world models. We find that structured world models allow for relational inductive biases that are suitable for tasks with many objects. Combined with our planning method, we obtain a task-agnostic free-play behavior that explores what can be done in the environment. Using the online-planning method, a robotic arm can then perform tasks such as block stacking without further training, so we achieved zero-shot task generalization.
