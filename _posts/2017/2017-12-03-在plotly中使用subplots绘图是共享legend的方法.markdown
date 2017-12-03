---
title: "在plotly中使用subplots绘图时共享legend的方法"
author: MrAlpha
date: "2017-12-03 10:57"
tags: pandas plotly python
---

在 `plotly` 中使用 `subplots` 绘图时，常常不同的 `figure` 之间使用了相同的 `trace name`（其也自动被用作 `legend`）。这样，相同的 `legend` 会在图例部分重复出现。如何在不同的 `figure` 中共享这些图例呢？

其实，图例可以在两个层面进行设置：一是在 `layout` 中，还有一个是在 `trace` 中。

如果直接在 `layout` 中设置，即 `showlegend = False`，那么所有的图例均不会显示了，达不到目标。那么应该在 `trace` 上进行设置: `trace['showlegend'] = False`。

在使用 `subplots` 进行绘图时，控制第一个（或者某个特定）的 `figure` 中所有 `trace` 显示图例，而其他的所有 `trace` 中均不显示图例。就可以达到目标了。

但是，上述做法有一个弊端。不显示图例的图形中无法图例进行交互控制。如下图所示，可以通过点击某个或某些图例，控制显示的 `trace` 。图中，点击中信银行、浦发银行和兴业银行可以在图形中动态调整是否显示对应的数据。

![](http://7xonmk.com1.z0.glb.clouddn.com/2017-12-03_11-15-05.jpg)

那么，这是如何做到的呢？在 [plotly官网](https://github.com/plotly/plotly.py/issues/800)上可以找到答案。即可以通过 `showlegend` 和 `legendgroup` 两个参数的搭配来实现。将未显示图例的 `figure` 中的 `trace` 的 `legendgroup` 参数设置为与显示了图例的 `trace` 中对应的 `legendgroup` 设置为一样的即可。

```python
figs = [df.loc[:, govs].iplot(asFigure = True) for df in dfs]
for i, fig in enumerate(figs):
    for trace in fig['data']:
        trace['legendgroup'] = trace['name']
        if( i != 0):
            trace['showlegend'] = False
```
