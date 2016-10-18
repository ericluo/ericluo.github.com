---
title: python tips
layout: post
tags: python tips
---

## 时间转换

在Python中经常要用到的时间格式的转换，如从字符串转换为日期格式，或是从日期格式转换为字符串，还有时候需要将整数数值型转换为字符串。可以借助于标准库 `datetime`中的相关函数来实现。

```python
import datetime
d = datetime.datetime.strptime(str(20151231), '%Y%m%d')
```

## Functional Programming

* map
* filter
* zip
* dict
* enumerate
* range
* str
* tuple
* type
* set
* reversed
