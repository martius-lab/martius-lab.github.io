---
title: Symbolic Regression and Equation Learning
area: ml-for-science
image: images/projects/symbolic-regression/teaser.webp
description: The Equation Learner (EQL) distills concise, interpretable analytic equations from data, enabling strong extrapolation and applications in the natural sciences.
status: current
---

{% include figure.html image="images/projects/symbolic-regression/fig1.webp" %}

When analyzing data in the context of natural sciences, the prime aim is often to gain understanding by distilling compact and interpretable analytic equations. Instead, contemporary supervised machine learning methods mostly produce unstructured and dense mapping functions from input to output with the aim to make accurate numeric predictions.

In this project, we aim to automate the extraction of concise functional equations from data by developing new machine learning methods. Our first method, called Equation Learner (EQL), is a modified feed-forward neural network containing algebraic base functions, such as cosine, multiplication, square root, exponential, and so forth. Using a particular regularization and model selection scheme and sufficient domain priors, we can often discover the correct analytical expressions, which then enable strong extrapolation performance. In a proof of principle, we show that the equations of motion of a cart-pendulum robot can be identified after only 20 seconds of random interaction -- enabling successful model-based control.

The beauty of our approach is that it can be embedded in larger neural networks or other differentiable processing pipelines. This is a property that we exploit in a collaboration project with the University of Tübingen to create effective descriptions of fluid particles. We were able to create a machine learning system using EQL to find suitable density functionals for simple fluids. Currently, we are investigating fluids of particles with anisotropic potentials which are important in many applications, such as drug design.

In another collaboration, we are deploying machine learning methods to improve the understanding of quantum systems. Given a physical system in which a subsystem is embedded in a larger system, i.e. a bath, we used neural networks to learn the generator of the subsystem's dynamics. Our analysis shows under which conditions Markovian generators are accurate and where long-term predictions can be made.
