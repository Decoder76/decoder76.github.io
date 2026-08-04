layout: default title: Projects permalink: /pages/projects/
Project Portfolio
{% for project in site.projects %}

[{{ project.title }}]({{ project.url }})
{{ project.overview }}

Tech Stack: {{ project.stack | join: " • " }} {% endfor %}

Projects
{% for data_project in site.data.projects %}

[{{ data_project.title }}](/projects/{{ data_project.slug }}/)
{{ data_project.summary }} {{ data_project.stack | join: " • " }} {% endfor %}
