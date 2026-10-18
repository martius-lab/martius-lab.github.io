---
title: Risk-Averse Planning
subtitle: Risk-Averse Zero-Order Trajectory Optimization
area: model-based-rl
image: images/projects/risk-averse-planning/teaser.webp
description: Managing risk in zero-order trajectory optimization by separating epistemic and aleatoric uncertainty of an ensemble of stochastic neural networks.
status: current
---

{% include figure.html image="images/projects/risk-averse-planning/fig1.webp" %}

We introduce a simple but effective method for managing risk in zero-order trajectory optimization that involves probabilistic safety constraints and balancing of optimism in the face of epistemic uncertainty and pessimism in the face of aleatoric uncertainty of an ensemble of stochastic neural networks. Various experiments indicate that the separation of uncertainties is essential to performing well with data-driven MPC approaches in uncertain and safety-critical control environments.
