---
layout: page
title: "Experience"
permalink: /experience/
description: "Professional experience across machine learning, Ruby on Rails development, and operational systems."
---

A career spanning applied machine learning, backend software development, and the operational workflows that software needs to support.

---

{% for exp in site.data.experience %}
## {{ exp.role | escape }} — {{ exp.company | escape }}

{% for point in exp.points %}
- {{ point | escape }}
{% endfor %}

---
{% endfor %}
