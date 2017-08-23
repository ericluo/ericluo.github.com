---
title: Windows配置
tags: sa Windows
permalink: /docs/windows/
---

Windows上进行软件开发一直都是种种坑，但是现在的办公环境只能是在Windows下。因此，再苦再难也要克服啊！本文专治Windows平台上的不服，着力打造一个顺手的研究和学习环境。

{% include toc title='文章大纲' %}

# 工具软件

- KeyTweak（主要用于将<kbd>Caps</kbd>映射为<kbd>Ctrl</kbd>)

- 搜狗输入法

- Snagit

  可以从其官网上下载安装最新版（13），注册码如下：

  - FFC2M-Z59RE-QLACP-C5MBV-M8RMB
  - 3KDPC-35ADD-CVG2U-5XU6C-MF3AF
  - 3AHYA-EMM5P-FTAYS-C9HMP-Y639E
  - HLADM-6UL48-27WA4-C9HH5-L326C
  - HML6E-CZMVY-QNY3C-CSAFH-AEC35
  - DQTXN-6JDSD-ZNDDP-CQAKH-AAAMC
  - 6BANC-FN3C4-DACAW-AMXHS-D5C3C

- 微信

- 7-zip

- Adobe Reader

- 百度网盘

- 迅雷下载

- WPS

# 编辑器(`Atom`)

编辑器使用`Atom`，安装好编辑器后，首先安装的插件是`sync-settings`，相关的设置可以参考README文件。接下来就可以通过该插件来同步不同计算机之间的个性化设置信息了。

# Git

## 下载`Git`的客户端软件

## 做好`Git`相关设置

如`user.email`,`user.name`,   `core.quotepath`等相关配置项，其中最后一个配置项用于解决`EDITMSG`中的中文文件名乱码问题，配置如下：

> git config --global core.quotepath false

## 配置ssh key

一种比较简单的方法是通过下载`GitHub Desktop`客户端，其自动会在`Home\.ssh\`目录下生成对应的私钥，并自动在`GitHub`上设置好了对应的公钥。那么我们只需将`.ssh`目录中的文件`github_rsa`复制并更名为`id_rsa`文件即可。这样就可以通过命令行来访问`GitHub`上的项目了。

# 图床设置

七牛提供了免费的云存储空间。在利用`GitHub Pages`搭建个人主页时，图片是不方便存储在`GitHub`上的，那么利用七牛提供的存储空间不仅有利于提高基于`git`操作的速度，而且七牛提供的 `CDN`可以加快页面的访问速度。

## 安装七牛同步客户端

七牛提供了`qrsbox`和`qrsboxcli`两个工具来辅助将本地文件同步到七牛的云存储上，其中前者是一个图形化工具，需要每次自己手动同步，后者提供了命令行工具，可以将其加入的自动任务，在电脑启动后自动执行。

## 在本地同步文件夹中保存图片文件

将本地截屏文件保存至同步文件夹中。在`windows`环境下，可以将同步文件夹设置在`OneDrive`目录下，这样不同桌面计算机的同步文件夹可以保存一致。

## 通过七牛`URL`来访问图片文件

在blog或文章中可以通过Qiniu的URL (http://7xonmk.com1.z0.glb.clouddn.com/) 来访问同步文件夹中对应的图片文件了。

## 使用说明

详细使用说明参见[API/SDK/命令行工具问题](https://support.qiniu.com/question/category?id=69503&categoryTitle=%E5%AF%B9%E8%B1%A1%E5%AD%98%E5%82%A8&forumTitle=API%2FSDK%20%2F%20%E5%91%BD%E4%BB%A4%E8%A1%8C%E5%B7%A5%E5%85%B7%E9%97%AE%E9%A2%98)

### 七牛同步客户端设置

使用七牛提供的同步客户端用于本地和云储存数据的同步，方便云存储的使用。将改同步客户端设置为开机自动启动即可。具体方法如下：

> 将`qrsbox.exe`文件的快捷方式添加至`C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp`目录下


# Ruby及相关软件

使用`GitHub Pages`来写文章需要依赖于`Ruby`。在`windows`平台上安装`Ruby`最方便的方法是通过`chocolate`工具，下载及安装方法参见 [https://chocolatey.org/install](https://chocolatey.org/install)。需要注意的是在安装之间需要用管理员身份开启`Powershell`，并且正确设置执行脚本的权限：

>  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned

然后，就可以使用`choco`来安装`ruby`相关的程序和packages了，[Jekyll on Windows](https://jekyllrb.com/docs/windows/#installation)

## 疑难问题

- SSL CERTIFICATE UPDATES

  `gem`安装过程中会碰到ssl cert相关问题时，需要对rubygems进行更新，参见http://guides.rubygems.org/ssl-certificate-update/#installing-using-update-packages

# Python

安装`Python`可以通过`Anaconda`软件包来完成。

# 股票软件

主要有看行情的同花顺和用于交易的平安证券、银河证券等。

# 无障碍上网

GFW的限制，导致很多网站无法访问，也造成了很多应用工具使用不正常，如`gist`, `gmail`等。今天发现了一个好用的翻墙软件 [蓝灯(Lantern)](https://github.com/getlantern/forum)，可以替代'更换host文件'等阶段性有效的方法和工具。
