# 原创
：  了解Shell环境

# 了解Shell环境

## shell 环境

大多数程序用配置文件来存储程序设置， 一些程序会根据环境变量来调整他们的行为。shell 在环境中存储了两种基本类型的数据：Shell 变量是 bash 存放的少量数据，剩下的都是 环境变量。另外还有别名和 shell 函数。

```
printenv - 打印部分或所有的环境变量
set - 设置 shell 选项
export — 导出环境变量，让随后执行的程序知道。
alias - 创建命令别名

```

### 检查环境变量

```
# printenv 命令也能够列出特定变量的数值
alien@localhost:~$  printenv USER
alien
# echo 命令来查看一个变量的内容
alien@localhost:~$ echo $HOME
/home/alien

```

别名无法通过使用 set 或 printenv 来查看。 用不带参数的 alias 来查看别名:

```
alien@localhost:~$ alias
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] &amp;&amp; echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&amp;|]\s*alert$//'\'')"'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'
alias grep='grep --color=auto'
alias l='ls -CF'
alias la='ls -A'
alias ll='ls -alF'
alias ls='ls --color=auto'

```

<th align="center">环境变量</th>|内容
|------
<td align="center">DISPLAY</td>|如果你正在运行图形界面环境，那么这个变量就是你显示器的名字。通常，它是 “:0”， 意思是由 X 产生的第一个显示器。
<td align="center">EDITOR</td>|文本编辑器的名字。
<td align="center">SHELL</td>|shell 程序的名字。
<td align="center">HOME</td>|用户家目录。
<td align="center">LANG</td>|定义了字符集以及语言编码方式。
<td align="center">OLD_PWD</td>|先前的工作目录。
<td align="center">PAGER</td>|页输出程序的名字。这经常设置为/usr/bin/less。
<td align="center">PATH</td>|由冒号分开的目录列表，当你输入可执行程序名后，会搜索这个目录列表。
<td align="center">PS1</td>|Prompt String 1. 这个定义了你的 shell 提示符的内容。随后我们可以看到，这个变量 内容可以全面地定制。
<td align="center">PWD</td>|当前工作目录。
<td align="center">TERM</td>|终端类型名。类 Unix 的系统支持许多终端协议；这个变量设置你的终端仿真器所用的协议。
<td align="center">TZ</td>|指定你所在的时区。大多数类 Unix 的系统按照协调时间时 (UTC) 来维护计算机内部的时钟 ，然后应用一个由这个变量指定的偏差来显示本地时间。
<td align="center">USER</td>|你的用户名

### 建立shell 环境

登录 shell 会读取一个或多个启动文件----虚拟控制台会话：

|文件|内容
|------
|/etc/profile|应用于所有用户的全局配置脚本。
|~/.bash_profile|用户个人的启动文件。可以用来扩展或重写全局配置脚本中的设置。
|~/.bash_login|如果文件 ~/.bash_profile 没有找到，bash 会尝试读取这个脚本。
|~/.profile|如果文件 ~/.bash_profile 或文件 ~/.bash_login 都没有找到，bash 会试图读取这个文件。 这是基于 Debian 发行版的默认设置，比方说 Ubuntu。

非登录 shell 会话会读取以下启动文件----GUI：

|文件|内容
|------
|/etc/bash.bashrc|应用于所有用户的全局配置文件。
|~/.bashrc|用户个人的启动文件。可以用来扩展或重写全局配置脚本中的设置。

除了读取以上启动文件之外，非登录 shell 会话也会继承它们父进程的环境设置，通常是一个登录 shell。

```
alien@localhost:~$ cat .bashrc
# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac
...

```

PATH 变量经常（但不总是，依赖于发行版）在 /etc/profile 启动文件中设置，通过这些代码：

```
# 目录 $HOME/bin 就添加到了命令搜索目录列表中
PATH=$PATH:$HOME/bin

```

> 
Tips: 把文本附加到一个变量值的末尾
<pre><code>alien@localhost:~$ foo="This is some"
alien@localhost:~$ echo $foo
This is some
alien@localhost:~$ foo="$foo text.";echo $foo
This is some text.
</code></pre>


`export PATH`：这个 export 命令告诉 shell 让这个 shell 的子进程可以使用 PATH 变量的内容。

### 修改 shell 环境

添加目录到你的 PATH 变量或者是定义额外的环境变量，要把这些更改放置到 .bash_profile 文件中（或者其替代文件中，根据不同的发行版。例如，Ubuntu 使用 .profile 文件）。

对于其它的更改，要放到 .bashrc 文件中。

```
# 别名
alien@localhost:~$ ll
总用量 332
drwxrwxrwx 35 alien alien  4096 9月  18 22:32 ./
drwxr-xr-x  3 root  root   4096 11月 29  2017 ../
...

```

```
# 强迫 bash 重新读取修改过的 .bashrc 文件，使用下面的命令：
source .bashrc

```

## 自定义Shell提示符

提示符是由一个环境变量定义的，叫做 PS1（是“prompt string one” 的简写）

```
alien@localhost:~$ echo $PS1
\[\e]0;\u@\h: \w\a\]${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$

```

具体的修改详见：[https://billie66.github.io/TLCL/book/chap14.html](https://billie66.github.io/TLCL/book/chap14.html) ，这方面不需要了解。
