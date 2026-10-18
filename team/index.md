---
title: Team
nav:
  order: 3
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %}Team

{% include slider.html data="group-photos" %}

{% include section.html %}

## Group Head

{% include list.html data="members" component="portrait" filter="role == 'principal-investigator'" %}

## Administration

{% include list.html data="members" component="portrait" filter="role == 'admin'" %}

## Researchers

{% include list.html data="members" component="portrait" filter="role == 'postdoc' || role == 'researcher'" %}

## PhD Students

{% include list.html data="members" component="portrait" filter="role == 'phd'" %}

## Master and Bachelor Students

{% include list.html data="members" component="portrait" filter="role == 'student'" style="tiny" %}

{% include section.html %}

## Alumni

{% include list.html data="members" component="portrait" filter="role == 'alumni'" style="small" %}
