---
title: Research
nav:
  order: 1
  tooltip: Research areas and projects
---

# {% include icon.html icon="fa-solid fa-microscope" %}Research

We are interested in autonomous learning, that is how an embodied agent can determine what to learn, how to learn, and how to judge the learning success.
In particular, we focus on learning to control a robotic body in a developmental fashion.
Below are our research areas and projects. All our papers are listed on the [Publications]({{ "publications/" | relative_url }}) page.

{% for area in site.data.research-areas %}

{% include section.html %}

<h2 id="{{ area.key }}">{{ area.title }}</h2>

{% if area.image %}
  {% include feature.html image=area.image text=area.description flip=area.flip %}
{% else %}
  {{ area.description | markdownify }}
{% endif %}

{% assign projects = site.projects | where: "area", area.key | sort: "order", "last" %}
{% for project in projects %}
  {%
    include card.html
    title=project.title
    subtitle=project.subtitle
    image=project.image
    link=project.url
    description=project.description
    style=area.card-style
  %}
{% endfor %}

{% endfor %}
