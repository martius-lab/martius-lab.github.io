---
title: Regularity as Intrinsic Reward for Free Play
subtitle: RaIR
area: intrinsically-motivated-learning
image: images/projects/regularity-free-play/teaser.webp
description: Inspired by child development, Regularity as Intrinsic Reward (RaIR) guides exploration in model-based RL towards regular structures, boosting zero-shot performance on assembly tasks.
status: current
---

{% include figure.html image="images/projects/regularity-free-play/fig1.webp" caption="Illustration of our measure of regularity. Top: a world with movable points. Bottom: A robot arm with 6 objects." %}

We propose Regularity as Intrinsic Reward (RaIR) for model-based reinforcement learning, inspired by child development, to guide exploration towards regular situations otherwise not easily discovered.

Inspired by child development, we postulate that the search for structure partially guides exploration. RaIR is a measure of regularity of a scene and is computed using Shannon Entropy of a suitable scene representation.

By combining RaIR with epistemic uncertainty, our approach enables autonomous construction of regular structures during free play, significantly boosting zero-shot performance on assembly tasks.
