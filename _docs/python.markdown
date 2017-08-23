---
tags: Python
---

{% include toc %}

## `_builtins_`


### 数据类型 `type`

- bytearray,bytes, complex, float, int, bool
- classmethod, property, staticmethod, type
- dict, list, set, frozenset,  range, *slice*, tuple, str
- enumerate, filter, map, zip

### 函数 `function`

## 时间转换

在Python中经常要用到的时间格式的转换，如从字符串转换为日期格式，或是从日期格式转换为字符串，还有时候需要将整数数值型转换为字符串。可以借助于标准库 `datetime`中的相关函数来实现。

```python
import datetime
d = datetime.datetime.strptime(str(20151231), '%Y%m%d')
```

## 函数式编程

> map filter zip enumerate range str tuple type


## `Pandas`

可以通过`set_option`相关函数来对`Pandas`的输入和显示效果进行设置，如通过 `display.precision` 控制项来设置浮点数显示的位数。

```python
  pd.set_option('display.precision', 2) # default to 6
```

`Pandas`中常用的对象主要有`DataFrame`、`Series`和`Panel`，3个不同对象之间提供了相应的方法可以相互转化。

- pd.DataFrame()
- panel.xs()、minor_xs, major_xs

3个对象中比较好用的方法记录如下：

- Series
  - value_counts 统计序列中不同值的个数
  - size


- DataFrame
  - fillna 将`NA`替换为缺省值
  - sort_index
  - groupby(['year', 'sex'])
  - pivot_table('births', rows='year', cols='sex', aggfunc=sum)
  - filter(regex = pattern)


- Panel
  - 构造函数
    - pd.Panel(data)
    - pd.Panel.from_dict(data, orient='minor')
    - df.to_panel() ** df with a two-level index **

  - 改变`axis`的数据类型

    `panel.minor_axis = pd.to_datatime(panel.minor_axis, format="%Y%m%d")`

### 显示格式控制

可以通过`df.style`属性来对`dataframe`的显示格式进行控制，参见[DataFrame.style](http://pandas.pydata.org/pandas-docs/stable/style.html#)

如下面的代码可以设置以保留两位小数，以逗号为千分位字符的百分比格式来显示：

    df.style.format("{:,.2%}")
    df.style.format({columnlabel: "{:,.2%}"})

### [`plotly`](https://plot.ly/pandas/)

在使用`Pandas`进行数据分析研究时，需要用到`dataframe.plot`的函数来进行绘图，但是用该函数绘图使用中文时需要做特殊的设置，非常不方便。网上看到有推荐使用`plotly`的，该包可以将生产的图片自动地保存到云上，这样在文档中直接插入对应的链接就可以了。**更重要的是，还可以对图像进行动态的更新，而不需要对原有文档进行更新，倒是可以省不少事。**

`plotly`账号信息（在ricequant上的文档中有记录）：

通过底层的`API`来使用`plotly`比较繁琐，如下面的示例。但是可以通过`cufflinks`库来辅助直接在`dataframe`上使用`iplot`进行画图。但是对于比较复杂的图，折必须通过原始的`plotly API`来进行画图。

```python

import plotly
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go

plotly.offline.init_notebook_mode()

fig = tls.make_subplots(rows=2, cols=1, shared_xaxes=True)

for bank in dfs['净利差']:
    fig.append_trace(go.Scatter(x=data.major_axis, y=dfs['净利差'][bank], name=bank), 1,1)
for bank in dfs['净息差']:
    fig.append_trace(go.Scatter(x=data.major_axis, y=dfs['存贷差'][bank], name=bank), 2,1)

plotly.offline.iplot(fig)

```

#### 在文章中引用图像

可以通过`iframe`技术来在文章中直接引用生产的图像文件。

```html
<iframe width="800" height="600" frameborder="0" scrolling="no"  src="//plot.ly/~luowenbo/2.embed"></iframe>
```

**并可以用[参数](http://help.plot.ly/embed-graphs-in-websites/#step-8-customize-the-iframe)来控制图像中的相关元素。**

![](http://7xonmk.com1.z0.glb.clouddn.com/2017-03-04_13-05-47.png)

#### traces & layout

`plotly`中的两类对象是`traces` 和 `layout`。[API Reference](https://plot.ly/python/reference/#layout)

调用方法如下：

```python
data = [
    go.Scatter(                         # all "scatter" attributes: https://plot.ly/python/reference/#scatter
        x=[1, 2, 3],                    # more about "x":  /python/reference/#scatter-x
        y=[3, 1, 6],                    # more about "y":  /python/reference/#scatter-y
        marker=dict(                    # marker is an dict, marker keys: /python/reference/#scatter-marker
            color="rgb(16, 32, 77)"     # more about marker's "color": /python/reference/#scatter-marker-color
        )
    ),
    go.Bar(                         # all "bar" chart attributes: /python/reference/#bar
        x=[1, 2, 3],                # more about "x": /python/reference/#bar-x
        y=[3, 1, 6],                # /python/reference/#bar-y
        name="bar chart example"    # /python/reference/#bar-name
    )
]

layout = go.Layout(             # all "layout" attributes: /python/reference/#layout
    title="simple example",     # more about "layout's" "title": /python/reference/#layout-title
    xaxis=dict(                 # all "layout's" "xaxis" attributes: /python/reference/#layout-xaxis
        title="time"            # more about "layout's" "xaxis's" "title": /python/reference/#layout-xaxis-title
    ),
    annotations=[
        dict(                            # all "annotation" attributes: /python/reference/#layout-annotations
            text="simple annotation",    # /python/reference/#layout-annotations-text
            x=0,                         # /python/reference/#layout-annotations-x
            xref="paper",                # /python/reference/#layout-annotations-xref
            y=0,                         # /python/reference/#layout-annotations-y
            yref="paper"                 # /python/reference/#layout-annotations-yref
        )
    ]
)

figure = go.Figure(data=data, layout=layout)

py.plot(figure, filename='api-docs/reference-graph')
```

#### [cufflinks](https://github.com/santosjorge/cufflinks)

其调用方法为: `df.iplot(xTitle='', yTitle='', title='', layout='')`

`cufflinks`也提供了一些方法来生产`subplots`，如：

```python
df = pd.DataFrame(np.random.rand(10,2), columns=['Col1', 'Col2'] )
df['X'] = pd.Series(['A','A','A','A','A','B','B','B','B','B'])
figs=[df[df['X']==d][['Col1','Col2']].iplot(kind='box',asFigure=True) for d in pd.unique(df['X']) ]
cf.iplot(cf.subplots(figs))
```

##### 饼图

在使用饼图之前，一定要想想是否合适，可能用其他的图(如柱状头bar)具有更好的表现力。

```python
df.iplot(kind='pie', labels=, values=, hole=0.3, textposition='inside',textinfo='label+percent+value', legend=False)
```
### FAQ



## Jupyter

`Jupyter Notebook` 是一个很方便的学习、研究和文档撰写平台。通过这两天的研究，已经初步掌握了其日常的用法。通过在 `Markdown` 文档中嵌入 `Python` 的脚本，可以通过后者来生成动态的图片、表格，甚至还可以增加一些动态的交互效果。

### 设置主页目录

默认状态下，`Notebook` 的 HOME 目录设置在当前用户主目录下。该目录混杂了所有用户相关的文件信息，比较杂乱。而且，该目录下的文件没有进行自动云端同步。不同电脑之间的研究文档同步只能通过手动操作，比较繁琐。

更好的解决方案是设置专用的 HOME 目录，并将该目录设置在 `OneDrive` 下。具体操作过程如下：

- 通过如下命令生成配置文件。

```bash
jupyter notebook --generate-config
```

该命令会在用户主目录下生成一个配置文件: ".jupyter/jupyter_notebook_config.py"

- 在该配置文件中设置文档目录, **注意设置中的双斜线**

```python
c.NotebookApp.notebook_dir = u"C:\\Usersi\\CBRC\\OneDrive\\workspace\\investment"
```

- 重启 `Jupyter`，就可以看到 HOME 目录已经更新了。

## Links

- [pandas](http://pandas.pydata.org)
- [Python中文开发者社区](http://pythontab.com)
- [Pands in 15 minutes](http://www.cnblogs.com/chaosimple/p/4153083.html)
