---
title: Learning Agile Skills via Adversarial Imitation of Rough Partial Demonstrations
area: rl-diverse-solutions
image: images/projects/agile-skills-wasabi/teaser.webp
description: A generative adversarial method infers reward functions from rough, partial demonstrations; with sim2real transfer, the quadruped Solo 8 learns robust agile skills such as a backflip.
status: current
---

{% include figure.html image="images/projects/agile-skills-wasabi/fig1.webp" caption="The Solo 8 robot performing a backflip." width="600px" %}

Mastering agility: We use a generative adversarial method for inferring reward functions from partial demonstrations. Using sim2real transfer we get robust skills enabling, for instance, the impressive backflip of our quadruped Solo 8.

Imitation learning from state-only demonstrations is a promising approach to capture preferences and to easily specify tasks. We study how to obtain agile behavior from only partial demonstrations and develop a Wasserstein discrimination method to compute the reward. This paper was one of the three best paper finalists at CoRL 2022.
