---
layout: default
title: Blog
permalink: /pages/blog/
---
## Blog
{% for post in site.posts %}
- [{{ post.title }}]({{ post.url }})
{% endfor %}
