---
layout: page
title: 资料汇编
permalink: /collection/
icon: bookmark
---

本文档收集整体日常工作、学习和生活中有用的工具、网站和相关小技巧。

## 工具

* [box-shadow generator](http://www.cssmatic.com/box-shadow)

    生成 box-shadow 的工具。

## 编程语言

### Ruby

### Python

#### Links

- [pandas](http://pandas.pydata.org)
- [Python中文开发者社区](http://pythontab.com)

### 时间转换

在Python中经常要用到的时间格式的转换，如从字符串转换为日期格式，或是从日期格式转换为字符串，还有时候需要将整数数值型转换为字符串。可以借助于标准库 `datetime`中的相关函数来实现。

```python
import datetime
d = datetime.datetime.strptime(str(20151231), '%Y%m%d')
```

### 函数式编程

map filter zip enumerate range str tuple type

## 编辑器

### Sublime 中常用插件

- Package Controll
- Vintageous 
- Emmet
- GitGutter 
- SublimeGit
- Jekyll
- SublimeREPL
- MarkdownEditor
- Terminal
- Autofilename
- Alignment
- SublimeCodeIntel
- IMESupport 用于解决输入法不能光标跟随的Bug

## Comments

{% include comments.html %}
