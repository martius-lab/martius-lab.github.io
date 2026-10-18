---
title: Optimizing Rank-based Metrics
subtitle: RaMBO -- Rank Metric Blackbox Optimization
area: combinatorial-optimization
image: images/projects/rank-based-metrics/teaser.webp
description: Applying blackbox differentiation to the argsort operation makes it possible to directly optimize recall and Average Precision for retrieval and detection tasks.
status: current
---

{% include figure.html image="images/projects/rank-based-metrics/fig1.webp" %}

In search for practical application of the blackbox-differentiation theory, we turn to computer vision. Concretely, we show that applying blackbox-backprop to computer vision benchmarks in recall and Average Precision for retrieval and detection tasks consistently improves the underlying architectures' performance.

The main component that enables this is the blackbox formulation of the argsort operation used for ranking, making the use of blackbox-differentiation theory possible. We made a [blog post](https://towardsdatascience.com/rambo-ranking-metric-blackbox-optimization-36811a5f52dd) describing the method, which we call RaMBO (Rank Metric Blackbox Optimization). Further information about the paper (including a short and long oral presented at CVPR 2020) can be found [here](https://al.is.mpg.de/publications/optimizing-rank-based-metrics-with-blackbox-differentiation).
