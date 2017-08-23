---
permalink: /docs/git/
tags: git
---

## 中文文件名乱码

参考以下的设置，在CygWin中git log内容已可正常使用、显示中文，但git status和push、pull时，中文文件名仍然乱码，不知如何解决，如:

```bash
[/data/soft/xstarcd.github.io]$git status
位于分支 master
您的分支与上游分支 'origin/master' 一致。
未跟踪的文件:
  （使用 "git add <文件>..." 以包含要提交的内容）

        "\346\265\213\350\257\225.txt"

提交为空，但是存在尚未跟踪的文件（使用 "git add" 建立跟踪）
```

解决方式：

```bash
#不对0x80以上的字符进行quote，解决git status/commit时中文文件名乱码
git config --global core.quotepath false
```
