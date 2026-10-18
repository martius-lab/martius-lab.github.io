---
title: Deep Graph Matching
area: combinatorial-optimization
image: images/projects/deep-graph-matching/teaser.webp
description: An end-to-end trainable keypoint matching architecture that embeds a state-of-the-art graph matching solver via blackbox differentiation.
status: current
---

{% include figure.html image="images/projects/deep-graph-matching/fig1.webp" %}

Staying in the research area of computer vision, we tackle the problem of keypoint matching. Leveraging our blackbox-backprop framework, we carefully extract keypoint descriptors using visual and geometrical information and use a [state-of-the-art solver](https://github.com/LPMP/LPMP) to solve a bipartite graph matching problem. The resulting end-to-end trainable architecture set the state-of-the-art on challenging keypoint matching benchmarks when it was published at ECCV 2020.
