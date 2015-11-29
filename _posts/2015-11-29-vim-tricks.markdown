---
layout: post
title: VIM 学习笔记
---

`VIM` 的最佳使用原则是 **执行、重复、回退** ，在使用 `VIM` 的过程中，要时刻注意有没有应用这个原则了简化编辑工作的机会。

 Dot Formula
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

