---
title: "Learning Pandas Notes"
author: MrAlpha
date: "2018-02-03 16:53"
tags: 读书笔记 Python
---

## 数据类别

- 结构化数据
- 非结构化数据，如文件、图片、视频等
- 半结构化数据， 如 `JSON`

## 变量类型

- Categorical
- Continuous
- Discrete
- **Time Series data**

## 单变量分析与多变量分析

- 单变量分析（描述性统计），`pandas` 主要设计目标和用途

  - 变量分布
  - 集中程度，mean, median, and mode
  - 分散程度

- 多变量分析（推理性统计学），`StatsModels, SciPy`

  - 相关性、回归
  - t-test, chi square, ANOVA, Bootstrapping

## DataFrame and Series

### 数据切片(slice) 或 切丁(dice)

```python
  # slice by column
  df['column']
  df[['column1', 'column2']]

  # slice by row
  df.loc[]
  df.iloc[]

  # slice by start:end:step
  series[start:end:step]
  df[start:end:step]
```

### Series

#### 使用 `NumPy` 来创建

```python
  pd.Series(np.arange(4,9))
  pd.Series(np.linspace(0, 9, 5))

  np.random.seed(12345)
  pd.Series(np.random.normal(size = 5))

```

### DataFrame

#### 删除 `columns`

- del ex. `del dataframe[column]` 直接从 `dataframe` 中删除 `Series`

- pop() 删除 `Series` 并从 `dataframe` 中返回该 `Series`

- drop(labels, axis = 1) 删除对应的 `columns`，生成并返回一个新的 `dataframe`

## 日期数据转换

在从外部文件中使用 `pd.read_csv(filename, parse_dates = ['column1', 'column2'])` 中的 `parse_dates` 参数来制定相应的列为日期类型。

```python
  df = pd.read_csv("data/google.csv", parse_dates=['Date'], index_col = 'Date')
```
