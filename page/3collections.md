---
layout: page
title: 资料汇编
permalink: /collection/
icon: bookmark
---

本文档收集整体日常工作、学习和生活中有用的工具、网站和相关小技巧。

# 工具

## Git

### 中文文件名乱码

参考以下的设置，在CygWin中git log内容已可正常使用、显示中文，但git status和push、pull时，中文文件名仍然乱码，不知如何解决，如:

```bash
[/data/soft/xstarcd.github.io]$git status
位于分支 master
您的分支与上游分支 'origin/master' 一致。
未跟踪的文件:
  （使用 "git add <文件>..." 以包含要提交的内容）

        "\346\265\213\350\257\225.txt"

提交为空，但是存在尚未跟踪的文件（使用 "git add" 建立跟踪）
```

解决方式：

```bash
#不对0x80以上的字符进行quote，解决git status/commit时中文文件名乱码
git config --global core.quotepath false
```

# 编程语言

## Ruby

## Python

### Links

- [pandas](http://pandas.pydata.org)
- [Python中文开发者社区](http://pythontab.com)

## 时间转换

在Python中经常要用到的时间格式的转换，如从字符串转换为日期格式，或是从日期格式转换为字符串，还有时候需要将整数数值型转换为字符串。可以借助于标准库 `datetime`中的相关函数来实现。

```python
import datetime
d = datetime.datetime.strptime(str(20151231), '%Y%m%d')
```

## 函数式编程

map filter zip enumerate range str tuple type

# 编辑器

## Sublime 中常用插件

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

# Comments

{% include comments.html %}
