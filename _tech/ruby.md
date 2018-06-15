---
tags: ruby
permalink: /tech/ruby/
---

## ruby安装与环境设置

- 安装Ruby

  在<https://rubyinstaller.org/>上下载最新版（当前为2.4.1）的`ruby`安装包。该安装包安装完成后会自动提示下载对应的`msys2`（其用于编译相关的gems)。

- `gems`的安装

  第一个安装的`gems`是`bundler`,安装后切换路径到对应的项目路径下，安装项目相关的`gems`

  ```bash
  gem install bundler
  cd $prjoect_home$
  bundle update
  ```
## jekyll无法本地预览中文文件问题的解决

对`ruby`安装路径中的`webrick/httpservlet/filehandler.rb`文件打补丁：

```ruby
  # position 1
  path = req.path_info.dup.force_encoding(Encoding.find("filesystem"))
  + path.force_encoding("UTF-8") # 加入编码
  if trailing_pathsep?(req.path_info)

  # positon 2
  break if base == "/"
  + base.force_encoding("UTF-8") #加入編碼
  break unless File.directory?(File.expand_path(res.filename + base))
```
