---
title: Equation Learner for Extrapolation and Control
area: ml-for-science
image: images/projects/eql-extrapolation-control/teaser.webp
description: Identifying system equations from a limited data range with gradient-based training, yielding models that extrapolate and enable highly data-efficient control.
status: current
---

{% include figure.html image="images/projects/eql-extrapolation-control/fig1.webp" %}

Intelligent systems today, including physical robots, are capable of amazing feats compared to their early predecessors. However, much of the planning and control relies on the accurate identification of the robotic system, often in the form of known physics equations derived by experienced engineers. In the case when the system model is unknown, various function approximations have been used in the context of model-based reinforcement learning. There is a typical trade-off between the explicability and model capacity when applying function approximation, e.g., deep neural networks may model complex system dynamics but are hard to interpret and optimize. Typically, control and planning tasks require much higher accuracy compared to regular machine learning tasks. In addition, it naturally occurs that unseen parts of the state space are visited. So we wish to address the problem of learning models that are highly accurate and also able to extrapolate.

Instead of resorting to black-box function approximation we designed a system to *identify the system equation from a limited data range* using gradient-based neural network training. In this way, we solve a symbolic regression problem using a continuous optimization method. The crucial aspect of the method is to find the simplest solution that still explains the data well -- implementing Occam's razor.

The identified equations are suitable for extrapolation to unseen domains which we demonstrate using several synthetic and real-world systems. Most importantly we show how to use these learned equations to obtain a highly efficient learning algorithm for control and planning. In our first experiment, a cart-pendulum system learns to swing up from scratch after two random rollouts. Ongoing work is to improve the efficiency and applicability of the method and applying it to challenging robotic systems.

- [Slides (pdf)](https://al.is.mpg.de/uploads/ckeditor/attachments/883/Martius_EQL_2018.pdf) (from a presentation in Edinburgh 2019)
- [Poster (pdf)](https://uni-tuebingen.de/fileadmin/Uni_Tuebingen/Fakultaeten/MatNat/Fachbereiche/Informatik/Lehrstuehle/Distributed_Intelligence/Research/Equation_Learner_for_Extrapolation_and_Control/ICML2018-poster.pdf) (ICML 2018)
- [Video](https://youtu.be/MG9q3gTtBLs) (YouTube)

{% include figure.html image="images/projects/eql-extrapolation-control/poster.webp" link="https://uni-tuebingen.de/fileadmin/Uni_Tuebingen/Fakultaeten/MatNat/Fachbereiche/Informatik/Lehrstuehle/Distributed_Intelligence/Research/Equation_Learner_for_Extrapolation_and_Control/ICML2018-poster.pdf" caption="ICML 2018 poster" width="400px" %}
