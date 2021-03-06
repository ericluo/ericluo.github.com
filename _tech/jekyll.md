---
tags: jekyll
permalink: /tech/jekyll/
---

## 升级`jekyll`

要定期升级`jekyll`的版本，使之与`github`上的版本一致。

    bundle update

## [kramdown](https://kramdown.gettalong.org/quickref.html)

`Jekyll`使用了`kramdown`作为`Markdown`的解释引擎，其具有比标准的`Markdown`更多的扩展标记，因此也能提供更加丰富的表现形式。

支持的标签有：

- [Definition Lists](https://kramdown.gettalong.org/syntax.html#definition-lists)
- [Tables](https://kramdown.gettalong.org/syntax.html#tables)
- [Block Attributes](https://kramdown.gettalong.org/syntax.html#block-ials)
- [Extensions](https://kramdown.gettalong.org/syntax.html#extensions)
- [Footnotes](https://kramdown.gettalong.org/syntax.html#footnotes)
- [Abbreviations](https://kramdown.gettalong.org/syntax.html#abbreviations)
- [Inline Attributes](https://kramdown.gettalong.org/syntax.html#span-ials)

### 小技巧

- 在行尾加2个或更多的空格可以添加换行(`<br/>`)
- 当代码块中含有 `{` 标签时，可以使用 `raw` 块，参见本文档 `gist` 部分。
- 可以通过将从其他软件（如`Jupyter`、`Excel`等数据处理软件）导出`csv`格式的数据拷贝到`Markdown`文档中，并借助于`atom-csv-markdown`插件来方便地将其转换为`html`表格。
- $ $ inline formula
- $$ $$ formula code block
- sub and sup tags for subscript and superscript
- --- will become an em-dash (like this —)
- -- will become an en-dash (like this –)
- ... will become an ellipsis (like this …)
- << will become a left guillemet (like this «) – an optional following space will become a non-breakable space
- \>> will become a right guillemet (like this ») – an optional leading space will become a non-breakable space
- ^ 可以用来将隔离两个 `list`

## [Liquid](https://shopify.github.io/liquid/)

`Jekyll`使用了`Liquid`语言作为模板语言，其主要有三种类型：

- **object** 可以直接生成`html`字符串内容

- **Tag**

  - **Control Flow**: if, unless, elsif/else, case/when

  - **Iteration**: for, break, continue, for(limit, offset, range, reversed), cycle, tablerow

  - **Variable**: assign, capture

- **Filter** map, sort, uniq, *strip_html*, *url_encode*, *url_decode*, etc


## jekyll-gist插件

安装好`gist-it`插件后，设置好对应的`token`，就可以在`Atom`中直接 **gist** 代码片段了。

接下来，就需要在`markdown`文档中引用刚刚创建的`gist`。

```liquid
  {% raw %}{% gist ericluo/8a94b03781aaa65941b6978c9b89c578 %}{% endraw %}
```

## jekyll应用疑难问题

### 添加具有 `{` 符号的 `code block`

由于 `Jekyll` 对 `code block` 中的 `Liquid filters or tags` 进行处理，因此代码中如果含有 `{` 等符号，需要用 {% raw %} 和 {% endraw %} 进行封装，如上述 `jekyll-gist插件` 部分所示。

>Jekyll processes all Liquid filters in code blocks If you are using a language that contains curly braces, you will likely need to place {% raw %} and  {% endraw %} tags around your code.


### SSL认证

在Windows上启动`jekyll`以后，会碰到的问题如下：

```bash
  GitHub Metadata: No GitHub API authentication could be found. Some fields may be missing or have incorrect data.
```

```bash
  Error: SSL_connect returned=1 errno=0 state=SSLv3 read server certificate B: certificate verify failed
```

主要解决的问题有：

1. 下载证书< https://curl.haxx.se/ca/cacert.pem>，并设置环境变量`SSL_CERT_FILE`指向该文件
2. 设置`GitHub Token`相关的环境变量`JEKYLL_GITHUB_TOKEN`
3. 升级`Rubygems`的版本到最新版本

```bash
  gem update --system
```

### 文章无法显示

今天碰到一个问题，新写的帖子再本地和`GitHub`上均无法显示，好像是丢失了。但是查看文件缺失在哪里。最后最终到原因在于在`_config.yml`中设置的时区，导致其认为是一个将来的帖子，自动忽略了，没有生产对应的文件。解决这个问题可以在启动时加上 **future** 的开关。

    bundle exec jekyll server --future

还有一个坑是总是报错说错误地使用了`post_url`这个`Tag`，即：

正确的写法如下，其中指向文件目录为相对应`_posts`的相对路径，且文件名可以不用添加后缀名。而使用`link`这个tag的时候，文件路径是相对于根目录的，且文件名必须加后缀名。详细调用方法参见<http://jekyllrb.com/docs/templates/>

但是，将错误的写法改正后，系统还是报原来的错误！经过网上查找相关解答，似乎是当前`Jekyll`的版本（3.3.1）的一个缺陷。~~待`GitHub Pages`升级后，试试新版本的`Jekyll`还有没有类似的问题。~~ **将 `github-pages`的版本升级到129以后（对应的`Jekyll`的版本升到到了3.4.3），改问题解决了。**
{: .notice--danger}
