---
layout: default
title: Blog
permalink: /pages/blog/
---
## Blog
{% for post in site.posts %}
- [{{ post.title }}]({{ post.url }})
{% endfor %}
## Technical Blog
- [From Operations to AI Engineering](/2026/05/25/from-operations-to-ai-engineering/)
