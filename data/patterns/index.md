---
title: Patterns
---

This section contains small snippets that will help you in the process of data wrangling. They might be small useful tips of full blown tutorials on tools or topics.

**Note on the term 'pattern'**

The term pattern has developed a very specific meaning in software engineering. While we use the term in this sense, the tricks presented are not defined as a pattern using any of the formal templates that have developed for software design patterns.

<ul>
{% assign sorted_pages = (site.pages | sort: 'title') %}
{% for page in sorted_pages %}
{% if page.section == 'patterns' and page.name != 'index.md' %}
<li><a href="{{ page.url | prepend: site.baseurl }}">{{page.title}}</a></li>
{% endif %}
{% endfor %}
</ul>

