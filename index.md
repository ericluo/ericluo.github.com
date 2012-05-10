---
layout  : page
title   : 夹缝中生存的程序员
tagline : GTD、数据分析
---
<ul class="posts">
{% for post in site.posts limit: 5 %}
  <div class="post_info">
    <li>
            <a href="{{ post.url }}">{{ post.title }}</a>
            <span>({{ post.date | date:"%Y-%m-%d" }})</span>
    </li>
    </br> <em>{{ post.content | trancatewords:20 }} </em>
    </div>
  {% endfor %}
</ul>
