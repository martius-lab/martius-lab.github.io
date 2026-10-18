---
title: CombOptNet
area: combinatorial-optimization
image: images/projects/comboptnet/teaser.webp
description: An architecture with universal combinatorial expressivity that learns the underlying combinatorial problem by learning the full specification of an Integer Linear Program.
status: current
---

{% include figure.html image="images/projects/comboptnet/fig1.webp" %}

While this project is not directly using the blackbox differentiation framework, its spirit is closely linked to the idea of using combinatorial solvers in deep neural networks. This paper asks the question whether it is possible to design an architecture that is not tailored to one specific combinatorial problem as in the blackbox differentiation framework, but instead offers universal combinatorial expressivity.

We describe *CombOptNet*, which learns the underlying combinatorial problem that governs the training data, by learning the parameters of the full specification of a general Integer Linear Program. Specifically, we show that we can solve challenging tasks such as knapsack problems from natural language description, as well as visual combinatorial graph matching, without a priori specifying the underlying combinatorial problem.
