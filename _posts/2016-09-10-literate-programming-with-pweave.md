---
title: literate programming with pweave
layout: post
---

# `Pweave` 安装

	 conda install -c mpastell pweave


# `Pweave` 文档转换方法

使用下述命令行可以将含有 `Python` 的文档转换为嵌入了代码块的 `markdown` 的文档。

	pweave -i markdown -f pandoc(markdown) source.markdown 

如果需要直接转换为其他格式，可以通过 `-f` 参数来进行设置。

如果需要转换为 html 格式，需要使用 `tabulate` 函数来变换，即

	```{python, evaluate=True, results='rst', echo=False}
	tabulate(df, tablefmt='html')
# 网格交易策略

chuck options:

* evaluate(True|False)
* results(verbatim|hidden|tex|rst)
* echo(True|False)

## 示例



~~~~{.python}
import numpy as np
import pandas as pd
from tabulate import tabulate

down, up = 0.59, 0.79
steps = 8
net = ["{:3.3f}".format(i) for i in np.linspace(down, up, steps)]
unit = 70000 / 10
strategy = list(zip(net, [4,3,2,1,1,2,3,4], ['买入'] * 4 + ['卖出'] * 4))
df = pd.DataFrame(strategy, columns=['网格价格', '资金份数', '交易方向'])
df['金额'] = df['资金份数'] * unit
df.sort_values('网格价格', ascending=False)

print(tabulate(df, tablefmt='pipe', headers='keys'))
~~~~~~~~~~~~~

|    |   网格价格 |   资金份数 | 交易方向   |    金额 |
|---:|-------:|-------:|:-------|------:|
|  0 |  0.59  |      4 | 买入     | 28000 |
|  1 |  0.619 |      3 | 买入     | 21000 |
|  2 |  0.647 |      2 | 买入     | 14000 |
|  3 |  0.676 |      1 | 买入     |  7000 |
|  4 |  0.704 |      1 | 卖出     |  7000 |
|  5 |  0.733 |      2 | 卖出     | 14000 |
|  6 |  0.761 |      3 | 卖出     | 21000 |
|  7 |  0.79  |      4 | 卖出     | 28000 |



|    |   网格价格 |   资金份数 | 交易方向   |    金额 |
|---:|-------:|-------:|:-------|------:|
|  0 |  0.59  |      4 | 买入     | 28000 |
|  1 |  0.619 |      3 | 买入     | 21000 |
|  2 |  0.647 |      2 | 买入     | 14000 |
|  3 |  0.676 |      1 | 买入     |  7000 |
|  4 |  0.704 |      1 | 卖出     |  7000 |
|  5 |  0.733 |      2 | 卖出     | 14000 |
|  6 |  0.761 |      3 | 卖出     | 21000 |
|  7 |  0.79  |      4 | 卖出     | 28000 |