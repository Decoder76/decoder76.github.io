---
layout: page
title: "Technical Skills"
permalink: /pages/skills/
---

**Comprehensive Technology Stack** categorized by engineering domain and system architecture depth.

---

### Skill Matrix

{% for skill_group in site.data.skills %}
* **{{ skill_group.category }}:** `{{ skill_group.items | join: " • " }}`
{% endfor %}
