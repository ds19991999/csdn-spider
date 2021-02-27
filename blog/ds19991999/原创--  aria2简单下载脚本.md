# 原创
：  aria2简单下载脚本

# aria2简单下载脚本

保存为 `bcloud`，修改权限 `chmod 755 bcloud` 就可以用了。

```
#!/bin/bash
# bcloud: bcloud downloud tool, rely on aria2.
# author: ds19991999
# date: 2018-09-26 16:35

# rely on:
# 	1.baidu-dl: http://kks.me/aMrPx !important
# 	2.aria2:
#		sudo add-apt-repository ppa:t-tujikawa/ppa 
#		sudo apt-get update 
#		sudo apt-get install aria2

# usage:run bcloud at terminal.

DIR=/home/$USER

echo "--&gt;Please enter urls for download."
echo -n "--&gt;URL:"
read downloud
echo

echo "--&gt;Please enter the save path(default:$DIR)."
echo -n "--&gt;PATH:"
read dir
dir=${dir:-$DIR}

echo "--&gt;The file will be downlouded at $dir"
echo
echo "--&gt;Downlouding..."

aria2c --dir=$dir --max-connection-per-server=16 --max-concurrent-downloads=16 --split=16 --continue=true $downloud

```
