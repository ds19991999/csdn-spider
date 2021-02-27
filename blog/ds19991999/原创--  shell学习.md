# 原创
：  shell学习

# shell学习

### 文章目录

## 一、什么是 shell

“bash” 是 “Bourne Again SHell” 的首字母缩写， 所指的是这样一个事实，bash 是最初 Unix 上由 Steve Bourne 写成 shell 程序 sh 的增强版。能够访问Shell的终端仿真器称为“terminal”。

如果终端提示符的最后一个字符是“#”, 而不是“$”, 那么这个终端会话就有超级用户权限。 这意味着，我们或者是以 root 用户的身份登录，或者是我们选择的终端仿真器提供超级用户（管理员）权限。

许多 Linux 发行版默认保存最后输入的`500`个命令。 按下下箭头按键，先前输入的命令就消失了。鼠标中键拷贝高亮的文本到光标所在的位置。

### 简单命令

`date;cal;df;free;exit`

```
alien@localhost:~$ date
2018年 09月 16日 星期日 10:29:55 CST
alien@localhost:~$ cal
      九月 2018         
日 一 二 三 四 五 六  
                   1  
 2  3  4  5  6  7  8  
 9 10 11 12 13 14 15  
16 17 18 19 20 21 22  
23 24 25 26 27 28 29  
30                    
alien@localhost:~$ df
文件系统           1K-块     已用     可用 已用% 挂载点
udev             1947612        0  1947612    0% /dev
tmpfs             394980     6452   388528    2% /run
/dev/sda10      25357412  7711332 16334952   33% /
tmpfs            1974892    68392  1906500    4% /dev/shm
tmpfs               5120        4     5116    1% /run/lock
tmpfs            1974892        0  1974892    0% /sys/fs/cgroup
tmpfs             394980       84   394896    1% /run/user/1000
/dev/sda6      133953532 88401188 45552344   66% /media/alien/File Sharing
alien@localhost:~$ free
              total        used        free      shared  buff/cache   available
Mem:        3949784     1415584      983500      271940     1550700     1975800
Swap:       4102140           0     4102140
alien@localhost:~$ exit

```

### 幕后控制台

即使终端仿真器没有运行，在后台仍然有几个终端会话运行着。它们叫做虚拟终端 或者是虚拟控制台。在大多数 `Linux` 发行版中，这些终端会话都可以通过按下 `Ctrl-Alt-F1 到 Ctrl-Alt-F6` 访问。当一个会话被访问的时候， 它会显示登录提示框，我们需要输入用户名和密码。要从一个虚拟控制台转换到另一个， 按下 Alt 和 F1-F6(中的一个)。返回图形桌面，按下 `Alt-F7`。

## 二、文件系统中的跳转

```
pwd - Print name of current working directory
cd - Change directory
ls - List directory contents

```

当我们首次登录系统（或者启动终端仿真器会话）后，当前工作目录是我们的家目录。 每个用户都有他自己的家目录，当用户以普通用户的身份操控系统时，家目录是唯一 允许用户写入文件的地方。

### 绝对路径

绝对路径开始于根目录，紧跟着目录树的一个个分支，一直到达所期望的目录或文件。

```
alien@localhost:~$ cd /usr/bin
alien@localhost:/usr/bin$ pwd
/usr/bin

```

### 相对路径

相对路径开始于工作目录，， 我们在文件系统树中用一对特殊符号来表示相对位置。 这对特殊符号是 “.” (点) 和 “…” (点点)。符号 “.” 指的是**工作目录**，”…” 指的是**工作目录的父目录**。在几乎所有的情况下，你可以省略”./”。它是隐含的。

|快捷键|运行结果
|------
|cd|更改工作目录到你的家目录。
|cd -|更改工作目录到先前的工作目录。
|cd ~user_name|更改工作目录到用户家目录。例如, cd ~bob 会更改工作目录到用户“bob”的家目录。

`ls -a` 命令可以列出以 “.” 字符开头的隐藏文件，一些应用程序会把它们的配置文件以隐藏文件的形式放在你的家目录下面，**文件名和命令名是大小写敏感的**。

## 三、探究操作系统

```
ls – List directory contents
file – Determine file type
less – View file contents

```

### ls

ls 可以列出多个目录：

```
alien@localhost:~$ ls ~ /usr
/home/alien:
app           examples.desktop  sys             公共的  视频  文档  音乐
Calibre 书库  PycharmProjects   VirtualBox VMs  模板    图片  下载  桌面

/usr:
bin  games  include  lib  lib64  local  locale  sbin  share  src

```

**ls常用命令选项：**

<th align="center">选项</th><th align="left">长选项</th><th align="left">描述</th>
|------
<td align="center">**-a**</td><td align="left">–all</td><td align="left">列出所有文件，甚至包括文件名以圆点开头的默认会被隐藏的**隐藏文件**。</td>
<td align="center">-d</td><td align="left">–directory</td><td align="left">通常，如果指定了目录名，ls 命令会列出这个目录中的内容，而不是目录本身。 把这个选项与 -l 选项结合使用，可以看到所指定目录的详细信息，而不是目录中的内容。</td>
<td align="center">-F</td><td align="left">–classify</td><td align="left">这个选项会在每个所列出的名字后面加上一个指示符。例如，如果名字是 目录名，则会加上一个’/'字符。</td>
<td align="center">**-h**</td><td align="left">–human-readable</td><td align="left">当以长格式列出时，以人们可读的格式，自适应使用K，M等单位，而不是以字节数来显示文件的大小。</td>
<td align="center">**-l**</td><td align="left">以长格式显示结果。</td>
<td align="center">-r</td><td align="left">–reverse</td><td align="left">以相反的顺序来显示结果。通常，ls 命令的输出结果按照字母升序排列。</td>
<td align="center">-S</td><td align="left">命令输出结果**按照文件大小来排序**。</td>
<td align="center">**-t**</td><td align="left">**按照修改时间来排序**。</td>

```
加上长选项 “–reverse”，则结果会以相反的顺序输出：
$ ls -lt --reverse

```

### 长格式输出

```
alien@localhost:~$ ls -l
总用量 64
drwxrwxr-x  3 alien alien 4096 9月  15 21:19 app
drwxrwxr-x 10 alien alien 4096 4月  12 17:25 Calibre 书库
-rw-r--r--  1 alien alien 8980 11月 29  2017 examples.desktop
drwxrwxr-x  3 alien alien 4096 9月  15 15:30 PycharmProjects
drwxrwxr-x  2 alien alien 4096 9月  16 20:23 sys
drwxrwxr-x  2 alien alien 4096 9月  16 20:49 VirtualBox VMs
drwxr-xr-x  2 alien alien 4096 11月 30  2017 公共的
drwxr-xr-x  2 alien alien 4096 11月 30  2017 模板
drwxr-xr-x  2 alien alien 4096 11月 30  2017 视频
drwxr-xr-x  2 alien alien 4096 9月  15 22:52 图片
drwxr-xr-x  2 alien alien 4096 11月 30  2017 文档
drwxr-xr-x  2 alien alien 4096 12月  8  2017 下载
drwxr-xr-x  3 alien alien 4096 11月 30  2017 音乐
drwxr-xr-x  5 alien alien 4096 9月  17 08:10 桌面

```

|字段|含义
|------
|-rw-r–r--|对于文件的访问权限。**第一个字符指明文件类型。在不同类型之间， 开头的“－”说明是一个普通文件，“d”表明是一个目录**。其后三个字符是**文件所有者**的 访问权限，再其后的三个字符是**文件所属组中成员**的访问权限，最后三个字符是**其他所 有人的访问权限**。也就是一共十个字符。
|1|文件的**硬链接**数目。
|alien|文件所有者的用户名。
|alien|文件所属用户组的名字。
|8980|以字节数表示的文件大小。
|11月 29 2017|上次修改文件的时间和日期。
|examples.desktop|文件名。

### 确定文件类型

```
file filename

```

Linux 中，有个普遍的观念就是“一切皆文件”。

### 用 less 浏览文件内容

许多包含系统设置的文件（叫做配置文件），是以文本格式存储的，实际程序（叫做脚本）也是以这种格式存储的。

```
# less 程序允许你前后滚动文件
less filename
# 按下“q”键， 退出 less 程序

```

**less参数：**

|命令|行为
|------
|Page **UP** or **b**|向上翻滚一页
|Page **Down** or **space**|向下翻滚一页
|UP Arrow|向上翻滚一行
|Down Arrow|向下翻滚一行
|**G**|移动到最后一行
|1G or **g**|移动到开头一行
|/charaters|向前查找指定的字符串
|n|向前查找下一个出现的字符串，这个字符串是之前所指定查找的
|h|显示帮助屏幕
|q|退出 less 程序

### less is more(色即是空)

less 属于”页面调度器”类程序，这些程序允许以**逐页方式**轻松浏览长文本文档。 **more 程序只能向前翻页**，而 less 程序允许前后翻页，此外还有很多其它的特性。

### Linux 系统中的目录

|目录|评论
|------
|/|根目录，万物起源。
|/bin|包含系统启动和运行所必须的二进制程序。
|/boot|包含 Linux 内核、初始 RAM 磁盘映像（用于启动时所需的驱动）和 启动加载程序。有趣的文件：/boot/grub/grub.conf or menu.lst， 被用来配置启动加载程序。/boot/vmlinuz，Linux 内核。
|/dev|这是一个包含设备结点的特殊目录。“一切都是文件”，也适用于设备。 在这个目录里，内核维护着所有设备的列表。
|/etc|这个目录包含所有系统层面的配置文件。它也包含一系列的 shell 脚本， 在系统启动时，这些脚本会开启每个系统服务。这个目录中的任何文件应该是可读的文本文件。有趣的文件：虽然/etc 目录中的任何文件都有趣，但这里只列出了一些我一直喜欢的文件：/etc/crontab， 定义自动运行的任务。/etc/fstab，包含存储设备的列表，以及与他们相关的挂载点。/etc/passwd，包含用户帐号列表。
|/home|在通常的配置环境下，系统会在/home 下，给每个用户分配一个目录。普通用户只能 在自己的目录下写文件。这个限制保护系统免受错误的用户活动破坏。
|/lib|包含核心系统程序所使用的共享库文件。这些文件与 Windows 中的动态链接库相似。
|/lost+found|每个使用 Linux 文件系统的格式化分区或设备，例如 ext3文件系统， 都会有这个目录。当部分恢复一个损坏的文件系统时，会用到这个目录。这个目录应该是空的，除非文件系统 真正的损坏了。
|/media|在现在的 Linux 系统中，/media 目录会包含可移动介质的挂载点， 例如 USB 驱动器，CD-ROMs 等等。这些介质连接到计算机之后，会自动地挂载到这个目录结点下。
|/mnt|在早些的 Linux 系统中，/mnt 目录包含可移动介质的挂载点。
|/opt|这个/opt 目录被用来安装“可选的”软件。这个主要用来存储可能 安装在系统中的商业软件产品。
|/proc|这个/proc 目录很特殊。从存储在硬盘上的文件的意义上说，它不是真正的文件系统。 相反，它是一个由 Linux 内核维护的虚拟文件系统。它所包含的文件是内核的窥视孔。这些文件是可读的， 它们会告诉你内核是怎样监管计算机的。
|/root|root 帐户的家目录。
|/sbin|这个目录包含“系统”二进制文件。它们是完成重大系统任务的程序，通常为超级用户保留。
|/tmp|这个/tmp 目录，是用来存储由各种程序创建的临时文件的地方。一些配置导致系统每次 重新启动时，都会清空这个目录。
|/usr|在 Linux 系统中，/usr 目录可能是最大的一个。它包含普通用户所需要的所有程序和文件。
|/usr/bin|/usr/bin 目录包含系统安装的可执行程序。通常，这个目录会包含许多程序。
|/usr/lib|包含由/usr/bin 目录中的程序所用的共享库。
|/usr/local|这个/usr/local 目录，是非系统发行版自带程序的安装目录。 通常，由源码编译的程序会安装在/usr/local/bin 目录下。新安装的 Linux 系统中会存在这个目录， 并且在管理员安装程序之前，这个目录是空的。
|/usr/sbin|包含许多系统管理程序。
|/usr/share|/usr/share 目录包含许多由/usr/bin 目录中的程序使用的共享数据。 其中包括像默认的配置文件、图标、桌面背景、音频文件等等。
|/usr/share/doc|大多数安装在系统中的软件包会包含一些文档。在/usr/share/doc 目录下， 我们可以找到按照软件包分类的文档。
|/var|除了/tmp 和/home 目录之外，相对来说，目前我们看到的目录是静态的，这是说， 它们的内容不会改变。/var 目录存放的是动态文件。各种数据库，假脱机文件， 用户邮件等等，都位于在这里。
|/var/log|这个/var/log 目录包含日志文件、各种系统活动的记录。这些文件非常重要，并且 应该时时监测它们。其中最重要的一个文件是/var/log/messages。注意，为了系统安全，在一些系统中， 你必须是超级用户才能查看这些日志文件。

### 符号链接（软链接）----与Windows一样

```
lrwxrwxrwx 1 root root 11 2007-08-11 07:34 libc.so.6 -&gt; libc-2.6.so

```

“l”是符号链接（也称为**软链接**或者 symlink ），一个文件被多个文件名所指向，即多个拥有不同文件名的软链接指向同一个文件。上面`libc.so.6`是`libc-2.6.so`的软链接。

### 硬链接

## 四、操作文件和目录

```
cp — 复制文件和目录
mv — 移动/重命名文件和目录
mkdir — 创建目录
rm — 删除文件和目录
ln — 创建硬链接和符号链接

```

命令行程序，功能强大灵活，对于 复杂的文件操作任务，使用命令行程序比较容易完成。

### 通配符

|通配符|意义
|------
|*|匹配任意**多个字符（包括零个或一个）**
|?|匹配任意**一个字符**（不包括零个）
|[characters]|匹配任意一个属于字符集中的字符
|[!characters]|匹配任意一个不是字符集中的字符
|[[:class:]]|匹配任意一个属于**指定字符类**中的字符

**普遍使用的字符类：**

|字符类|意义
|------
|[:alnum:]|匹配任意**一个字母或数字**
|[:alpha:]|匹配任意**一个字母**
|[:digit:]|匹配任意一个**数字**
|[:lower:]|匹配任意一个**小写字母**
|[:upper:]|匹配任意一个**大写字母**

**通配符范例：**

|模式|匹配对象
|------
|*|所有文件
|g*|文件名以“g”开头的文件
|b*.txt|以"b"开头，中间有零个或任意多个字符，并以".txt"结尾的文件
|Data???|以“Data”开头，其后紧接着3个字符的文件
|[abc]*|文件名以"a",“b”,或"c"开头的文件
|BACKUP.[0-9][0-9][0-9]|以"BACKUP."开头，并紧接着3个数字的文件
|[[:upper:]]*|以大写字母开头的文件
|[![:digit:]]*|不以数字开头的文件
|*[[:lower:]123]|文件名以小写字母结尾，或以 “1”，“2”，或 “3” 结尾的文件

避免使用[A-Z]或 [a-z]，用[字符](#%E9%80%9A%E9%85%8D%E7%AC%A6)类来代替它们。

### mkdir - 创建目录

### cp - 复制文件和目录

```
cp item... directory

```

复制多个项目（文件或目录）到一个目录下。

|选项|意义
|------
|-a, --archive|复制文件和目录，以及它们的属性，包括所有权和权限。 通常，复本具有用户所操作文件的默认属性。
|-i, --interactive|在重写已存在文件之前，**提示用户确认**。如果这个选项不指定， cp 命令会**默认重写文件。**
|-r, --recursive|递归地复制目录及目录中的内容。当复制目录时， 需要这个选项（或者-a 选项）。
|-u, --update|当把文件从一个目录复制到另一个目录时，仅复制 目标目录中不存在的文件，或者是文件内容新于目标目录中已经存在的文件。
|-v, --verbose|显示翔实的命令操作信息

**示例：**

<th align="center">命令</th>|运行结果
|------
<td align="center">`cp file1 file2`</td>|复制文件 file1 内容到文件 file2。如果 file2 已经存在， file2 的内容会被 file1 的内容重写。如果 file2 不存在，则会创建 file2。
<td align="center">`cp -i file1 file2`</td>|这条命令和上面的命令一样，除了如果文件 file2 存在的话，在文件 file2 被**重写**之前， 会提示用户确认信息。
<td align="center">`cp file1 file2 dir1`</td>|复制文件 file1 和文件 file2 到目录 dir1。目录 dir1 必须存在。
<td align="center">`cp dir1/* dir2`</td>|使用一个通配符，在目录 dir1 中的所有文件都被复制到目录 dir2 中。 dir2 必须已经存在。
<td align="center">`cp -r dir1 dir2`</td>|复制目录 dir1 中的内容到目录 dir2。如果目录 dir2 不存在， 创建目录 dir2，操作完成后，目录 dir2 中的内容和 dir1 中的一样。 如果目录 dir2 存在，则目录 dir1 (和目录中的内容)将会被复制到 dir2 中。

### mv - 移动和重命名文件

与[cp](#cp - 复制文件和目录)基本一样.

```
mv item... directory

```

|选项|意义
|------
|-i --interactive|在重写一个已经存在的文件之前，提示用户确认信息。 **如果不指定这个选项，mv 命令会默认重写文件内容。**
|-u --update|当把文件从一个目录移动另一个目录时，只是移动不存在的文件， 或者文件内容新于目标目录相对应文件的内容。
|-v --verbose|当操作 mv 命令时，显示翔实的操作信息。

**示例：**

|命令|运行情况
|------
|mv file1 file2|移动 file1 到 file2。**如果 file2 存在，它的内容会被 file1 的内容重写。** 如果 file2 不存在，则创建 file2。 **这两种情况下，file1 都不再存在。**
|mv -i file1 file2|除了如果 file2 存在的话，在 file2 被重写之前，用户会得到 提示信息外，这个和上面的选项一样。
|mv file1 file2 dir1|移动 file1 和 file2 到目录 dir1 中。dir1 必须已经存在。
|mv dir1 dir2|如果目录 dir2 不存在，创建目录 dir2，并且移动目录 dir1 的内容到 目录 dir2 中，同时删除目录 dir1。如果目录 dir2 存在，移动目录 dir1（及它的内容）到目录 dir2。

### rm - 删除文件和目录

```
rm item...

```

|选项|意义
|------
|-i, --interactive|在删除已存在的文件前，提示用户确认信息。 **如果不指定这个选项，rm 会默默地删除文件**
|-r, --recursive|递归地删除文件，这意味着，如果要删除一个目录，而此目录 又包含子目录，那么子目录也会被删除。要删除一个目录，必须指定这个选项。
|-f, --force|忽视不存在的文件，不显示提示信息。这选项覆盖了“–interactive”选项。
|-v, --verbose|在执行 rm 命令时，显示翔实的操作信息。

**示例：**

|命令|运行结果
|------
|rm file1|默默地删除文件
|rm -i file1|除了在删除文件之前，提示用户确认信息之外，和上面的命令作用一样。
|rm -r file1 dir1|删除文件 file1, 目录 dir1，及 dir1 中的内容。
|rm -rf file1 dir1|同上，除了如果文件 file1，或目录 dir1 不存在的话，rm 仍会继续执行。

一般我们可以先用`ls`测试一下要删除的文件，再进行删除操作，防止误删。

### ln — 创建链接

ln 命令既可创建硬链接，也可以创建符号链接（软链接）。

```
# 创建硬链接
ln file link
# 创建符号链接，”item” 可以是一个文件或是一个目录
ln -s item link

```

## 五、使用命令

```
type – 说明怎样解释一个命令名
which – 显示会执行哪个可执行程序
man – 显示命令手册页
apropos – 显示一系列适合的命令
info – 显示命令 info
whatis – 显示一个命令的简洁描述
alias – 创建命令别名

```

命令：可执行程序、内建于 shell 自身的命令、 shell 函数、命令别名

### 识别命令

### 使用命令文档

```
alien@localhost:~$ help cd
cd: cd [-L|[-P [-e]] [-@]] [dir]
    Change the shell working directory.
...

```

**命令文档表示法：<strong>出现在命令语法说明中的方括号，表示**可选的项目</strong>。一个**竖杠字符**表示**互斥选项**。在上面 cd 命令的例子中：cd 命令可能有一个“-L”选项或者“-P”选项，进一步，可能有参数“dir”。

```
alien@localhost:~$ mkdir --help
用法：mkdir [选项]... 目录...
Create the DIRECTORY(ies), if they do not already exist.

```

**手册布局：**

|章节|内容
|------
|1|用户命令
|2|程序接口内核系统调用
|3|C 库函数程序接口
|4|特殊文件，比如说设备结点和驱动程序
|5|文件格式
|6|游戏娱乐，如屏幕保护程序
|7|其他方面
|8|系统管理员命令

有时候，我们需要查看参考手册的特定章节，从而找到我们需要的信息：`man section search_term`，例如：

```
alien@localhost:~$ man 5 passwd

```

```
alien@localhost:~$ apropos floppy
fdformat (8)         - low-level format a floppy disk
mbadblocks (1)       - tests a floppy disk, and marks the bad blocks in the FAT
mformat (1)          - add an MSDOS filesystem to a low-level formatted flopp...
mxtar (1)            - Wrapper for using GNU tar directly from a floppy disk

```

第一个字段是手册页的名字，第二个字段展示章节，man 命令加上”-k”选项， 和 apropos 完成一样的功能。

```
alien@localhost:~$ whatis ls
ls (1)               - list directory contents

```

info 程序读取 info 文件，info 文件是树型结构，分化为各个结点，每一个包含一个题目。 info 文件包含超级链接，它可以让你从一个结点跳到另一个结点。一个超级链接可通过 它开头的星号来辨别出来，把光标放在它上面并按下 enter 键，就可以激活它。

**info命令：**

|命令|行为
|------
|?|显示命令帮助
|PgUp or Backspace|显示上一页
|PgDn or Space|显示下一页
|n|下一个 - 显示下一个结点
|p|上一个 - 显示上一个结点
|u|Up - 显示当前所显示结点的父结点，通常是个菜单
|Enter|激活光标位置下的超级链接
|q|退出

gzip 软件包包括一个特殊的 less 版本，叫做 **zless，zless 可以显示由 gzip 压缩的文本文件的内容**。

### 用别名（alias）创建你自己的命令

> 
tips:把多个命令放在同一行上，命令之间 用”;”分开。`command1; command2; command3...`


```
alien@localhost:~$ type foo
bash: type: foo: 未找到

```

```
alien@localhost:~$ cd /usr; ls; cd -
bin  games  include  lib  lib64  local  locale  sbin  share  src
/home/alien

```

创建命令别名`foo`：

```
alien@localhost:~$ alias foo='cd /usr; ls; cd -'
alien@localhost:~$ alias name='string'
alien@localhost:~$ foo
bin  games  include  lib  lib64  local  locale  sbin  share  src
/home/alien
alien@localhost:~$ type foo
foo 是 `cd /usr; ls; cd -' 的别名

```

删除别名：

```
alien@localhost:~$ unalias foo
alien@localhost:~$ type foo
bash: type: foo: 未找到

```

在命令行中定义别名有点儿小问题。当你的 shell 会话结束时，它们会消失，后面会介绍怎样把自己的别名添加到文件中去，每次我们登录系统，这些文件会建立系统环境。

## 六、重定向 “&gt;” “&lt;”

I/O 重定向。”I/O”代表输入/输出， 通过这个工具，你可以重定向命令的输入输出，命令的输入来自文件，而输出也存到文件。 也可以把多个命令连接起来组成一个强大的命令管道。

```
cat － 连接文件
sort － 排序文本行
uniq － 报道或省略重复行
grep － 打印匹配行
wc － 打印文件中换行符，字，和字节个数
head － 输出文件第一部分
tail - 输出文件最后一部分
tee - 从标准输入读取数据，并同时写到标准输出和文件

```

```
# 这样会重写 ls-output.txt 文件
alien@localhost:~$ ls -l /usr/bin &gt; ls-output.txt
alien@localhost:~$ ls
app               ls-output.txt    VirtualBox VMs  视频  下载
Calibre 书库      PycharmProjects  公共的          图片  音乐
examples.desktop  sys              模板            文档  桌面
alien@localhost:~$ cat ls-output.txt 
总用量 126424
-rwxr-xr-x 1 root root      51920 3月   3  2017 [
lrwxrwxrwx 1 root root          8 11月 24  2017 2to3 -&gt; 2to3-2.7
...

```

注意：ls 程序不把它的错误信息输送到标准输出。

> 
tips：`&gt; ls-output.txt`清空文件内容


### 重定向标准输出和错误到同一个文件

一个程序可以在几个编号的文件流中的任一个上产生输出。这些文件流的前 三个称作标准输入、输出和错误，shell 内部分别将其称为文件描述符0、1和2。

```
alien@localhost:~$ ls -l /bin/usr &gt; ls-output.txt 2&gt;&amp;1
alien@localhost:~$ ls -l /usr/bin &gt;&gt; ls-output.txt 2&gt;&amp;1
alien@localhost:~$ cat ls-output.txt 
ls: 无法访问'/bin/usr': 没有那个文件或目录
总用量 126424
-rwxr-xr-x 1 root root      51920 3月   3  2017 [

```

> 
**标准错误的重定向必须总是出现在标准输出重定向之后**，而且必须是上面这种格式


现在的`bash`版本提供了一种新方法`&amp;&gt;`：`ls -l /bin/usr &amp;&gt; ls-output.txt`

### 处理不需要的输出

隐瞒命令错误信息，我们这样做：

```
alien@localhost:~$ ls -l /bin/usr 2&gt; /dev/null
alien@localhost:~$ 

```

其中`/dev/null`的特殊文件， 是系统设备，叫做**位存储桶**，它可以接受输入，并且对输入不做任何处理。

### 标准输入重定向

**cat 命令读取一个或多个文件，然后复制它们到标准输出。**

> 
tips: 创建一个叫做”lazy_dog.txt” 的文件：
<pre><code>alien@localhost:~$ cat &gt; lazy_dog.txt
The quick brown fox jumped over the lazy dog.
alien@localhost:~$ cat lazy_dog.txt 
The quick brown fox jumped over the lazy dog.
# Ctrl+d退出
</code></pre>


**重定向标准输入：**把标准输入源从键盘改到文件 lazy_dog.tx。

```
alien@localhost:~$ cat &lt; lazy_dog.txt 
The quick brown fox jumped over the lazy dog.

```

### 管道线`|`

`command1 | command2`一个命令的标准输出可以通过管道送至另一个命令的标准输入：`$ ls -l /usr/bin | less`

**过滤器:**

把几个命令放在一起组成一个管道线，以这种方式使用的命令被称为过滤器。

```
alien@localhost:~$ ls /bin /usr/bin | sort | less

```

我们指定了两个目录（/bin 和/usr/bin），ls 命令的输出结果由有序列表组成， 各自针对一个目录。通过在管道线中包含 sort，我们改变输出数据，从而产生一个 有序列表。

**uniq - 忽略重复行**

uniq 从标准输入或单个文件名参数接受数据有序列表默认情况下，从数据列表中删除任何重复行。

```
 ls /bin /usr/bin | sort | uniq | less

```

如果想看到重复的数据列表，加上”-d”选项，就像这样：`ls /bin /usr/bin | sort | uniq -d | less`

### `wc--grep--head--tail--tee`

**wc － 打印行数、字数(单词数)和字节数**，`-l`选项限制命令输出只能 报道行数。

```
alien@localhost:~$ wc ls-output.txt
  3617  34113 232078 ls-output.txt
alien@localhost:~$ ls /bin /usr/bin | sort | uniq | wc -l
1957

```

**grep － 打印匹配行**

`grep pattern [file...]`，当 grep 遇到一个文件中的匹配”模式”，它会打印出包含这个类型的行，这里再次强调了[正则表达式](https://blog.csdn.net/ds19991999/article/category/7887554)的重要性。

```
# 找到文件名中包含单词”zip”的所有文
alien@localhost:~$ ls /bin /usr/bin | sort | uniq | grep zip
bunzip2
bzip2
...

```

grep中的”-i”使得 grep 在执行搜索时忽略大小写（通常，搜索是大小写 敏感的），”-v”选项会告诉 grep 只打印不匹配的行。

**head / tail － 打印文件开头部分/结尾部分**

head 命令打印文件的前十行，而 tail 命令打印文件的后十行。默认情况下，两个命令 都打印十行文本，但是可以通过”-n”选项来调整命令打印的行数。

```
alien@localhost:~$ head -n 3 ls-output.txt
ls: 无法访问'/bin/usr': 没有那个文件或目录
总用量 126424
-rwxr-xr-x 1 root root      51920 3月   3  2017 [
alien@localhost:~$ tail -n 3 ls-output.txt
-rwxr-xr-x 1 root root      81840 8月  17  2015 zipsplit
-rwxr-xr-x 1 root root      27064 4月   7  2016 zjsdecode
-rwxr-xr-x 1 root root      10336 5月   2 21:42 zlib-flate
alien@localhost:~$ ls /usr/bin | tail -n 3
zipsplit
zjsdecode
zlib-flate
alien@localhost:~$ 

```

**tee － 从 Stdin 读取数据，并同时输出到 Stdout 和文件**

```
alien@localhost:~$ ls /usr/bin | tee ls.txt | grep zip
funzip
gpg-zip
mzip
preunzip
prezip
prezip-bin
unzip
unzipsfx
zip
zipcloak
zipdetails
zipgrep
zipinfo
zipnote
zipsplit
alien@localhost:~$ cat ls.txt 
[
2to3
2to3-2.7
2to3-3.5

```

## 七、走进Shell

```
echo － 显示一行文本

```

### echo展开

**(字符)展开：**

一个简单的字符序列”*”，通过展开， 你输入的字符，在 shell 对它起作用之前，会展开成为别的字符。

```
alien@localhost:~$ echo this is a test
this is a test
alien@localhost:~$ echo *
app Calibre 书库 examples.desktop lazy_dog.txt ls-output-1.txt ls-output.txt ls.txt PycharmProjects sys test.txt VirtualBox VMs 公共的 模板 视频 图片 文档 下载 音乐 桌面
alien@localhost:~$ 

```

关于[通配符](#%E9%80%9A%E9%85%8D%E7%AC%A6)，看上面的介绍。 shell 在 echo 命 令被执行前把 `*` 展开成了另外的东西（在这里，就是在当前工作目录下的文件名字）当回车键被按下时，shell 在命令被执行前在命令行上自动展开任何符合条件的字符， 所以 echo 命令的实际参数并不是”*“，而是它展开后的结果。

**路径名展开:**

通配符所依赖的工作机制叫做路径名展开.

```
alien@localhost:~$ ls
app               ls-output-1.txt  sys             模板  下载
Calibre 书库      ls-output.txt    test.txt        视频  音乐
examples.desktop  ls.txt           VirtualBox VMs  图片  桌面
lazy_dog.txt      PycharmProjects  公共的          文档
alien@localhost:~$ echo ls*
ls-output-1.txt ls-output.txt ls.txt
alien@localhost:~$ echo *t
lazy_dog.txt ls-output-1.txt ls-output.txt ls.txt test.txt

```

**显示隐藏文件：**

```
# 不能包含以多个圆点开头的文件名
alien@localhost:~$ echo .[!.]?*
.adobe .atom .bash_history .bash_logout .bashrc .bashrc.swl .bashrc.swm .bashrc.swn .bashrc.swo .bashrc.swp .cache .compiz .config .dbus .dmrc 
...
alien@localhost:~$ ls -d .[!.]?*
.adobe         .compiz        .java        .PyCharmCE2016.3
.atom          .config        .jupyter     .python_history
.bash_history  .dbus          .kingsoft    .remarkable
...
# 显示所有文件
alien@localhost:~$ ls -A
.adobe            .gnome            .python_history
app               .gnupg            .remarkable
...

```

**算术表达式展开:**

```
alien@localhost:~$ echo $((2 + 2))
4
alien@localhost:~$ echo $(($((5**2)) * 3))
75
alien@localhost:~$ echo $(((5**2) * 3))
75

```

算术表达式空格并不重要，表达式可以嵌套，只支持整数（全部是**数字，不带小数点**），但是能执行很多不同的操作。

|操作符|说明
|------
|+|加
|-|减
|*|乘
|/|除（但是记住，因为展开只是支持整数除法，所以结果是整数。）
|%|取余，只是简单的意味着，“余数”
|**|取幂

**花括号展开：**

```
alien@localhost:~$ echo Front-{A,B,C}-Back
Front-A-Back Front-B-Back Front-C-Back
alien@localhost:~$ echo Number_{1..5}
Number_1 Number_2 Number_3 Number_4 Number_5
alien@localhost:~$ echo a{A{1,2},B{3,4}}b
aA1b aA2b aB3b aB4b

```

括号展开模式可能包含一个开头部分叫做报头，一个结尾部分叫做附言。

```
alien@localhost:~$ mkdir Pics
alien@localhost:~$ cd Pics/
alien@localhost:~/Pics$ mkdir {2007..2009}-0{1..9} {2007..2009}-{10..12}
alien@localhost:~/Pics$ ls
2007-01  2007-05  2007-09  2008-01  2008-05  2008-09  2009-01  2009-05  2009-09
2007-02  2007-06  2007-10  2008-02  2008-06  2008-10  2009-02  2009-06  2009-10
2007-03  2007-07  2007-11  2008-03  2008-07  2008-11  2009-03  2009-07  2009-11
2007-04  2007-08  2007-12  2008-04  2008-08  2008-12  2009-04  2009-08  2009-12

```

**参数展开：**

```
alien@localhost:~$ echo $USER
alien
# 查看有效的变量列表
alien@localhost:~$ printenv | less

```

### 命令替换

命令替换允许我们把一个命令的输出作为一个展开模式来使用：

```
# 在不知道 cp 命令 完整路径名的情况下得到它的文件属性列表
alien@localhost:~$ ls -l $(which cp)
-rwxr-xr-x 1 root root 151024 3月   3  2017 /bin/cp
alien@localhost:~$ ls -l `which cp`
-rwxr-xr-x 1 root root 151024 3月   3  2017 /bin/cp
# 管道线的输出结果成为 file 命令的参数列表
alien@localhost:~$ file $(ls /usr/bin/* | grep zip)
/usr/bin/funzip:     ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=06412c648a6927c4a14c751fe2412db3425ecd0f, stripped
...

```

### 引用–控制展开

`\`是转义字符，经常在双引号中使用转义字符，来有选择地阻止展开。

```
# shell 利用单词分割删除掉 echo 命令的参数列表中多余的空格
alien@localhost:~$ echo this is a    test
this is a test
# 参数展开把 $1 的值替换为一个空字符串
alien@localhost:~$ echo The total is $100.00
The total is 00.00

```

双引号中的文本都失去它们的特殊含义，单词分割被禁止，内嵌的空格也不会被当作界定符，它们成为参数的一部分，一对双引号里的内容就是一个参数的命令。

```
alien@localhost:~$ cat two\ words.txt 
hhh
alien@localhost:~$ cat two words.txt 
cat: two: 没有那个文件或目录
cat: words.txt: 没有那个文件或目录
alien@localhost:~$ cat "two words.txt"
hhh
alien@localhost:~$ cat two\ words.txt 
hhh
alien@localhost:~$ mv "two words.txt" two_words.txt 

```

> 
在双引号中，参数展开、算术表达式展开和命令替换仍然有效


```
alien@localhost:~$ echo "$USER $((2+2)) $(cal)"
alien 4       九月 2018         
日 一 二 三 四 五 六  
                   1  
 2  3  4  5  6  7  8 
 ....

```

```
# 38个参数
alien@localhost:~$ echo $(cal)
九月 2018 日 一 二 三 四 五 六 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
# 只有一个参数
alien@localhost:~$ echo "$(cal)"
      九月 2018         
日 一 二 三 四 五 六  
                   1  
 2  3  4  5  6  7  8  
 9 10 11 12 13 14 15  
16 17 18 19 20 21 22  
23 24 25 26 27 28 29  
30  

```

> 
**单引号禁止所有的展开**


|转义序列|含义
|------
|\a|响铃（”警告”－导致计算机嘟嘟响）
|\b|退格符
|\n|新的一行。在类 Unix 系统中，产生换行。
|\r|回车符
|\t|制表符

echo 命令带上 ‘-e’ 选项，能够解释转义序列。**展开和引用**在Linux系统中使用非常频繁，这是shell的重要特性 。

## 八、键盘高级操作技巧

```
clear － 清空屏幕
history － 显示历史列表内容

```

### 快捷键

**移动光标：**

<th align="center">按键</th>|行动
|------
<td align="center">Ctrl-a</td>|移动光标到行首。
<td align="center">Ctrl-e</td>|移动光标到行尾。
<td align="center">Ctrl-f</td>|光标前移一个字符；和右箭头作用一样。
<td align="center">Ctrl-b</td>|光标后移一个字符；和左箭头作用一样。
<td align="center">Alt-f</td>|光标前移一个字。
<td align="center">Alt-b</td>|光标后移一个字。
<td align="center">Ctrl-l</td>|清空屏幕，移动光标到左上角。clear 命令完成同样的工作。

**修改文本:**

|按键|行动
|------
|Ctrl-d|删除光标位置的字符。
|Ctrl-t|光标位置的字符和光标前面的字符互换位置。
|Alt-t|光标位置的字和其前面的字互换位置。
|Alt-l|把从光标位置到字尾的字符转换成小写字母。
|Alt-u|把从光标位置到字尾的字符转换成大写字母。

**剪切和粘贴文本:**

|按键|行动
|------
|Ctrl-k|剪切从光标位置到行尾的文本。
|Ctrl-u|剪切从光标位置到行首的文本。
|Alt-d|剪切从光标位置到词尾的文本。
|Alt-Backspace|剪切从光标位置到词头的文本。如果光标在一个单词的开头，剪切前一个单词。
|Ctrl-y|把剪切环中的文本粘贴到光标位置。

**利用历史命令：**

```
# `.bash_history` 的文件存放历史命令
alien@localhost:~$ ls .bash*
.bash_history  .bashrc      .bashrc.swm  .bashrc.swo
.bash_logout   .bashrc.swl  .bashrc.swn  .bashrc.swp
alien@localhost:~$ history | less

```

```
# 找出和/usr/bin这一目录相关的命令
alien@localhost:~$ history | grep /usr/bin
  786  cd /usr/bin
  793  cd /usr/bin
  903  ls -l /usr/bin &gt; ls-output.txt
  933  ls -l /usr/bin &gt;&gt; ls-output.txt 2&gt;&amp;1
  936  ls -l /usr/bin &gt;&gt; ls-output.txt 2&gt;&amp;1
  937  ls -l /usr/bin &gt;&gt; ls-output-1.txt 2&gt;&amp;1
  946  ls -l /usr/bin | less
...

```

`Ctrl-r`:历史命令反向增量搜索，匹配到命令行按`enter`执行，`Ctrl-j`复制。

|序列|行为
|------
|!!|重复最后一次执行的命令。可能按下上箭头按键和 enter 键更容易些。
|!number|重复历史列表中第 number 行的命令。
|!string|重复最近历史列表中，以这个字符串开头的命令。
|!?string|重复最近历史列表中，包含这个字符串的命令。

## 九、权限

```
id – 显示用户身份号
chmod – 更改文件模式
umask – 设置默认的文件权限
su – 以另一个用户的身份来运行 shell
sudo – 以另一个用户的身份来执行命令
chown – 更改文件所有者
chgrp – 更改文件组所有权
passwd – 更改用户密码

```

```
alien@localhost:~$ id
uid=1000(alien) gid=1000(alien) 组=1000(alien),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),113(lpadmin),128(sambashare)

```

当用户创建帐户之后，系统会给用户分配一个号码，叫做用户 ID 或者 uid，这个 ID 映射到一个用户名。系统又会给这个用户分配一个原始的组 ID 或者是 gid，这个 gid 可能属于另外的组。

用户帐户 定义在`/etc/passwd`文件里面，用户组定义在`/etc/group` 文件里面。当用户帐户和用户组创建以后， 这些文件随着文件`/etc/shadow`的变动而修改，文件`/etc/shadow`包含了关于用户密码的信息。 对于每个用户帐号，文件`/etc/passwd` 定义了`用户（登录）名、uid、gid、帐号的真实姓名、家目录 和登录 shell`。

```
alien@localhost:~$ touch foo.txt
alien@localhost:~$ ls -l foo.txt 
-rw-rw-r-- 1 alien alien 0 9月  18 16:04 foo.txt

```

**文件类型：**

<th align="center">属性</th>|文件类型
|------
<td align="center">-</td>|一个普通文件
<td align="center">d</td>|一个目录
<td align="center">l</td>|一个符号链接。注意对于符号链接文件，剩余的文件属性总是"rwxrwxrwx"，而且都是 虚拟值。真正的文件属性是指符号链接所指向的文件的属性。
<td align="center">c</td>|一个字符设备文件。这种文件类型是指按照字节流来处理数据的设备。 比如说终端机或者调制解调器
<td align="center">b</td>|一个块设备文件。这种文件类型是指按照数据块来处理数据的设备，例如一个硬盘或者 CD-ROM 盘。

后面九个字符代表着**文件所有者、文件组所有者和其他人**的读、写和执行权限。

|属性|文件|目录
|------
|r|允许打开并读取文件内容。|允许列出目录中的内容，前提是目录必须设置了可执行属性（x）。
|w|允许写入文件内容或截断文件。但是不允许对文件进行重命名或删除，重命名或删除是由目录的属性决定的。|允许在目录下新建、删除或重命名文件，前提是目录必须设置了可执行属性（x）。
|x|允许将文件作为程序来执行，使用脚本语言编写的程序必须设置为可读才能被执行。|允许进入目录，例如：cd directory 。

### chmod － 更改文件权限

chmod 命令支持两种不同的方法来改变文件模式：八进制数字表示法或 符号表示法。

**八进制数字表示法：**

|Octal|Binary|File Mode
|------
|0|000|—
|1|001|–x
|2|010|-w-
|3|011|-wx
|4|100|r–
|5|101|r-x
|6|110|rw-
|7|111|rwx

```
alien@localhost:~$ ls -l foo.txt 
-rw-rw-r-- 1 alien alien 0 9月  18 16:04 foo.txt
alien@localhost:~$ chmod 777 foo.txt 
alien@localhost:~$ ls -l foo.txt 
-rwxrwxrwx 1 alien alien 0 9月  18 16:04 foo.txt
# u+rw、g-w等等
alien@localhost:~$ chmod g-rwx foo.txt 
alien@localhost:~$ ls -l foo.txt 
-rwx---rwx 1 alien alien 0 9月  18 16:04 foo.txt

```

**符号表示法：**

如果没有指定字符，则假定使用”all”。

|u|"user"的简写，意思是文件或目录的所有者。
|------
|g|用户组。
|o|"others"的简写，意思是其他所有的人。
|a|“all"的简写，是"u”, "g"和“o”三者的联合。

### umask － 设置默认权限

|Original file mode|— rw- rw- rw-
|------
|Mask|000 000 000 010
|Result|— rw- rw- r–

掩码是八进制，转换为二进制后，若出现一个数字1，则删除文件模式中和这个1在相同位置的属性

### 更改身份

```
注销系统并以其他用户身份重新登录系统。
使用 su 命令。
使用 sudo 命令。

```

su 命令用来以另一个用户的身份来启动 shell：`su [-[l]] [user]`，如果包含”-l”或者"-"选项，那么会为指定用户启动一个需要登录的 shell，并且工作目录会更改到这个用户的家目录。如果不指定用户，那么就假定是超级用户。

```
alien@localhost:~$ su
密码： 
root@localhost:/home/alien# exit
exit
alien@localhost:~$ su -l
密码： 
root@localhost:~# exit
注销
alien@localhost:~$ su -
密码： 
root@localhost:~# exit
注销

```

```
# 查看sudo 命令可以授予哪些权限
alien@localhost:~$ sudo -l
匹配 %2$s 上 %1$s 的默认条目：
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

用户 alien 可以在 localhost 上运行以下命令：
    (ALL : ALL) ALL

```

### chown － 更改文件所有者和用户组

```
alien@localhost:~$ su
密码： 
root@localhost:/home/alien# chown [owner][:[group]] file...

```

第一个参数更改文件所有者和/或文件用户组，第二个参数是文件或文件夹

|参数|结果
|------
|bob|把文件所有者从当前属主更改为用户 bob。
|bob:users|把文件所有者改为用户 bob，文件用户组改为用户组 users。
|:admins|把文件用户组改为组 admins，文件所有者不变。
|bob:|文件所有者改为用户 bob，文件用户组改为用户 bob 登录系统时所属的用户组。

### 更改用户密码

`passwd [user]`

## 十、进程

```
ps – 报告当前进程快照
top – 显示任务
jobs – 列出活跃的任务
bg – 把一个任务放到后台执行
fg – 把一个任务放到前台执行
kill – 给一个进程发送信号
killall – 杀死指定名字的进程
shutdown – 关机或重启系统

```

### ps查看进程

```
alien@localhost:~$ ps
  PID TTY          TIME CMD
27867 pts/3    00:00:00 bash
28091 pts/3    00:00:00 ps

```

TTY 是指进程的控制终端默，TIME 字段表示 进程所消耗的 CPU 时间数量。认情况下，ps 不会显示很多进程信息，只是列出与当前终端会话相关的进程.

```
alien@localhost:~$ ps x
  PID TTY      STAT   TIME COMMAND
 1148 ?        Ss     0:00 /lib/systemd/systemd --user
 1150 ?        S      0:00 (sd-pam)
 ...

```

STAT 是 “state” 的简写，它揭示了进程当前状态。进程状态信息之后，可能还跟随其他的字符。这表示各种外来进程的特性。

|状态|含义
|------
|R|运行中。这意味着，进程正在运行或准备运行。
|S|正在睡眠。进程没有运行，而是，正在等待一个事件， 比如说，一个按键或者网络分组。
|D|不可中断睡眠。进程正在等待 I/O，比方说，一个磁盘驱动器的 I/O。
|T|已停止. 已经指示进程停止运行。稍后介绍更多。
|Z|一个死进程或“僵尸”进程。这是一个已经终止的子进程，但是它的父进程还没有清空它。 （父进程没有把子进程从进程表中删除）
|&lt;|一个高优先级进程。这可能会授予一个进程更多重要的资源，给它更多的 CPU 时间。 进程的这种属性叫做 niceness。具有高优先级的进程据说是不好的（less nice）， 因为它占用了比较多的 CPU 时间，这样就给其它进程留下很少时间。
|N|低优先级进程。 一个低优先级进程（一个“nice”进程）只有当其它高优先级进程被服务了之后，才会得到处理器时间。

```
# 这个选项组合，能够显示属于每个用户的进程信息
alien@localhost:~$ ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.1 185460  4748 ?        Ss   11:25   0:01 /sbin/init spla
root         2  0.0  0.0      0     0 ?        S    11:25   0:00 [kthreadd]
...

```

<th align="center">标题</th>|含义
|------
<td align="center">USER</td>|用户 ID. 进程的所有者。
<td align="center">%CPU</td>|以百分比表示的 CPU 使用率
<td align="center">%MEM</td>|以百分比表示的内存使用率
<td align="center">VSZ</td>|虚拟内存大小
<td align="center">RSS</td>|进程占用的物理内存的大小，以千字节为单位。
<td align="center">START</td>|进程启动的时间。若它的值超过24小时，则用天表示。

### top动态查看进程

```
# 默认情况下，每三秒钟更新一次,top 显示结果由两部分组成： 最上面是系统概要，下面是进程列表，以 CPU 的使用率排序。
alien@localhost:~$ top

top - 17:24:44 up  5:59,  1 user,  load average: 0.56, 0.81, 0.63
Tasks: 222 total,   1 running, 221 sleeping,   0 stopped,   0 zombie
%Cpu(s):  9.3 us,  2.7 sy,  0.0 ni, 87.8 id,  0.2 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem :  3949784 total,  1227196 free,  1562828 used,  1159760 buff/cache
KiB Swap:  4102140 total,  3583672 free,   518468 used.  1768020 avail Mem 

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND                                                      
  870 root      20   0  413888  53400  36872 S  10.3  1.4  12:43.43 Xorg  
...

```

**系统概要含义：**

<th align="center">行号</th><th align="center">字段</th>|意义
|------
<td align="center">1</td><td align="center">top</td>|程序名。
<td align="center">14:59:20</td>|当前时间。
<td align="center">up 6:30</td>|这是正常运行时间。它是计算机从上次启动到现在所运行的时间。 在这个例子里，系统已经运行了六个半小时。
<td align="center">2 users</td>|有两个用户登录系统。
<td align="center">load average:</td>|加载平均值是指，等待运行的进程数目，也就是说，处于可以运行状态并共享 CPU 的进程个数。 这里展示了三个数值，每个数值对应不同的时间段。第一个是最后60秒的平均值， 下一个是前5分钟的平均值，最后一个是前15分钟的平均值。若平均值低于1.0，则指示计算机 工作不忙碌。
<td align="center">2</td><td align="center">Tasks:</td>|总结了进程数目和这些进程的各种状态。
<td align="center">3</td><td align="center">Cpu(s):</td>|这一行描述了 CPU 正在进行的活动的特性。
<td align="center">0.7%us</td>|0.7% 的 CPU 被用于用户进程。这意味着进程在内核之外。
<td align="center">1.0%sy</td>|1.0%的 CPU 时间被用于系统（内核）进程。
<td align="center">0.0%ni</td>|0.0%的 CPU 时间被用于"nice"（低优先级）进程。
<td align="center">98.3%id</td>|98.3%的 CPU 时间是空闲的。
<td align="center">0.0%wa</td>|0.0%的 CPU 时间来等待 I/O。
<td align="center">4</td><td align="center">Mem:</td>|展示物理内存的使用情况。
<td align="center">5</td><td align="center">Swap:</td>|展示交换分区（虚拟内存）的使用情况。

top 程序接受一系列从键盘输入的命令。两个最有趣的命令是 h 和 q。h，显示程序的帮助屏幕，q， 退出 top 程序。

### 控制进程

```
alien@localhost:~$ xlogo &amp;
[1] 30167
alien@localhost:~$ ps
  PID TTY          TIME CMD
29939 pts/2    00:00:00 bash
30167 pts/2    00:00:00 xlogo
30169 pts/2    00:00:00 ps

```

执行 jobs 命令，列出从我们终端中启动了的任务。

```
alien@localhost:~$ xlogo &amp;
[1] 30691
alien@localhost:~$ jobs
[1]+  运行中               xlogo &amp;
alien@localhost:~$ fg %1
xlogo
^C
alien@localhost:~$ 

```

**为什么要从命令行启动一个图形界面程序呢？**有两个原因。第一个，你想要启动的程序，可能 没有在窗口管理器的菜单中列出来（比方说 xlogo）。第二个，从命令行启动一个程序， 你能够看到一些错误信息，如果从图形界面中运行程序的话，这些信息是不可见的。

```
alien@localhost:~$ xlogo &amp;
[1] 31254
alien@localhost:~$ kill %1

```

`kill [-signal] PID...`：如果在命令行中没有指定信号，那么默认情况下，发送 TERM（Terminate，终止）信号。kill 命令被经常 用来发送以下命令：

<th align="center">编号</th><th align="center">名字</th>|含义
|------
<td align="center">1</td><td align="center">HUP</td>|挂起（Hangup）。这是美好往昔的残留部分，那时候终端机通过电话线和调制解调器连接到 远端的计算机。这个信号被用来告诉程序，控制的终端机已经“挂断”。 通过关闭一个终端会话，可以展示这个信号的作用。在当前终端运行的前台程序将会收到这个信号并终止。许多守护进程也使用这个信号，来重新初始化。这意味着，当一个守护进程收到这个信号后， 这个进程会重新启动，并且重新读取它的配置文件。Apache 网络服务器守护进程就是一个例子。
<td align="center">2</td><td align="center">INT</td>|中断。实现和 Ctrl-c 一样的功能，由终端发送。通常，它会终止一个程序。
<td align="center">9</td><td align="center">KILL</td>|杀死。这个信号很特别。尽管程序可能会选择不同的方式来处理发送给它的 信号，其中也包含忽略信号，但是 KILL 信号从不被发送到目标程序。而是内核立即终止 这个进程。当一个进程以这种方式终止的时候，它没有机会去做些“清理”工作，或者是保存工作。 因为这个原因，把 KILL 信号看作最后一招，当其它终止信号失败后，再使用它。
<td align="center">15</td><td align="center">TERM</td>|终止。这是 kill 命令发送的默认信号。如果程序仍然“活着”，可以接受信号，那么 这个它会终止。
<td align="center">18</td><td align="center">CONT</td>|继续。在一个停止信号后，这个信号会恢复进程的运行。
<td align="center">19</td><td align="center">STOP</td>|停止。这个信号导致进程停止运行，而不是终止。像 KILL 信号，它不被 发送到目标进程，因此它不能被忽略。

> 
信号既可以用号码，也可以用名字来指定，可以用 jobspec（例如，“％1”）来代替 PID。


**其它常用信号：**

<th align="center">编号</th><th align="center">名字</th>|含义
|------
<td align="center">3</td><td align="center">QUIT</td>|退出
<td align="center">11</td><td align="center">SEGV</td>|段错误(Segmentation Violation)。如果一个程序非法使用内存，就会发送这个信号。也就是说， 程序试图写入内存，而这个内存空间是不允许此程序写入的。
<td align="center">20</td><td align="center">TSTP</td>|终端停止(Terminal Stop)。当按下 Ctrl-z 组合键后，终端发送这个信号。不像 STOP 信号， TSTP 信号由目标进程接收，且可能被忽略。
<td align="center">28</td><td align="center">WINCH</td>|改变窗口大小(Window Change)。当改变窗口大小时，系统会发送这个信号。 一些程序，像 top 和 less 程序会响应这个信号，按照新窗口的尺寸，刷新显示的内容。

**完整的信号列表：**

```
alien@localhost:~$ kill -l
 1) SIGHUP	 2) SIGINT	 3) SIGQUIT	 4) SIGILL	 5) SIGTRAP
 6) SIGABRT	 7) SIGBUS	 8) SIGFPE	 9) SIGKILL	10) SIGUSR1
11) SIGSEGV	12) SIGUSR2	13) SIGPIPE	14) SIGALRM	15) SIGTERM
16) SIGSTKFLT	17) SIGCHLD	18) SIGCONT	19) SIGSTOP	20) SIGTSTP
21) SIGTTIN	22) SIGTTOU	23) SIGURG	24) SIGXCPU	25) SIGXFSZ
26) SIGVTALRM	27) SIGPROF	28) SIGWINCH	29) SIGIO	30) SIGPWR
31) SIGSYS	34) SIGRTMIN	35) SIGRTMIN+1	36) SIGRTMIN+2	37) SIGRTMIN+3
38) SIGRTMIN+4	39) SIGRTMIN+5	40) SIGRTMIN+6	41) SIGRTMIN+7	42) SIGRTMIN+8
43) SIGRTMIN+9	44) SIGRTMIN+10	45) SIGRTMIN+11	46) SIGRTMIN+12	47) SIGRTMIN+13
48) SIGRTMIN+14	49) SIGRTMIN+15	50) SIGRTMAX-14	51) SIGRTMAX-13	52) SIGRTMAX-12
53) SIGRTMAX-11	54) SIGRTMAX-10	55) SIGRTMAX-9	56) SIGRTMAX-8	57) SIGRTMAX-7
58) SIGRTMAX-6	59) SIGRTMAX-5	60) SIGRTMAX-4	61) SIGRTMAX-3	62) SIGRTMAX-2
63) SIGRTMAX-1	64) SIGRTMAX	

```

### killall给多个进程发送信号

```
killall [-u user] [-signal] name...

```

```
alien@localhost:~$ xlogo &amp;
[1] 31816
alien@localhost:~$ xlogo &amp;
[2] 31817
alien@localhost:~$ killall xlogo
alien@localhost:~$ 

```

### 更多和进程相关的命令

|命令名|命令描述
|------
|pstree|输出一个树型结构的进程列表(processtree)，这个列表展示了进程间父/子关系。
|vmstat|输出一个系统资源使用快照，包括内存，交换分区和磁盘 I/O。 为了看到连续的显示结果，则在命令名后加上更新操作延时的时间（以秒为单位）。例如，“vmstat 5”。 ，按下 Ctrl-c 组合键, 终止输出。
|xload|一个图形界面程序，可以画出系统负载随时间变化的图形。
|tload|terminal load与 xload 程序相似，但是在终端中画出图形。使用 Ctrl-c，来终止输出。

**至此，`Shell`算是了解了一些基本概念，路还很长，后续继续更新…**
