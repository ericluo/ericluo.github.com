---
layout  : page
title   : 夹缝中生存的程序员
tagline : GTD、数据分析
---
<div class="row">
  <div class="span12">
    <div class="row">
      <div class="span9">
        {% for post in site.posts limit: 5 %}
        <div class="row">
          <div class="span2">
            <h5 class="post-date" align="right">{{ post.date | date_to_string }}</h5>
          </div>
          <div class="span7">
            <h2><a class="post-title" href="{{site.baseurl}}{{ post.url }}">{{ post.title }}</a></h2>
            {{ post.content | strip_html | truncatewords: 30 }}
            <a href="{{site.baseurl}}{{ post.url }}">评论</a>
            <hr>
            <br/><br/>
          </div>
        </div>
        {% endfor %}
      </div>
      <div class="span3">
      </div>
    </div>
  </div>
</div>
<div class="row">
  <center><h3><a href="{{ site.baseurl }}/archive.html">文章列表</a></h3></center>
</div>
