---
layout: page
title: "Experience"
permalink: /experience/
---

**Professional Journey & Technical Milestones** across software development, backend systems, and applied machine learning.

---

### Timeline & Milestones

{% for exp in site.data.experience %}
#### **{{ exp.title }}** — *{{ exp.organization }}*
{{ exp.description }}

* **Duration:** {{ exp.period }}
* **Tech Stack:** `{{ exp.tech | join: " • " }}`
---
{% endfor %}
