# 原创
：  Rclone笔记

# Rclone笔记

> 



### 目录

## 一些简单命令

### 挂载

```
# windows 挂载命令
rclone mount OD:/ H: --cache-dir E:\ODPATH --vfs-cache-mode writes &amp;
# linux 挂载命令
nohup rclone mount GD:/ /root/GDPATH --copy-links --no-gzip-encoding --no-check-certificate --allow-other --allow-non-empty --umask 000 &amp;
# 取消挂载————linux 通用
fusermount -qzu /root/GDPATH 或者
fusermount -u /path/to/local/mount
# windows 取消挂载
umount /path/to/local/mount

```

### rclone命令

```
rclone ls

eg____rclone ls remote:path [flags]
ls # 递归列出 remote 所有文件及其大小，有点类似 tree 命令
lsl # 递归列出 remote 所有文件、大小及修改时间
lsd # 仅仅列出文件夹的修改时间和文件夹内的文件个数

lsf # 列出当前层级的文件或文件夹名称
lsjson # 以JSON格式列出文件和目录


rclone copy

eg____rclone copy OD:/SOME/PATH GD:/OTHER/PATH
--no-traverse # /path/to/src中有很多文件，但每天只有少数文件发生变化，加上这个参数可以提高传输速度
-P # 实时查看传输统计信息
--max-age 24h # 仅仅传输24小时内修改过的文件，默认关闭
rclone copy --max-age 24h --no-traverse /path/to/src remote:/PATH -P

rclone sync
eg____rclone sync source:path dest:path [flags]
# 使用该命令时先用 --dry-run 测试，明确要复制和删除的内容

rclone delete
# 列出大于 100M 的文件
rclone --min-size 100M lsl remote:path
# 删除测试
rclone --dry-run --min-size 100M delete remote:path
# 删除
rclone --min-size 100M delete remote:path

# 删除路径及其所有内容，filters此时无效，这与 delete 不同
rclone purge

# 删除空路径
rclone rmdir

# 删除路径下的空目录
rclone rmdirs

# 移动文件
rclone move
# 移动后删除空源目录
--delete-empty-src-dirs

# 检查源和目标匹配中的文件
rclone check
# 从两个源下载数据并在运行中互相检查它们而不是哈希检测
--download

rclone md5sum
# 为路径中的所有文件生成md5sum文件
rclone sha1sum
# 为路径中的所有文件生成sha1sum文件
rclone size
# 在remote：path中打印该路径下的文件总大小和数量
--json # 输出json格式
rclone version --check #检查版本更新
rclone cleanup # 清理源的垃圾箱或者旧版本文件

rclone dedupe # 以交互方式查找重复文件并删除/重命名它们
--dedupe-mode newest - 删除相同的文件，然后保留最新的文件,非交互方式

rclone cat
# 同linux

rclone copyto
# 将文件从源复制到dest，跳过已复制的文件

rclone gendocs output_directory [flags] 
# 生成rclone的说明文档

rclone listremotes # 列出配置文件中所有源
--long 显示类型和名称 默认只显示名称

rclone moveto
# 不会传输未更改的文件

rclone cryptcheck /path/to/files encryptedremote:path
# 检查加密源的完整性

rclone about
# 获取源的配额 ，eg
$ rclone about ODA1P1:
Total:   5T
Used:    284.885G
Free:    4.668T
Trashed: 43.141G
--json # 以 json 格式输出


rclone mount # 挂载命令

# 在Windows使用则需要安装winfsp
--vfs-cache-mode # 不使用该参数，只能按顺序写入文件，只能在读取时查找，即windows程序无法操作文件，使用该参数即启用缓存机制
# 共四种模式：off|minimal|writes|full 缓存模式越高，rclone越多，代价是使用磁盘空间，默认为full
--vfs-cache-max-age 24h # 缓存24小时内修改过的文件
--vfs-cache-max-size 10g # 最大总缓存10g (缓存可能会超过此大小)
--cache-dir 指定缓存位置
--umask int 覆盖文件系统权限
--allow-non-empty 允许挂载在非空目录
--allow-other 允许其他用户访问
--no-check-certificate 不检查服务器SSL证书
--no-gzip-encoding 不设置接受gzip编码

```

## 用自己的 api 进行 gd 转存

> 
见这位大佬博客：[https://www.moerats.com/archives/877/](https://www.moerats.com/archives/877/)


使用 `rclone` 的人太多吉会有一个问题，我们使用的是共享的`client_id`，在高峰期会出现`403`或者还没到`750G`限制就出现`Limitations`问题，所以高频率使用`rclone`转存谷歌文件得朋友就需要使用自己的`api`。通过上面那篇文章给出的方法获取谷歌的 API 客户端`ID`和客户端密钥，`rclone config`命令配置的时候，会有部分提示你输入，直接粘贴就`OK`.

挂载就变成：

```
#该参数主要是上传用的
/usr/bin/rclone mount DriveName:Folder LocalFolder \
 --umask 0000 \
 --default-permissions \
 --allow-non-empty \
 --allow-other \
 --transfers 4 \
 --buffer-size 32M \
 --low-level-retries 200

#如果你还涉及到读取使用，比如使用H5ai等在线播放，就还建议加3个参数，添加格式参考上面
--dir-cache-time 12h
--vfs-read-chunk-size 32M
--vfs-read-chunk-size-limit 1G

```

## 突破 Google Drive 服务端 750g 限制

谷歌官方明确限制通过第三方`api`每天限制转存`750G`文件，这个 `750G` 是直接通过谷歌服务端进行，文件没有经过客户端，另外经过客户端上传到 `gd` 与 服务端转存不冲突，官方也有 `750G` 限制，所以每天上传限额一共是 `1.5T`

```
# 一般用法，使用服务端API，不消耗本地流量
rclone copy GD1:/PATH GD2:/PATH

# disable server side copies 使用客户端 API，流量走客户端
rclone --disable copy GD1:/PATH GD2:/PATH

```

这样就是每天 `1.5T` 了。

## 谷歌文档限制

在 `rclone ls` 中谷歌文档会出现 `-1`， 而对于其他 `VFS` 层文件显示 `0` ，比喻通过 `rclone mount`，`rclone serve`操作的文件。而我们用 `rclone sync`，`rclone copy`的命令时，它会忽略文档大小而直接操作。也就是说如果你没有下载谷歌文档，就不知道它多大，没啥影响…
