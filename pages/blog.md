---
layout: page
title: "Technical Blog"
permalink: /pages/blog/
---

**Engineering Notes & Articles** — Deep dives into system design, artificial intelligence workflows, and backend development.

---

### Recent Articles

{% for post in site.posts %}
#### **[{{ post.title }}]({{ post.url }})**
* *Published:* {{ post.date | date: "%B %d, %Y" }}
* *Summary:* {{ post.excerpt | strip_html | truncate: 140 }}

[Read Full Article]({{ post.url }})
---
{% endfor %}
