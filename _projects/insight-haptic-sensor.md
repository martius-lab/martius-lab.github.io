---
title: "Insight: a Haptic Sensor Powered by Vision and Machine Learning"
area: haptic-sensing
image: images/projects/insight-haptic-sensor/teaser.webp
description: A robust, soft, low-cost, vision-based, thumb-sized 3D haptic sensor that continually supplies the robot with a directional force-distribution map over its entire conical sensing surface.
status: current
---

{% include figure.html image="images/projects/insight-haptic-sensor/fig1.webp" caption="We introduce a new soft haptic sensor that uses vision and learning to accurately estimate where and how it is being contacted. The sensor constantly records images from the inside using a camera. Feeding these images and a reference image into a trained deep neural network makes it possible to estimate the directional force distribution all over the sensing surface." %}

**Introduction video:** [youtube.com/watch?v=lTAJwcZopAA](https://www.youtube.com/watch?v=lTAJwcZopAA)

Robots need detailed haptic sensing that covers their complex surfaces to learn effective behaviors in unstructured environments. However, state-of-the-art sensors tend to focus on improving precision and sensitivity, increasing taxel density, or enlarging the sensed area rather than prioritizing system robustness and the usability of the sensed haptic information. By considering the goals and constraints from a fresh perspective, we have designed **a robust, soft, low-cost, vision-based, thumb-sized 3D haptic sensor** named ***Insight***; it continually supplies the host robot with a **directional force-distribution map** over its entire conical sensing surface.

Insight uses an internal monocular camera, photometric stereo, and structured light to detect the 3D deformation of the easily replaceable flexible outer shell, which is molded in a single layer over a stiff frame to guarantee sensitivity, robustness, and a soft contact surface. The force information is inferred by a deep-neural-network-based machine-learning method that maps images to the spatial distribution of 3D contact force (normal and shear), including numerous distinct contacts with widely varying contact areas.

Extensive experiments show that Insight has an **overall spatial resolution of 0.4 mm**, **force magnitude accuracy around 0.03 N**, and **force direction accuracy around 5 degrees** over a range of 0.03-2 N. It is sensitive enough to feel its own orientation relative to gravity, and its tactile fovea can be used to sense object shapes. The presented hardware and software design concepts can be extended to achieve robust and usable tactile sensing on a wide variety of robot parts with different shapes and sensing requirements. Ongoing work aims to reduce Insight's size, increase its framerate, and add other haptic sensing modalities such as vibration.
