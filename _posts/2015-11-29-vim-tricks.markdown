---
layout: post
title: VIM 学习笔记
---

* 主要内容
{:toc}

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

# VIM应用技巧

## Vim 输入法切换

在插入模式的时候如果使用的是中文输入法，想回到正常模式，这时候按ESC是不管用的，因为键都让输入法捕获了。你必须先手动切换成英文输入法才能正常使用VIM的键盘命令。

加入下面这两行配置，可以让你简单地按ESC就回到正常模式，而不需要手动切换为英文输入法：

{% highlight vim %}
au InsertEnter * set noimdisable
au InsertLeave * set imdisable
{% endhighlight %}

注意：如果再进入插入模式会自动切换到正常模式之前的输入法。

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

| Keystrokes            | Effect                                                 |
|-----------------------+--------------------------------------------------------|
| `<C-h>`               | Delete back one character (backspace)                  |
| `<C-w>`               | Delete back one word                                   |
| `<C-u>`               | Delete back to start of line                           |
| `<C-r>{register}`     | Paste text from {register}                             |
| `<C-r>=`              | Paste return from expression register                  |
|-----------------------+--------------------------------------------------------|
| `<C-v>{123}`          | Insert character by decimal code                       |
| `<C-v>u{1234}`        | Insert character by hexadecimal code                   |
| `<C-v>{nondigit}`     | Insert nondigit literally                              |
| `<C-k>{char1}{char2}` | Insert character represented by {char1}{char2} digraph |
|-----------------------+--------------------------------------------------------|
| `<Esc>`               | Switch to Normal mode                                  |
| `<C-[>`               | Switch to Normal mode                                  |
| `<C-o>`               | Switch to Insert Normal mode[^1]                       |
|-----------------------+--------------------------------------------------------|

[^1]: 用于在 `Insert mode` 下临时性地调用一次 `Normal mode` 命令，然后在返回 `Insert mode`。

## Visual mode

## Command-Line(Ex) Mode

> Ex commands Strike Far and Wide

在该模式中可以使用类似于 `bash` 中的快捷键进行命令的编辑。主要可以使用的命令有：

| Keystrokes    | Effect           |
| ------------  | ---------------- |
| C-u           | 撤销全行内容     |
| C-w           | 撤销前一个单词   |
| C-a           | 跳到行首         |
| C-e           | 跳到行尾         |
| C-r{register} | 插入寄存器内容   |
| C-r C-w       | 插入当前位置单词 |

### Ex Commands

| Keystrokes                                    | Effect                                                                          |
|-----------------------------------------------+---------------------------------------------------------------------------------|
| :[range]delete [x]                            | delete lines into register x                                                    |
| :[range]yank [x]                              | yank specified lines [into register x]                                          |
| :[line]put [x]                                | put the text from register x after the specified line                           |
| :[range]copy {address}                        | copy specified lines to below the line specified by {address}                   |
| :[range]move {address}                        | move specified lines to below the line specified by {address}                   |
| :[range]join                                  | join the specified lines                                                        |
| :[range]normal {commands}                     | execute Normal mode {commands} with {string} on each specified line             |
| :[range]substitute/{pattern}/{string}/[flags] | replace occurrences of {pattern} with {string} on each specified line           |
| :[range]global/{pattern}/[cmd]                | execute the Ex command [cmd] on all specified lines where the {pattern} matches |
|-----------------------------------------------+---------------------------------------------------------------------------------|

使用 `q:` 可以进入 `Command line window` 模式。

# Registers

| name                | register |
|---------------------+----------|
| Unnamed Registers   | ""       |
| Yank Registers      | "0       |
| Named Registers     | "a - "z  |
| Black Hole Register | "_       |
| Expression register | "=       |
| Search register     | "/       |
| System Clipboard    | "+       |

# Patterns

## Substitution

## Global Commands

# Tools

## ctags

## quickfix

> At any given moment, there can be only one quickfix list, but we can create as many location lists as we want.
> Location list is bound to the currently active window, quickfix list is available throughtout Vim.

* Quickfix List
    : :make, :grep, :vimgrep use the quickfix list
* Location List
    : :lmake, :lgrep, :lvimgrep use the location list

## grep

## autocompletion
