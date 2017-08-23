---
title: atom编辑器设置
tags: editor sa
permalink: /docs/atom/
---

借着这两天的空闲，将自己日常用的编辑器从`Sublime`切换到了`Atom`，前者基于`Python`的内核，后者基于现代的`Web`技术。前者更新较慢，没有大公司或团队支撑，后者是`Github`出品，且版本更新更为频繁。更重要的是，其使用了基于`Coffeescript`, `Less`的JavaScript和css的成熟技术，以`Chrome`为内核，更具有现代感。在页面展示上效果更佳！特别是在编写`Markdown`的过程中，可以在编辑器内进行展示，太强大了。

{% include toc %}

# 插件安装设置

由于安装插件的网站被墙了，导致安装时进程会出一些莫名其妙的错误。解决方案是：要么使用`VPN`，要么使用国内的源。幸运的是国内已有相关的镜像了！在 `~\.atom\.apmrc`文件（如果没有这个文件，新建一个）中，添加如下两条配置信息：

> registry=https://registry.npm.taobao.org/  
> strict-ssl=false

# 使用插件

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

- vim-mode-plus(在中文输入状态下，可以使用 **inset mode**，或者是禁用该插件)

- ex-mode 同上

- atom-chrome 使用Atom来编辑Chrome中的文本框

- eval-and-replace 用于动态执行代码片段

  对于拷贝的url可以通过coffeescript `decodeURI 'encoded url'` 来对其进行解码，然后`Execute coffeeScript`即可。

- gist-it 在`Atom`中分享代码片段到<https://gist.github.com>

- autocomplete-emojis 支持在`Atom`中直接自动完成并预览对应的emoji。

- atom-csv-markdown 将csv格式的数据转换为`Markdown`的表格


# 不同电脑之间配置文件的同步

可以通过`sync-settings`来进行不同电脑之间配置文件的同步，其使用了`gist`作为后端存储。因此在系统配置上需要做如下设置：

- Personal Access Token

需要从`Github`网站上重新生成Token

- Gist id

> 7f228e0a47090155cb7bb248099f2d53

## 用法

调用如下命令来进行配置文件查看、备份、恢复和检查。

- sync-settings:backup

- sync-settings:restore

- sync-settings:view-backup

- sync-settings:check-backup

- sync-settings:fork

# 软件更新

将软件的自动更新关闭。**今后有大版本出来，或是使用过程中碰到软件缺陷的时候才作版本更新**，要不然跟随版本更新的操作太耗时了。
