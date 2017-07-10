---
title: Jupyter Notebook使用笔记

tags: tips
---

`Jupyter Notebook` 是一个很方便的学习、研究和文档撰写平台。通过这两天的研究，已经初步掌握了其日常的用法。通过在 `Markdown` 文档中嵌入 `Python` 的脚本，可以通过后者来生成动态的图片、表格，甚至还可以增加一些动态的交互效果。

## 设置主页目录

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

Enjoy！
