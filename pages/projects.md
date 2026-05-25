---
layout: default
title: Projects
permalink: /pages/projects/
---
## Projects
{% for project in site.data.projects %}
### [{{ project.title }}](/projects/{{ project.slug }}/)
{{ project.summary }}
`{{ project.stack | join: " • " }}`
{% endfor %}
