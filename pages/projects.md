---
layout: page
title: "Projects Showcase"
permalink: /pages/projects/
---

**Featured Engineering Work** — Production-grade systems, machine learning models, and automated RAG assistants.

---

### System Portfolio

{% for project in site.data.projects %}
#### **[{{ project.title }}]({{ project.detail_page }})**
{{ project.summary }}

* **Category:** {{ project.category }}
* **Tech Stack:** `{{ project.tags | join: " • " }}`
* **Key Metrics:** {% for metric in project.metrics %}`{{ metric.label }}: {{ metric.value }}` {% unless forloop.last %}•{% endunless %} {% endfor %}

[View Repository]({{ project.github }})
---
{% endfor %}
