---
layout: default
title: Projects
permalink: /pages/projects/
---
## Project Portfolio
{% for project in site.projects %}
### [{{ project.title }}]({{ project.url }})
{{ project.overview }}

**Tech Stack:** `{{ project.stack | join: " • " }}`

{% endfor %}
