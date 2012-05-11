---
layout  : page
title   : 夹缝中生存的程序员
tagline : GTD、数据分析
---
<div class="posts">
  {% for post in site.posts limit: 5 %}
  <div>
    <p class="excerpt">     
      <h2>
        <a href="{{site.baseurl}}{{ post.url }}">{{ post.title }}</a> 
      </h2>
      <span class="post-date" >({{ post.date | date_to_string }})</span>        
    </p>
    <div class="excerpt-post">
      {% if post.description %} 
      <p>{{ post.description }}</p>
      {% else %}
      <p>{{ post.content | strip_html | truncatewords: 30 }}</p>
      {% endif %}
      <p style="text-align:right">
        <span class="more">
          <a  href="{{site.baseurl}}{{ post.url }}">阅读全文...</a>
        </span>
      </p>
    </div>
  </div>
  {% endfor %}
  <center><a href="{{ site.baseurl }}/archives">文章列表</a></center>
</div>
