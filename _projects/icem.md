---
title: iCEM
subtitle: Sample-efficient Cross-Entropy Method for Real-time Planning
area: model-based-rl
image: images/projects/icem/teaser.webp
description: An improved Cross-Entropy Method for fast planning with temporally-correlated actions and memory, requiring 2.7-22x fewer samples in high-dimensional control problems.
status: current
---

{% include figure.html image="images/projects/icem/fig1.webp" %}

Trajectory optimizers for model-based reinforcement learning, such as the Cross-Entropy Method (CEM), can yield compelling results even in high-dimensional control tasks and sparse-reward environments. However, their sampling inefficiency prevents them from being used for real-time planning and control. We propose an improved version of the CEM algorithm for fast planning, with novel additions including temporally-correlated actions and memory, requiring 2.7-22x less samples and yielding a performance increase of 1.2-10x in high-dimensional control problems.
