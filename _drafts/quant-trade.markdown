---
title: quant trade
layout: post
tags: 投资
---

目前，机器人、人工智能概念层出不穷，阿尔法狗都战胜了围棋冠军，量化交易正在风口。如何发挥个人IT狗的特长，通过数据分析来研究分析投资策略，回测验证投资思路，应该是一个比较靠谱的路。

主要使用的平台拟采用 [RiceQuant](https://www.ricequant.com)。该平台具备以下优势：

- 数据全，不仅包括交易数据，还有比较好的基本面财务数据
- 能回测，可以对交易思路进行回测
- 模块化，在研究、模拟交易以及回测中，能引用自定义的函数，有利于模块化
- 更新快，该平台还处在不断的进化之中

# 财务数据查询

fundamentals是一个重要的对象，其中包括了

- 股指指标表（eod_derivative_indicator）
- 财务指标表（financial_indicator）
- 利润表（income_statement）
- 资产负债表（balance_sheet）
- 现金流量表（cash_flow_statement）
- 股票列表（stock_code）等

数据查询接口：其中`entry_date`为查询财务数据的 **基准开始日期**。

> get_fundamentals(query, entry_date, interval=None, report_quarter=False)


financials是在查询中会使用到的重要对象，功能与上述fundamentals类似。但因为get_financials为季度财务信息查询，所以financials中支持的财务表格包括:

- 利润表（income_statement）
- 资产负债表（balance_sheet）
- 现金流量表（cash_flow_statement）
- 财务指标（financial_indicator）
- 股票列表（stock_code）
- 公布日期（announce_date）

数据查询接口：其中`quarter`为财报回溯查询的 **起始报告期**，如"2016q4", "2015q3"等

> get_financials(query, quarter, interval=None)

# 单只股票基本面研究

基本面研究的主要关注点包括：营收、净利润、现金流、估值(PE、PB、)、ROE、ROA等指标。
