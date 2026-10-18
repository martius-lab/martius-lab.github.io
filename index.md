---
logo: images/logo-color.png
logo-badge: true
---

# Autonomous Learning Group

**Distributed Intelligence / Autonomous Learning**, Department of Computer Science, University of Tübingen

We are interested in autonomous learning, that is how an embodied agent can determine what to learn, how to learn, and how to judge the learning success.
In particular, we focus on learning to control a robotic body in a developmental fashion.
Artificial intrinsic motivations are a central component that we develop using information theory and dynamical systems theory.
We work on reinforcement learning, representation learning, and internal model learning.

{% include slider.html data="group-photos" %}

{% include section.html %}

## Highlights

{% capture text %}

Model-based and model-free reinforcement learning, intrinsic motivation, representation learning, combinatorial optimization, haptic sensing, and machine learning for science.

{%
  include button.html
  link="research"
  text="Explore our research"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/projects/areas/model-based-rl.webp"
  link="research"
  title="Our Research"
  text=text
%}

{% capture text %}

All our papers, searchable and sorted by year.

{%
  include button.html
  link="publications"
  text="See our publications"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/projects/insight-haptic-sensor/teaser.webp"
  link="publications"
  title="Our Publications"
  flip=true
  text=text
%}

{% capture text %}

PhD students, postdocs, and researchers in Tübingen and Zürich.

{%
  include button.html
  link="team"
  text="Meet our team"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/group/2024-schruns.webp"
  link="team"
  title="Our Team"
  text=text
%}

{% include section.html %}

## Latest News

{% include list.html data="posts" component="post-excerpt" filter="date > (Time.now - 365*24*3600)" %}

{%
  include button.html
  link="blog"
  text="All posts"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% include section.html %}

## Funding and Sponsors

{% capture content %}

{% include figure.html image="images/funders/erc.webp" link="https://erc.europa.eu/" width="160px" %}
{% include figure.html image="images/funders/ml-cluster.webp" link="https://uni-tuebingen.de/forschung/forschungsschwerpunkte/exzellenzcluster-maschinelles-lernen/home/" width="160px" %}
{% include figure.html image="images/funders/tuebingen-ai.webp" link="https://tuebingen.ai/" width="160px" %}
{% include figure.html image="images/funders/imprs-is.webp" link="https://imprs.is.mpg.de/" width="160px" %}
{% include figure.html image="images/funders/cyber-valley.webp" link="https://cyber-valley.de/" width="160px" %}
{% include figure.html image="images/funders/volkswagen-foundation.webp" link="https://www.volkswagenstiftung.de/" width="160px" %}
{% include figure.html image="images/funders/bw-stiftung.webp" width="160px" %}
{% include figure.html image="images/funders/bmftr.webp" width="160px" %}

{% endcapture %}

{% include grid.html content=content %}

## Our Spin-offs

- [pi_optimal](https://pi-optimal.com/)
- [Polybot](https://polybot.eu/)
- [Ontic Labs](https://onticlabs.io/)
