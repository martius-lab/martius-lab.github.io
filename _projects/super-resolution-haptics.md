---
title: Super-resolution Sensing for Haptics
area: haptic-sensing
image: images/projects/super-resolution-haptics/teaser.webp
description: A theory based on sensor isolines to characterize, analyze, and predict force sensation at super-resolution, guiding the design of tactile skins with only a few taxels.
status: current
---

{% include figure.html image="images/projects/super-resolution-haptics/fig1.webp" caption="We introduce a theory to characterize, analyze, and predict force sensation at super-resolution for haptic sensors. Our theory is based on sensor isolines that directly assess the uniqueness of contact position reconstruction. A sensor design guided by this theory achieves a super-resolution factor of over 1200." %}

**Introduction video:** [youtube.com/watch?v=KA2LMAUUba4](https://www.youtube.com/watch?v=KA2LMAUUba4)

Haptic feedback is essential to make robots more dexterous and effective in unstructured environments. Nevertheless, high-resolution tactile sensors are still not widely available. When using a large number of physical sensing units we often face manufacturing challenges and wiring problems. Such complex hardware can also lead to durability issues as each additional component constitutes a potential point of failure.

We pursue a route towards high-resolution and robust tactile skins by embedding only a few sensor units (taxels) into a flexible surface material and use signal processing to achieve sensing with super-resolution accuracy. We first rely on the empirical knowledge that overlapping multiple taxels' perception fields enables super-resolution behavior and design a sensing system for robotic applications. We then propose a theory for geometric super-resolution to guide the development of tactile sensors of this kind and link it to machine learning techniques for signal processing. This theory is based on sensor isolines and allows us to predict force sensitivity and accuracy in contact position and force magnitude as a spatial quantity. We evaluate the influence of different factors, such as elastic properties of the material, structure design, and transduction methods, using finite element simulations and implemented real sensors. Using machine learning methods to infer contact information, our sensors obtain an unparalleled average super-resolution factor of over 1000. Our theory can guide future haptic sensor designs and inform various design choices.
