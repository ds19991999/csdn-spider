# 原创
：  第一个Shell脚本

# 第一个Shell脚本

## 第一个Shell脚本

### hello_world脚本

编写一个 Shell 脚本：**编写一个脚本**、**使脚本文件可执行**、**把脚本放置到 shell 能够找到的地方**

```
#!/bin/bash
# This is our first script.
# 保存为hello_world
echo 'Hello World!'

```

`#!`字符序列是一种特殊的结构叫做`shebang`。 这个 `shebang` 被用来告诉**操作系统将执行此脚本所用的解释器的名字**。

对于脚本文件，有两个常见的权限设置；权限为755的脚本，则每个人都能执行，和权限为700的 脚本，只有文件所有者能够执行。设置好权限之后就可运行了:`./hello_world`

```
alien@localhost:~ $ echo $PATH
/home/alien/.nvm/versions/node/v8.12.0/bin:/home/alien/bin:/home/alien/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin

```

上面的路径相当于windows中的环境变量。

```
# 添加环境变量
alien@localhost:~ $ export PATH=~/bin:"$PATH"
alien@localhost:~ $ . .bashrc

```

这个点（.）命令是 source 命令的同义词，一个 shell 内建命令，用来读取一个指定的 shell 命令文件， 并把它看作是从键盘中输入的一样，`.bashrc`文件存放了环境变量。

### 脚本书写规范

```
ls -ad
ls --all --directory

```

```
find playground \( -type f -not -perm 0600 -exec chmod 0600 ‘{}’ ‘;’ \) -or \( -type d -not -perm 0711 -exec chmod 0711 ‘{}’ ‘;’ \)

```

这样的长命令，可以展开，提高可读性：

```
find playground \
    \( \
        -type f \
        -not -perm 0600 \
        -exec chmod 0600 ‘{}’ ‘;’ \
    \) \
    -or \
    \( \
        -type d \
        -not -perm 0711 \
        -exec chmod 0711 ‘{}’ ‘;’ \
    \)

```

**变量和常量：**

```
#!/bin/bash
# Program to output a system information page
# 创建了一个title变量
title="System Information Report"
echo "&lt;HTML&gt;
        &lt;HEAD&gt;
                &lt;TITLE&gt;$title&lt;/TITLE&gt;
        &lt;/HEAD&gt;
        &lt;BODY&gt;
                &lt;H1&gt;$title&lt;/H1&gt;
        &lt;/BODY&gt;
&lt;/HTML&gt;"

```

变量名规则：
1. 变量名可由字母数字字符（字母和数字）和下划线字符组成。1. 变量名的第一个字符必须是一个字母或一个下划线。1. 变量名中不允许出现空格和标点符号。1. Shell惯例是指定大写字母来表示常量，小写字母表示真正的变量
Shell可以使用带有-r（只读）选项的内部命令 declare， 来强制常量的不变性。

```
declare -r TITLE=”Page Title”

```

```
variable=value

```

variable是变量的名字，value是一个字符串，shell 不会 在乎变量值的类型；它把它们都看作是字符串。通过使用带有-i 选项的 declare 命令，你可以强制 shell 把 赋值限制为整数。

赋值过程中，变量名、等号和变量值之间必须没有空格。可以在同一行中对多个变量赋值。

here document 或者 here script也是一种文本输出方法，here document 是另外一种 I/O 重定向形式。

```
command &lt;&lt; token
text
token

```

我们 在脚本文件中嵌入正文文本，然后把它发送给一个命令的标准输入。command 是一个可以接受标准输入的命令名，token 是一个用来指示嵌入文本**结束**的字符串。here documents 中的**单引号和双引号**会失去它们在 shell 中的特殊含义，把它们看作是普通的字符。如果我们把重定向操作符从 “&lt;&lt;” 改为 “&lt;&lt;-”，shell 会**忽略在此 here document 中开头的 tab 字符**。 这就能缩进一个 here document，从而提高脚本的可读性。

## 自顶向下设计

先确定上层步骤，然后再逐步细化这些步骤的过程被称为自顶向下设计。开发一个报告产生器脚本：

步骤7和8之间添加一些额外的任务：

shell 函数是位于其它脚本中的“微脚本”，作为自主程序。Shell 函数有两种语法形式：

```
# name 是函数名，commands 是一系列包含在函数中的命令
# 在脚本中 shell 函数定义必须出现在函数调用之前。
function name {
    commands
    return
}
and
name () {
    commands
    return
}

```

局部变量允许与已存在的变量名相同，这些变量可以是全局变量， 或者是其它 shell 函数中的局部变量，却不必担心潜在的名字冲突。

```
#!/bin/bash
# Program to output a system information page
TITLE="System Information Report For $HOSTNAME"
CURRENT_TIME=$(date +"%x %r %Z")
TIME_STAMP="Generated $CURRENT_TIME, by $USER"

report_uptime () {
  cat &lt;&lt;- _EOF_
  &lt;H2&gt;System Uptime&lt;/H2&gt;
  &lt;PRE&gt;$(uptime)&lt;/PRE&gt;
_EOF_
  return
}

report_disk_space () {
  cat &lt;&lt;- _EOF_
  &lt;H2&gt;Disk Space Utilization&lt;/H2&gt;
  &lt;PRE&gt;$(df -h)&lt;/PRE&gt;
_EOF_
  return
}
report_home_space () {
  cat &lt;&lt;- _EOF_
  &lt;H2&gt;Home Space Utilization&lt;/H2&gt;
  &lt;PRE&gt;$(du -sh /home/*)&lt;/PRE&gt;
_EOF_
  return
}
cat &lt;&lt; _EOF_
&lt;HTML&gt;
    &lt;HEAD&gt;
        &lt;TITLE&gt;$TITLE&lt;/TITLE&gt;
    &lt;/HEAD&gt;
    &lt;BODY&gt;
        &lt;H1&gt;$TITLE&lt;/H1&gt;
        &lt;P&gt;$TIME_STAMP&lt;/P&gt;
        $(report_uptime)
        $(report_disk_space)
        $(report_home_space)
    &lt;/BODY&gt;
&lt;/HTML&gt;
_EOF_

```

保存为testtest：
