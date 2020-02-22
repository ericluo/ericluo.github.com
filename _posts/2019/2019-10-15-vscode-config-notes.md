---
title: "VSCode Configuration"
---

今天开始使用 `VSCode` 来替代 `Atom` 作为日常工作的编辑器和编程工具。相比较而言，前者速度更快，功能更强大，而且插件生态也更丰富。更加重要的是其插件下载平台没有被 `GFW`，因此下载安装插件会更快，不需要考虑网关代理等烦人的问题。

替换为 `VSCode` 后，碰到了搜狗输入法中烦人的快捷键设置问题，外加其夹带的不堪其扰的弹出广告，终于下决心将输入法替换为百度输入法，目前使用效果良好。

## 主要插件

- Python
- ~~Markdown All in One~~ 
- Markdown Preview Github + Markdown Footnotes + Markdown Math
- markdownlint
- Emoji
- Calculator
- GitLens
- Prettier
- vscode-icons
- scratchpad
- Excel to markdown table           # copy from excel, paste to markdown table
- Picgo                             # upload picture to clound
- TabOut                            # tab key to out of {}, (), "",<>,etc

## 字体设置

在 `vscode` 中，默认配置下英文使用等宽字体，但中文使用宋体。中英文字体不等宽，导致在中英文混排时无法对齐，特别是在 `markdown` 中使用到表格时显示效果很差。

可以通过使用 [`Sarasa Mono`](https://github.com/be5invis/Sarasa-Gothic) 字体来解决这个问题。下载并安装对应简体中文字体(`sarasa-term-sc`)后，在 `Settings` 中进行如下设置即可：

> font-family: 'Sarasa Term SC',Consolas, 'Courier New', monospace

**对应的有 `Sarasa Mono Sc` 和 `Sarasa Term SC` 两种字体可以安装和设置，会有部分差异。可以根据实际情况进行调整。**

## 键盘快捷键设置

`vscode` 提供了方便的快捷键设置功能。打开快捷键设置界面，在输入栏中输入对应的按键或功能，查询到对应的快捷键设置列表，并对目标快捷键设定进行编辑修订或删除操作。

## Picgo 设置

尝试过多种解决方案后，还是觉得阿里云是目前最成熟的。安装 `Picgo` 插件后，进行如下 4 个参数设置，就可以在 `vscode` 中直接使用快捷键 `Ctrl + Alt + U` 来上传图片到图床（阿里云）上了。

- Access Key ID:
- Access Key Secret:
- Area: oss-cn-beijing
- bucket: netimages

## VIM

### 输入法

在 `VIM` 插件中，在切换到 `Normal` 模式时，能自动切换到英文输入法的状态，并在进入 `Insert` 模式时，自动恢复为切换前的输入法。可以通过如下步骤实现：

1. 安装 `im-select`，下载安装 `im-select.exe` 命令行软件，用于动态设置和切换输入法。

2. 在 `VIM` 插件中进行配置

```json
  "vim.autoSwitchInputMethod.enable": true,
  "vim.autoSwitchInputMethod.defaultIM": "1033",
  "vim.autoSwitchInputMethod.obtainIMCmd": "D:\\bin\\im-select.exe",
  "vim.autoSwitchInputMethod.switchIMCmd": "D:\\bin\\im-select.exe {im}",
```

### 快捷键

`VIM` 中的部分快捷键与 `VSCode` 相同，特别是 `Ctrl-` 类的快捷键。本着能用尽用 `VSCode` 原生功能和快捷键的原则，将 `VIM` 中的部分 `Ctrl-` 类快捷键禁用。

```json
  "vim.handleKeys": {
      "<C-a>": false,
      "<C-b>": false,
      "<C-c>": false,
      "<C-d>": false,
      "<C-f>": false,
      "<C-k>": false,
      "<C-t>": false,
  },
```
