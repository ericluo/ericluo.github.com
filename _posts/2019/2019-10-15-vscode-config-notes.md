---
title: "VSCode Configuration"
---

今天开始使用 `VSCode` 来替代 `Atom` 作为日常工作的编辑器和编程工具。相比较而言，前者速度更快，功能更强大，而且插件生态也更丰富。更加重要的是其插件下载平台没有被 `GFW`，因此下载安装插件会更快，不需要考虑网关代理等烦人的问题。

替换为 `VSCode` 后，碰到了搜狗输入法中烦人的快捷键设置问题，外加其夹带的不堪其扰的弹出广告，终于下决心将输入法替换为百度输入法，目前使用效果良好。

## 主要插件

- Python
- Vim
- Markdown
- Emoji
- markdownlint
- Prettier
- vscode-icons

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
