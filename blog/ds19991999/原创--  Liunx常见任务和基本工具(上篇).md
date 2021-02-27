# 原创
：  Liunx常见任务和基本工具(上篇)

# Liunx常见任务和基本工具(上篇)

### 文章目录

## 一、软件包管理

**主要的包管理系统家族：**

|包管理系统|发行版 (部分列表)
|------
|Debian Style (.deb)|Debian, Ubuntu, Xandros, Linspire
|Red Hat Style (.rpm)|Fedora, CentOS, Red Hat Enterprise Linux, OpenSUSE, Mandriva, PCLinuxOS

如果一个软件包需要一些共享的资源，如一个动态链接库，它就被称作有一个**依赖**。软件包管理系统通常由两种工具类型组成：**底层工具**用来处理这些任务，比方说安装和删除软件包文件；**上层工具**，完成元数据搜索和依赖解析。

**包管理工具：**

|发行版|底层工具|上层工具
|------
|Debian-Style|dpkg|apt-get, aptitude
|Fedora, Red Hat Enterprise Linux, CentOS|rpm|yum

**使用上层工具来搜索资源库元数据，可以根据软件包的名字和说明来定位它：**

|风格|命令
|------
|Debian|apt-get update; apt-cache search search_string
|Red Hat|yum search search_string

**上层工具允许从一个资源库中下载一个软件包，并经过完全依赖解析来安装它：**

|风格|命令
|------
|Debian|apt-get update; apt-get install package_name
|Red Hat|yum install package_name

**底层软件包安装命令：**

|风格|命令
|------
|Debian|dpkg --install package_file
|Red Hat|rpm -i package_file

**使用上层工具来卸载软件：**

|风格|命令
|------
|Debian|apt-get remove package_name
|Red Hat|yum erase package_name

**上层工具软件包更新命令：**

|风格|命令
|------
|Debian|apt-get update; apt-get upgrade
|Red Hat|yum update

**底层软件包升级命令：**

|风格|命令
|------
|Debian|dpkg --install package_file
|Red Hat|rpm -U package_file

**列出所安装的软件包：**

|风格|命令
|------
|Debian|dpkg --list
|Red Hat|rpm -qa

**底端工具可以用来显示是否安装了一个指定的软件包：**

|风格|命令
|------
|Debian|dpkg --status package_name
|Red Hat|rpm -q package_name

**查看软件包信息：**

|风格|命令
|------
|Debian|apt-cache show package_name
|Red Hat|yum info package_name

**确定哪个软件包对所安装的某个特殊文件负责：**

|风格|命令
|------
|Debian|dpkg --search file_name
|Red Hat|rpm -qf file_name

## 二、存储媒介

```
mount – 挂载一个文件系统
umount – 卸载一个文件系统
fsck – 检查和修复一个文件系统
fdisk – 分区表控制器
mkfs – 创建文件系统
fdformat – 格式化一张软盘
dd — 把面向块的数据直接写入设备
genisoimage (mkisofs) – 创建一个 ISO 9660的映像文件
wodim (cdrecord) – 把数据写入光存储媒介
md5sum – 计算 MD5检验码

```

### 挂载和卸载存储设备

管理存储设备的第一步是把设备连接到文件系统树中，即挂载。有一个叫做`/etc/fstab`的文件可以列出系统启动时要挂载的设备（典型地，硬盘分区）。

Fedora 7系统的/etc/fstab 文件实例：

```
LABEL=/12               /               ext3        defaults        1   1
LABEL=/home             /home           ext3        defaults        1   2
LABEL=/boot             /boot           ext3        defaults        1   2

```

字段说明：

|字段|内容|说明
|------
|1|设备名|传统上，这个字段包含与物理设备相关联的设备文件的实际名字，比如说/dev/hda1（第一个 IDE 通道上第一个主设备分区）。然而今天的计算机，有很多热插拔设备（像 USB 驱动设备），许多 现代的 Linux 发行版用一个文本标签和设备相关联。当这个设备连接到系统中时， 这个标签（当储存媒介格式化时，这个标签会被添加到存储媒介中）会被操作系统读取。 那样的话，不管赋给实际物理设备哪个设备文件，这个设备仍然能被系统正确地识别。
|2|挂载点|设备所连接到的文件系统树的目录。
|3|文件系统类型|Linux 允许挂载许多文件系统类型。大多数本地的 Linux 文件系统是 ext3， 但是也支持很多其它的，比方说 FAT16 (msdos), FAT32 (vfat)，NTFS (ntfs)，CD-ROM (iso9660)，等等。
|4|选项|文件系统可以通过各种各样的选项来挂载。有可能，例如，挂载只读的文件系统， 或者挂载阻止执行任何程序的文件系统（一个有用的安全特性，避免删除媒介。）
|5|频率|一位数字，指定是否和在什么时间用 dump 命令来备份一个文件系统。
|6|次序|一位数字，指定 fsck 命令按照什么次序来检查文件系统。

### 查看挂载的文件系统列表

```
# mount 命令被用来挂载文件系统
# 设备 on 挂载点 type 文件系统类型（选项）
alien@localhost:~$ mount
sysfs on /sys type sysfs (rw,nosuid,nodev,noexec,relatime)
proc on /proc type proc (rw,nosuid,nodev,noexec,relatime)
udev on /dev type devtmpfs (rw,nosuid,relatime,size=1947612k,nr_inodes=486903,mode=755)
/dev/hdc on /media/live-1.0.10-8 type iso9660 (ro,noexec,nosuid,
nodev,uid=500)
...

```

```
# umount卸载文件系统
alien@localhost:~$ su
密码： 
root@localhost:/home/alien# umount /dev/hdc

```

```
# 把设备挂载到了一个目录
mkdir /mnt/cdrom
mount -t iso9660 /dev/hdc /mnt/cdrom
# 卸载设备
umount /dev/hdc

```

> 
tips：打印机缓存是一个包含一些 RAM 内存 的设备，位于计算机和打印机之间。通过打印机缓存，计算机把要打印的结果发送到这个缓存区， 数据会迅速地存储到这个 RAM 中，这样计算机就能回去工作，而不用等待。与此同时，打印机缓存将会 以打印机可接受的速度把缓存中的数据缓慢地输出给打印机。


### 确定设备名称

```
# 列出目录/dev（所有设备的住所）
alien@localhost:~$ ls /dev
autofs           i2c-8               sda       tty21  tty55      ttyS3
block            initctl             sda1      tty22  tty56      ttyS30
bsg              input               sda10     tty23  tty57      ttyS31
btrfs-control    kmsg                sda11     tty24  tty58      ttyS4
...

```

**Linux 存储设备名称:**

|模式|设备
|------
|/dev/fd*|软盘驱动器
|/dev/hd*|老系统中的 IDE(PATA)磁盘。典型的主板包含两个 IDE 连接器或者是通道，每个连接器 带有一根缆线，每根缆线上有两个硬盘驱动器连接点。缆线上的第一个驱动器叫做主设备， 第二个叫做从设备。设备名称这样安排，/dev/hdb 是指第一通道上的主设备名；/dev/hdb 是第一通道上的从设备名；/dev/hdc 是第二通道上的主设备名，等等。末尾的数字表示 硬盘驱动器上的分区。例如，/dev/hda1是指系统中第一硬盘驱动器上的第一个分区，而 /dev/hda 则是指整个硬盘驱动器。
|/dev/lp*|打印机
|/dev/sd*|SCSI 磁盘。在最近的 Linux 系统中，内核把所有类似于磁盘的设备（包括 PATA/SATA 硬盘， 闪存，和 USB 存储设备，比如说可移动的音乐播放器和数码相机）看作 SCSI 磁盘。 剩下的命名系统类似于上述所描述的旧的/dev/hd*命名方案。
|/dev/sr*|光盘（CD/DVD 读取器和烧写器）

### 创建新的文件系统

假设我们使用一个16MB 闪存备，名称是/dev/sdb 指整个设备，/dev/sdb1是这个设备的第一分区，fdisk 命令操作分区：

```
# 操作分区
sudo fdisk /dev/sdb
# 创建一个新的文件系统
sudo mkfs -t ext3 /dev/sdb1
# 重新格式化为它最初的 FAT32文件 系统
sudo mkfs -t vfat /dev/sdb1

```

### 测试和修复文件系统

```
# 检查我们的闪存驱动器
sudo fsck /dev/sdb1

```

### 格式化软盘

使用 fdformat 程序，同时指定软盘设备名称（通常为/dev/fd0）：

```
sudo fdformat /dev/fd0
# 通过 mkfs 命令，给这个软盘创建一个 FAT 文件系统
sudo mkfs -t msdos /dev/fd0

```

### 直接把数据移入/出设备

dd 程序把磁盘驱动器简单地看成一个数据块大集合，可以克隆设备：

```
dd if=input_file of=output_file [bs=block_size [count=blocks]]

```

```
# 把第一个驱动器中的所有数据复制到第二个 驱动器中。
dd if=/dev/sdb of=/dev/sdc
# 如果只有第一个驱动器被连接到计算机上，我们可以把它的内容
# 复制到一个普通文件中供 以后恢复或复制数据：
dd if=/dev/sdb of=flash_drive.img

```

### 创建 CD-ROM 映像

```
# 适用于 DVD 光盘, 对于音频 CD，看一下 cdrdao 命令
dd if=/dev/cdrom of=ubuntu.iso

```

创建一个包含目录内容的 iso 映像文件，我们使用 genisoimage 程序:

```
genisoimage -o cd-rom.iso -R -J ~/cd-rom-files

```

“-R”选项添加元数据为 Rock Ridge 扩展，这允许使用长文件名和 POSIX 风格的文件权限。 同样地，这个”-J”选项使 Joliet 扩展生效，这样 Windows 中就支持长文件名了。

```
# 直接挂载一个 ISO 镜像
mkdir /mnt/iso_image
mount -t iso9660 -o loop image.iso /mnt/iso_image
# 清除一张可重写入的 CD-ROM
wodim dev=/dev/cdrw blank=fast
# 写入镜像
wodim dev=/dev/cdrw image.iso

```

**checksum 文件：**

iso 映像文件的贡献者也会提供 一个 checksum 文件，它是一个神奇的数学运算的计算结果，这个数学计算会产生一个能表示目标文件内容的数字。生成 checksum 数字的最常见方法是使用 md5sum 程序。

```
md5sum image.iso
34e354760f9bb7fbf85c96f6a3f94ece    image.iso

```

这就可以验证我们下载的镜像和发行商提供的镜像是否一致。如检验映像文件 dvd-image.iso 以及 DVD 光驱中磁盘 /dev/dvd 文件的完整性：

```
md5sum dvd-image.iso; dd if=/dev/dvd bs=2048 count=$(( $(stat -c "%s" dvd-image.iso) / 2048 )) | md5sum

```

## 三、网络系统

```
ping - 发送 ICMP ECHO_REQUEST 数据包到网络主机
traceroute - 打印到一台网络主机的路由数据包
netstat - 打印网络连接，路由表，接口统计数据，伪装连接，和多路广播成员
ftp - 因特网文件传输程序
wget - 非交互式网络下载器
ssh - OpenSSH SSH 客户端（远程登录程序）

```

### 检查和监测网络

```
alien@localhost:~ $ traceroute slashdot.org
traceroute to slashdot.org (216.105.38.15), 30 hops max, 60 byte packets
 1  10.35.0.1 (10.35.0.1)  43.175 ms  71.185 ms  71.203 ms
 2  10.0.5.185 (10.0.5.185)  71.196 ms  71.165 ms  71.134 ms
 3  10.0.8.5 (10.0.8.5)  71.052 ms 10.0.6.5 (10.0.6.5)  70.984 ms 10.0.8.5 (10.0.8.5)  70.978 ms
...
28  * * *
29  * * *
30  * * *

```

一共经由30个路由器，对于那些 提供标识信息的路由器，我们能看到它们的主机名，IP 地址和性能数据，这些数据包括三次从本地到 此路由器的往返时间样本。对于那些没有提供标识信息的路由器（由于路由器配置，网络拥塞，防火墙等 方面的原因），我们会看到几个星号，正如行中所示。

```
# 使用“-ie”选项，我们能够查看系统中的网络接口
alien@localhost:~ $ netstat -ie
Kernel Interface table
enp7s0    Link encap:以太网  硬件地址 74:e6:e2:41:f6:62  
          UP BROADCAST MULTICAST  MTU:1500  跃点数:1
          接收数据包:689500 错误:0 丢弃:0 过载:0 帧数:0
          发送数据包:156502 错误:0 丢弃:0 过载:0 载波:0
          碰撞:0 发送队列长度:1000 
          接收字节:300138422 (300.1 MB)  发送字节:23781675 (23.7 MB)
...

```

其中`enp7s0`是一个网络接口，`lo`是内部回环网络接口，它是一个虚拟接口，系统用它来自言自语。

### 网络中传输文件

**ftp：**

|命令|意思
|------
|ftp fileserver|唤醒 ftp 程序，让它连接到 FTP 服务器，fileserver。
|anonymous|登录名。输入登录名后，将出现一个密码提示。一些服务器将会接受空密码， 其它一些则会要求一个邮件地址形式的密码。如果是这种情况，试着输入 “user@example.com”。
|cd pub/cd_images/Ubuntu-8.04|跳转到远端系统中，要下载文件所在的目录下， 注意在大多数匿名的 FTP 服务器中，支持公共下载的文件都能在目录 pub 下找到
|ls|列出远端系统中的目录。
|lcd Desktop|跳转到本地系统中的 ~/Desktop 目录下。在实例中，ftp 程序在工作目录 ~ 下被唤醒。 这个命令把工作目录改为 ~/Desktop
|get ubuntu-8.04-desktop-i386.iso|告诉远端系统传送文件到本地。因为本地系统的工作目录 已经更改到了 ~/Desktop，所以文件会被下载到此目录。
|bye|退出远端服务器，结束 ftp 程序会话。也可以使用命令 quit 和 exit。

**lftp - 更好的 ftp：**

虽然 lftp 工作起来与传统的 ftp 程序很相似，但是它带有额外的便捷特性，包括 多协议支持（包括 HTTP），若下载失败会自动地重新下载，后台处理，用 tab 按键来补全路径名，还有很多。

**wget：**

不只能下载单个文件，多个文件，甚至整个网站都能下载，这个程序的许多选项允许 wget 递归地下载，在后台下载文件（你退出后仍在下载），能完成未下载 全的文件。

### 与远程主机安全通信

**ssh**（Secure Shell）：它要认证远端主机是否为它 所知道的那台主机（这样就阻止了所谓的“中间人”的攻击），其次，它加密了本地与远程主机之间 所有的通讯信息。

SSH 由两部分组成。SSH 服务端运行在远端主机上，在端口 22 上监听收到的外部连接，而 SSH 客户端用在本地系统中，用来和远端服务器通信。

为了能让系统接受远端的连接，它必须安装 OpenSSH-server 软件包，它必须允许在 TCP 端口 22 上接收网络连接。

**scp 和 sftp：**

OpenSSH 软件包也包含两个程序，scp（安全复制）被用来复制文件，与熟悉的 cp 程序非常相似。

```
# 主机名后面跟":"
scp bob@remote-sys:./document.txt ./

```

sftp:任何一台能用 SSH 客户端连接的远端机器，也可当作类似于 FTP 的服务器来使用.

## 四、查找文件

```
locate – 通过名字来查找文件
find – 在一个目录层次结构中搜索文件
xargs – 从标准输入生成和执行命令行
touch – 更改文件时间
stat – 显示文件或文件系统状态

```

### locate - 查找文件的简单方法

### find - 查找文件的复杂方式

locate 程序只能依据文件名来查找文件，而 find 程序能基于各种各样的属性 搜索一个给定目录（以及它的子目录），来查找文件。

上面`find ~`将产生一张很大的列表。

```
# wc 程序来计算出文件的数量
alien@localhost:~ $ sudo find ~ | wc -l
76602
# 文件数
alien@localhost:~ $ sudo find ~ -type f | wc -l
67531
# 目录数
alien@localhost:~ $ sudo find ~ -type d | wc -l
8899

```

**文件类型：**

<th align="center">文件类型</th>|描述
|------
<td align="center">b</td>|块特殊设备文件
<td align="center">c</td>|字符特殊设备文件
<td align="center">d</td>|目录
<td align="center">f</td>|普通文件
<td align="center">l</td>|符号链接

```
# 限定名字和大小
alien@localhost:~ $ sudo find ~ -type f -name "*.png" -size +1k | wc -l
5409

```

**大小单位：**

|字符|单位
|------
|b|512 个字节块。如果没有指定单位，则这是默认值。
|c|字节
|w|两个字节的字
|k|千字节(1024个字节单位)
|M|兆字节(1048576个字节单位)
|G|千兆字节(1073741824个字节单位)

**find常用测试条件：**

|测试条件|描述
|------
|-cmin n|匹配内容或属性最后修改时间正好在 n 分钟之前的文件或目录。 指定少于 n 分钟之前，使用 -n，指定多于 n 分钟之前，使用 +n。
|-cnewer file|匹配内容或属性最后修改时间晚于 file 的文件或目录。
|-ctime n|匹配内容和属性最后修改时间在 n*24小时之前的文件和目录。
|-empty|匹配空文件和目录。
|-group name|匹配属于一个组的文件或目录。组可以用组名或组 ID 来表示。
|-iname pattern|就像-name 测试条件，但是不区分大小写。
|-inum n|匹配 inode 号是 n的文件。这对于找到某个特殊 inode 的所有硬链接很有帮助。
|-mmin n|匹配内容被修改于 n 分钟之前的文件或目录。
|-mtime n|匹配的文件或目录的内容被修改于 n*24小时之前。
|-name pattern|用指定的通配符模式匹配的文件和目录。
|-newer file|匹配内容晚于指定的文件的文件和目录。这在编写执行备份的 shell 脚本的时候很有帮。 每次你制作一个备份，更新文件（比如说日志），然后使用 find 命令来判断哪些文件自从上一次更新之后被更改了。
|-nouser|匹配不属于一个有效用户的文件和目录。这可以用来查找 属于被删除的帐户的文件或监测攻击行为。
|-nogroup|匹配不属于一个有效的组的文件和目录。
|-perm mode|匹配权限已经设置为指定的 mode的文件或目录。mode 可以用 八进制或符号表示法。
|-samefile name|类似于-inum 测试条件。匹配和文件 name 享有同样 inode 号的文件。
|-size n|匹配大小为 n 的文件
|-type c|匹配文件类型是 c 的文件。
|-user name|匹配属于某个用户的文件或目录。这个用户可以通过用户名或用户 ID 来表示。

**操作符：**

```
find ~ \( -type f -not -perm 0600 \) -or \( -type d -not -perm 0700 \)

```

|操作符|描述
|------
|-and|如果操作符两边的测试条件都是真，则匹配。可以简写为 -a。 注意若没有使用操作符，则默认使用 -and。
|-or|若操作符两边的任一个测试条件为真，则匹配。可以简写为 -o。
|-not|若操作符后面的测试条件是真，则匹配。可以简写为一个感叹号（!）。
|()|把测试条件和操作符组合起来形成更大的表达式。这用来控制逻辑计算的优先级。 默认情况下，find 命令按照从左到右的顺序计算。经常有必要重写默认的求值顺序，以得到期望的结果。 即使没有必要，有时候包括组合起来的字符，对提高命令的可读性是很有帮助的。注意 因为圆括号字符对于 shell 来说有特殊含义，所以在命令行中使用它们的时候，它们必须 用引号引起来，才能作为实参传递给 find 命令。通常反斜杠字符被用来转义圆括号字符。

上述表达式`( expression 1 ) -or ( expression 2 )`解释为：`( file with bad perms ) -or ( directory with bad perms )`，圆括号对于 shell 有特殊含义，我们必须转义它们，来阻止 shell 解释它们。

|expr1 的结果|操作符|expr2 is…
|------
|真|-and|总要执行
|假|-and|从不执行
|真|-or|从不执行
|假|-or|总要执行

### 预定义的操作

find 命令允许基于搜索结果来执行操作

|操作|描述
|------
|-delete|删除当前匹配的文件。
|-ls|对匹配的文件执行等同的 ls -dils 命令。并将结果发送到标准输出。
|-print|把匹配文件的全路径名输送到标准输出。如果没有指定其它操作，这是 默认操作。
|-quit|一旦找到一个匹配，退出。

`-ok`：交互式地执行一个用户定义的行为。

```
-exec command {} ;

```

这里的 command 就是指一个命令的名字，{}是当前路径名的符号表示，分号是必要的分隔符 表明命令的结束。

### xargs

xargs 命令从标准输入接受输入，并把输入转换为一个特定命令的 参数列表。find 命令提供的 -print0 行为， 则会产生由 null 字符分离的输出，并且 xargs 命令有一个 –null 选项，这个选项会接受由 null 字符 分离的输入。这里有一个例子：

```
find ~ -iname ‘*.jpg’ -print0	xargs –null ls -l

```

```
alien@localhost:~ $ mkdir -p playground/dir-{00{1..9},0{10..99},100}
alien@localhost:~ $ touch playground/dir-{00{1..9},0{10..99},100}/file-{A..Z}
alien@localhost:~ $ find playground -type f -name 'file-A' | wc -l
100
alien@localhost:~ $ touch playground/timestamp
alien@localhost:~ $ stat playground/timestamp
  文件：'playground/timestamp'
  大小：0         	块：0          IO 块：4096   普通空文件
设备：80ah/2058d	Inode：1316820     硬链接：1
权限：(0664/-rw-rw-r--)  Uid：( 1000/   alien)   Gid：( 1000/   alien)
最近访问：2018-09-20 00:12:17.421846149 +0800
最近更改：2018-09-20 00:12:17.421846149 +0800
最近改动：2018-09-20 00:12:17.421846149 +0800
创建时间：-
alien@localhost:~ $ touch playground/timestamp
alien@localhost:~ $ stat playground/timestamp
  文件：'playground/timestamp'
  大小：0         	块：0          IO 块：4096   普通空文件
设备：80ah/2058d	Inode：1316820     硬链接：1
权限：(0664/-rw-rw-r--)  Uid：( 1000/   alien)   Gid：( 1000/   alien)
最近访问：2018-09-20 00:12:55.566202684 +0800
最近更改：2018-09-20 00:12:55.566202684 +0800
最近改动：2018-09-20 00:12:55.566202684 +0800
创建时间：-
alien@localhost:~ $ find playground -type f -name 'file-B' -exec touch '{}' ';'
alien@localhost:~ $ find playground -type f -newer playground/timestamp
playground/dir-051/file-B
playground/dir-007/file-B
playground/dir-092/file-B
playground/dir-068/file-B
...

```

**find 命令选项:**

|选项|描述
|------
|-depth|指示 find 程序先处理目录中的文件，再处理目录自身。当指定-delete 行为时，会自动 应用这个选项。
|-maxdepth levels|当执行测试条件和行为的时候，设置 find 程序陷入目录树的最大级别数
|-mindepth levels|在应用测试条件和行为之前，设置 find 程序陷入目录数的最小级别数。
|-mount|指示 find 程序不要搜索挂载到其它文件系统上的目录。
|-noleaf|指示 find 程序不要基于自己在搜索 Unix 的文件系统的假设，来优化它的搜索。 在搜索DOS/Windows 文件系统和CD/ROMS的时候，我们需要这个选项
