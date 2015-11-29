---
layout: post
title: VIM 学习笔记
---

`VIM` 的最佳使用原则是 **执行、重复、回退** ，在使用 `VIM` 的过程中，要时刻注意有没有应用这个原则了简化编辑工作的机会。

`Dot Formula`
: One Keystroke to move, One Keystroke to Execute


|----------------------------------+-----------------------+--------+---------+------|
| Intent                           | Act                   | Repeat | Reverse | mode |
|----------------------------------+-----------------------+:------:+:-------:+------|
| Make a change                    | {edit}                |    .   |    u    |      |
| Scan line for next character     | f{char}/t{char}       |    ;   |    ,    |      |
| Scan line for previous character | F{char}/T{char}       |    ;   |    ,    |      |
| Scan document for next match     | /pattern<CR>          |    n   |    N    |      |
| Scan document for previous match | ?pattern<CR>          |    n   |    N    |      |
| Perform substitution             | :s/target/replacement |    &   |    u    |      |
| Execute a sequence of changes    | qx{changes}q          |   @x   |    u    |      |
|----------------------------------+-----------------------+--------+---------+------|

# Modes

## Normal mode

*撤销*命令的粒度由从 `normal mode` 进入 `insert mode`，然后在恢复到 `Normal mode` 决定。期间对文档变更作为一个整体 (`chunk`) 。

**注意：如果在 `insert mode` 下，使用了上下左右的方向键移动光标位置，将视作退回了 `Normal mode` ，并使用 `h,j,k,l` 来移动。**

因此，在编辑过程中，应该尽可能按照思维粒度来决定返回 `Normal mode` 的时机，从而一次思维过程可以作为一个可撤销单元。

### Vim's Operator commands

| Trigger | Effect                                            |
|---------+---------------------------------------------------|
| c       | Change                                            |
| d       | Delete                                            |
| y       | Yank into register                                |
| g~      | Swap case                                         |
| gu      | Make lowercase                                    |
| gU      | Make uppercase                                    |
| >       | Shift right                                       |
| <       | Shift left                                        |
| =       | Autoindent                                        |
| !       | Filter {motion} lines through an external program |
|---------+---------------------------------------------------|

#### Vim's Grammer

> Operator + Motion = Action

> When an operator is invoked in duplicate, it acts upon the current line.


## Insert mode

| Keystrokes           | Effect                                                 |
|----------------------+--------------------------------------------------------|
| `<C-h>`              | Delete back one character (backspace)                  |
| `<C-w>`              | Delete back one word                                   |
| `<C-u>`              | Delete back to start of line                           |
| `<C-r>{register}`    | Paste text from {register}                             |
| `<C-r>=`             | Paste return from expression register                  |
|----------------------+--------------------------------------------------------|
| `<C-v>{123}`         | Insert character by decimal code                       |
| `<C-v>u{1234}`       | Insert character by hexadecimal code                   |
| `<C-v>{nondigit}     | Insert nondigit literally                              |
| `<C-k>{char1}{char2} | Insert character represented by {char1}{char2} digraph |
|----------------------+--------------------------------------------------------|
| `<Esc>`              | Switch to Normal mode                                  |
| `<C-[>`              | Switch to Normal mode                                  |
| `<C-o>`              | Switch to Insert Normal mode[^1]                       |
|----------------------+--------------------------------------------------------|

## Visual mode

## Command-Line Mode




[^1]: 用于在 `Insert mode` 下临时性地调用一次 `Normal mode` 命令，然后在返回 `Insert mode`。
