---
layout: default
title: Experience
permalink: /pages/experience/
---
## Experience
{% for item in site.data.experience %}
### {{ item.role }} — {{ item.company }}
{% for point in item.points %}- {{ point }}
{% endfor %}
{% endfor %}
