---
title: atom编辑器设置
tags: editor sa
permalink: /tech/atom/
toc: true
---

借着这两天的空闲，将自己日常用的编辑器从`Sublime`切换到了`Atom`，前者基于`Python`的内核，后者基于现代的`Web`技术。前者更新较慢，没有大公司或团队支撑，后者是`Github`出品，且版本更新更为频繁。更重要的是，其使用了基于`Coffeescript`, `Less`的JavaScript和css的成熟技术，以`Chrome`为内核，更具有现代感。在页面展示上效果更佳！特别是在编写`Markdown`的过程中，可以在编辑器内进行展示，太强大了。

## 插件安装设置

由于安装插件的网站被墙了，导致安装时进程会出一些莫名其妙的错误。解决方案是：要么使用`VPN`，要么使用国内的源。幸运的是国内已有相关的镜像了！在 `~\.atom\.apmrc`文件（如果没有这个文件，新建一个）中，添加如下两条配置信息：

> registry=https://registry.npm.taobao.org/  
> strict-ssl=false

{% gist ericluo/9224d6472c38b76e68121528839fdba5 %}

还有一种方式是通过使用代理(蓝灯)，通过代理来访问国外的源。但是在升级过程中总是会出现权限不够的异常，可以通过**使用系统管理员权限的 CMD 来执行插件升级命令**解决这个问题。:feelsgood:

## 插件清单

`Atom`自身就是使用插件架构堆积而成，除其官方自带的插件外，比较好用的社区插件如下：

- atom-beautify

- git-plus 在编辑器中自己调用git命令

- markdown-writer 提供了一组基于jekyll的工具和snippet

- markdown-img-paste 方便的图床管理包，将剪贴板中的图标上传图床并插入markdown文档

- markdown-scroll-sync 同步`Markdown`和`Preview`之间的内容

- platformio-ide-terminal 编辑器中的终端管理包

  - terminal-plus 同上，但是暂时有bug，无法正常使用。

    **该包目前在`Windows10`下有`bug`,打开终端后，系统frozen了，无法使用，目前没有办法解决。**

- script 执行各种脚本文件的包

- vim-mode-plus

- ex-mode 同上

- atom-chrome 使用Atom来编辑Chrome中的文本框

- eval-and-replace 用于动态执行代码片段

  对于拷贝的url可以通过coffeescript `decodeURI 'encoded url'` 来对其进行解码，然后`Execute coffeeScript`即可。

- gist 在`Atom`中分享代码片段到<https://gist.github.com>

- autocomplete-emojis 支持在`Atom`中直接自动完成并预览对应的emoji。

- atom-csv-markdown 将csv格式的数据转换为`Markdown`的表格

- todo-show 按 workspace/project/file 搜索并显示任务标签

### 不同电脑之间配置文件的同步(`sync-settings`)

可以通过`sync-settings`来进行不同电脑之间配置文件的同步，其使用了`gist`作为后端存储。因此在系统配置上需要做如下设置：

- Personal Access Token

需要从`Github`网站上重新生成Token: (218eb08ca8469bc1ce785df71901a6878e832951)

- Gist id

> 7f228e0a47090155cb7bb248099f2d53

#### 用法

调用如下命令来进行配置文件查看、备份、恢复和检查。

- sync-settings:backup

- sync-settings:restore

- sync-settings:view-backup

- sync-settings:check-backup

- sync-settings:fork

### VIM 编辑器(`vim-mode-plus`）

新版的`vim-mode-plus`可以支持在退出`insert mode`时禁用输入法，在中文环境下需要频繁切换输入法的麻烦终于去除了，而且也不需要借助于外部的脚本（ime_helper.py）和输入法切换插件来帮忙了。😄

| commands         | 功能                                     |
| ---------------- | ---------------------------------------- |
| Ctrl-w z         | 最大化当前窗口并且居中                   |
| Ctrl-w Z         | 最大化当前窗口并且不居中                 |
| Ctrl-.           | 显示快捷键所绑定的命令                   |
| Ctrl-.           | 显示`settings`                           |
| Tab or Shift-tab | 增量搜索时在匹配项间跳动                 |
| gv               | 重新选择上次选择的区域                   |
| coip             | `o`用于将`cip`的功能转移到`occurrence`上 |
| go               | 预先设置`occurrence`                     |

#### `preset-occurrence` 和 `persistent-selection`

`g o` 将当前光标下的单词设置为 `preset-occurrence`。可以重复多次，将多个单词设置为 `occurrence`。

通过 `v`, `V`, `Ctrl-v` 来进行可视化选择后，可以通过 `Enter` 键来**持续化选择**，即`persistent-selection`。

#### 字符处理

VMP 提供了 `transform-string-by-select-list`，可以用于对选定的字符串进行字符变换，变换函数很多，不可能记得每个函数的名称。则可以`Command Palette`中输入`transform-string-by-select-list`来显示并选择变换函数名称。如果已经知道函数名称，则可以直接在`Command Palette`中调用。

## VMP 中的 `Text Object`

![](https://netimages.oss-cn-beijing.aliyuncs.com/img/20181029173438.png)

## 软件更新

将软件的自动更新关闭。**今后有大版本出来，或是使用过程中碰到软件缺陷的时候才作版本更新**，要不然跟随版本更新的操作太耗时了。
