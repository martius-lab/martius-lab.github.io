---
title: Publications
nav:
  order: 2
  tooltip: All our papers
---

# {% include icon.html icon="fa-solid fa-scroll" %}Publications

Generated from our BibTeX file.
Members of the group are shown in **bold**.

{% assign selected = site.data.citations | data_filter: "selected" %}
{% if selected.size > 0 %}

{% include section.html %}

## Selected

{% include list.html data="citations" component="citation" style="rich" filter="selected" %}

{% endif %}

{% include section.html %}

## All

{% include search-box.html %}

{% include search-info.html %}

{% include list.html data="citations" component="citation" style="rich" %}
