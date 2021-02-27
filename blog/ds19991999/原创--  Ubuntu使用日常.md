# 原创
：  Ubuntu使用日常

# Ubuntu使用日常

# Ubuntu使用日常

> 
记录使用`Ubuntu`过程中遇到的问题，总结一些常用工具，归纳一些小技巧。本文永久更新地址：[Ubuntu.md](https://github.com/ds-ebooks/test/blob/master/Ubuntu.md)


### 文章目录

## 1、redshift色温调节工具

安装

```
# 只安装Redshift发现没有界面，所以安装了三个包
sudo apt install gtk-redshift redshift python-appindicator
# 执行
gtk-redshift 

```

配置

```
touch ~/.config/redshift.conf
sudo gedit ~/.config/redshift.conf
# 加上以下内容
; Global settings for redshift
[redshift]
; Set the day and night screen temperatures
temp-day=4500
temp-night=3500

; Enable/Disable a smooth transition between day and night
; 0 will cause a direct change from day to night screen temperature.
; 1 will gradually increase or decrease the screen temperature.
transition=1

; Set the screen brightness. Default is 1.0.
;brightness=0.9
; It is also possible to use different settings for day and night
; since version 1.8.
;brightness-day=0.7
;brightness-night=0.4
; Set the screen gamma (for all colors, or each color channel
; individually)
gamma=0.8
;gamma=0.8:0.7:0.8
; This can also be set individually for day and night since
; version 1.10.
;gamma-day=0.8:0.7:0.8
;gamma-night=0.6

; Set the location-provider: 'geoclue', 'geoclue2', 'manual'
; type 'redshift -l list' to see possible values.
; The location provider settings are in a different section.
location-provider=manual

; Set the adjustment-method: 'randr', 'vidmode'
; type 'redshift -m list' to see all possible values.
; 'randr' is the preferred method, 'vidmode' is an older API.
; but works in some cases when 'randr' does not.
; The adjustment method settings are in a different section.
adjustment-method=randr

; Configuration of the location-provider:
; type 'redshift -l PROVIDER:help' to see the settings.
; ex: 'redshift -l manual:help'
; Keep in mind that longitudes west of Greenwich (e.g. the Americas)
; are negative numbers.
[manual]
lat=36.10
lon=103.80

; Configuration of the adjustment-method
; type 'redshift -m METHOD:help' to see the settings.
; ex: 'redshift -m randr:help'
; In this example, randr is configured to adjust screen 1.
; Note that the numbering starts from 0, so this is actually the
; second screen. If this option is not specified, Redshift will try
; to adjust _all_ screens.
; [randr]
; screen=1

```

## 2、无道词典

环境

```
sudo apt-get install python3
sudo apt-get install python3-pip
sudo pip3 install bs4
sudo pip3 install lxml

```

安装

```
git clone https://github.com/chestnutheng/wudao-dict
cd ./wudao-dict/wudao-dict
sudo bash setup.sh #或者sudo ./setup.sh

```

## 3、pip指向问题

第一次安装pip

```
sudo apt-get install python-pip python-dev build-essential 
sudo pip install --upgrade pip 
sudo pip install --upgrade virtualenv 
sudo apt-get install python-setuptools python-dev build-essential

```

安装分别pip

```
sudo apt-get install python3-pip
sudo apt-get install python-pip

```

指向问题<br/> 编辑这三个文件，将第一行注释分别改为`python\python2\python3`

```
~ $which pip
/usr/local/bin/pip
21:36 alien@alien-Inspiron-3443:
~ $which pip2
/usr/local/bin/pip2
21:36 alien@alien-Inspiron-3443:
~ $which pip3
/usr/local/bin/pip3

```

改好之后便升级pip

```
sudo pip3 install --upgrade pip
sudo pip2 install --upgrade pip
sudo pip install --upgrade pip

```

## 4、更换pip源

pip国内的一些镜像,换源之后出现python2版本过低的情况导致以前的包下载不了，那就直接将文件夹删除就行。

linux:

```
cat &gt; ~/.pip/pip.conf
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple

```

windows:

> 
直接在user目录中创建一个pip目录，如：C:\Users\xx\pip，新建文件pip.ini，内容如下


```
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple

```

另外npm，yarn也可以通过换源提高速度，网上很多教程，稍微提一下。

## 5、GitHub源

```
sudo gedit /etc/hosts
219.76.4.4 github-cloud.s3.amazonaws.com
151.101.72.249 http://global-ssl.fastly.Net
192.30.253.112 http://github.com

```

## 6、查看Linux本地IP地址

```
ifconfig -a
inet addr:172.18.166.207  Bcast:172.18.166.255  Mask:255.255.255.0

```

## 7、ubuntu本地开启微型服务器

```
python -m SimpleHTTPServer 8888 #Python2
python -m http.server #python3

```

之后可以通过ip:端口远程访问本地主机文件。<br/> 传输文件

## 8、ECS与本地主机互传文件

通过`ssh`协议实现：

```
scp ~/cert/* root@47.107.129.219:/usr/local/nginx/cert
scp root@47.107.129.219:/usr/local/nginx/cert ~/cert/*

```

## 9、小书匠和Evernote

小书匠基础模板:

```
---
title: 2018-10-27未命名文件 
tags: tag1,tag2
grammar_cjkRuby: true
---
[Edit](http://markdown.xiaoshujiang.com/)

```

```
脚注[^1x]
[^1x]: 脚注用法测试

```

## 10、Windows 中 Chromium 缺少 Google API 密钥

在`CMD`中执行：

```
setx GOOGLE_API_KEY AIzaSyCkfPOPZXDKNn8hhgu3JrA62wIgC93d44k 
setx GOOGLE_DEFAULT_CLIENT_ID 811574891467.apps.googleusercontent.com 
setx GOOGLE_DEFAULT_CLIENT_SECRET kdloedMFGdGla2P1zacGjAQh

```

## 11、博客音乐外链

[音乐外链播放器推荐](https://perpeht.com/2017/12/%E4%BC%98%E7%A7%80%E9%9F%B3%E4%B9%90%E5%A4%96%E9%93%BE%E6%92%AD%E6%94%BE%E5%99%A8%E6%8E%A8%E8%8D%90/)

## 12、Debian/Ubuntu中管理多版本Node.js

安装nvm:

```
git clone https://github.com/creationix/nvm.git ~/.nvm
cd ~/.nvm
git checkout `git describe --abbrev=0 --tags`

```

激活nvm:

```
. ~/.nvm/nvm.sh

```

登录后自动激活nvm，在`~/.bashrc`加

```
export NVM_DIR=~/.nvm
[ -s "$NVM_DIR/nvm.sh" ] &amp;&amp; . "$NVM_DIR/nvm.sh"
[ -r $NVM_DIR/bash_completion ] &amp;&amp; . $NVM_DIR/bash_completion

```

卸载node和nvm

```
rm -rf ~/.nvm

```

## 13、虚拟终端（Ctrl+Alt+F1）下显示菱形中文乱码

系统全用英文吧：

```
sudo gedit /etc/default/locale

```

将内容改为：

```
LANG="en_US.UTF-8"
LANGUAGE="en_US:en"

```

再运行：

```
sudo locale-gen

```

然后重启`reboot`，会提示是否将文件夹改成英文的，此时选择“Update…”即可。

## 14、彻底卸载mysql重新安装

1.命令apt-get删除mysql

```
sudo apt-get remove --purge mysql-\*

```

2.手动删除mysql剩余文件<br/> 执行命令

```
sudo find  / -name mysql -print

```

会显示出所有的含有mysql文件名的路径，如下：

```
/var/lib/mysql
/var/lib/mysql/mysql
/var/log/mysql
/usr/bin/mysql
/usr/lib/mysql
/usr/share/mysql
/etc/mysql
/etc/init.d/mysql

```

都删除掉

3.重新安装

```
sudo apt-get install mysql-server mysql-client

```

如果报错执行下面命令再安装

```
sudo apt-get remove --purge mysql-\*
sudo apt-get install mysql-server mysql-client

```

## 15、MySQL5.7设置utf8编码格式

[查看博文](https://blog.csdn.net/qq_32144341/article/details/51318390)

## 16、WIndows的Linux子系统

[查看博文](http://csuncle.com/2017/08/08/Windows-linux%E5%AD%90%E7%B3%BB%E7%BB%9F-%E5%85%A5%E9%97%A8%E5%88%B0GUI/)

## 17、文件管理器左侧快捷方式管理

```
sudo gedit ~/.config/user-dirs.dirs
# 默认的内容是文档，图片，下载等目录
# This file is written by xdg-user-dirs-update
# If you want to change or add directories, just edit the line you're
# interested in. All local changes will be retained on the next run
# Format is XDG_xxx_DIR="$HOME/yyy", where yyy is a shell-escaped
# homedir-relative path, or XDG_xxx_DIR="/yyy", where /yyy is an
# absolute path. No other format is supported.
# 
XDG_DESKTOP_DIR="$HOME/Desktop"
XDG_DOWNLOAD_DIR="$HOME/Downloads"
XDG_TEMPLATES_DIR="$HOME/Templates"
XDG_PUBLICSHARE_DIR="$HOME/Public"
XDG_DOCUMENTS_DIR="$HOME/Documents"
XDG_MUSIC_DIR="$HOME/Music"
XDG_PICTURES_DIR="$HOME/Pictures"
XDG_VIDEOS_DIR="$HOME/Videos"
# 再创建一个文件，直接执行：
echo”enabled = false“&gt;〜/ .config / user-dirs.conf

```

## 18、访问磁盘

```
sudo apt-get install ntfs-3g
# 修复不能访问的磁盘
sudo ntfsfix /dev/sda6

```

## 19、Grub启动图形界面美化

[查看博文](https://tianyijian.github.io/2018/04/05/ubuntu-grub-beautify/)<br/> 更新Grub:

```
sudo update-grub
sudo grub-install /dev/sda

```

## 20、开机自启动

以`plank`为例

```
sudo ln -s /usr/share/applications/plank.desktop /etc/xdg/autostart/

```

## 21、Pycharm汉化

[JetBrains 系列软件汉化包](https://github.com/pingfangx/TranslatorX)

## 22、Notepad++配置

[查看博文](https://www.jianshu.com/p/3088175e5f78)

## 23、Windows10 Python配置

[查看博文](https://blog.csdn.net/qiang12qiang12/article/details/53239866)

## 24、MAC OS 主题

```
sudo apt-get install unity-tweak-tool 
sudo add-apt-repository ppa:noobslab/macbuntu


sudo apt-get update


sudo apt-get install macbuntu-os-icons-lts-v7


sudo apt-get install macbuntu-os-ithemes-lts-v7


cd &amp;&amp; wget -O Mac.po http://drive.noobslab.com/data/Mac/change-name-on-panel/mac.po


cd /usr/share/locale/en/LC_MESSAGES; sudo msgfmt -o unity.mo ~/Mac.po;rm ~/Mac.po;cd


wget -O launcher_bfb.png http://drive.noobslab.com/data/Mac/launcher-logo/apple/launcher_bfb.png
sudo mv launcher_bfb.png /usr/share/unity/icons/
gsettings set com.canonical.unity-greeter draw-grid false;exit


sudo add-apt-repository ppa:noobslab/themes
sudo apt-get update
sudo apt-get install macbuntu-os-bscreen-lts-v7

```

## 25、垃圾清理

```
sudo apt-get autoclean 清理旧版本的软件缓存
sudo apt-get clean 清理所有软件缓存
sudo apt-get autoremove 删除系统不再使用的孤立软件
sudo apt-get install gtkorphan -y清理Linux下孤立的包
sudo apt-get remove tracker

```

## 26、暴力关机导致蓝屏问题

```
sudo dpkg --configure -a
sudo apt-get install xserver-xorg-lts-utopic 
sudo dpkg-reconfigure xserver-xorg-lts-utopic 
reboot

```

## 27、mentohust联网

下载地址：[http://c7.gg/aCFu4](http://c7.gg/aCFu4)

```
sudo apt-get install mentohust
sudo mentohust -k
sudo mentohust -uusername -p123456 -a1 -d2 -b2 -v4.10 -w

```

## 28、彻底卸载Firefox

```
dpkg --get-selections |grep firefox
sudo apt-get purge firefox  
sudo apt-get purge firefox-locale-en
sudo apt-get purge firefox-locale-zh-hans
sudo apt-get purge unity-scope-firefoxbookmarks

```

## 29、安装chromium

```
sudo add-apt-repository ppa:a-v-shkop/chromium
sudo apt-get update
sudo apt-get install chromium-browser

```

## 30、终端图片显示工具

```
sudo apt-get install aview

```

```
asciiview elephant.jpg -driver curses 

```

## 31、经典菜单指示器

[ClassicMenu Indicator](http://www.florian-diesch.de/software/classicmenu-indicator/#download)

## 32、文件编码转换

安装`enca、iconv`:

```
sudo apt-get enca iconv

```

```
#enca查看文件编码
enca filename
#iconv将一个GBK编码的文件转换成UTF-8编码
enconv -L zh_CN -x UTF-8 filename

```

## 33、字符串logo工具
1. 安装：
```
sudo apt-get install figlet

```
1. 用法：
```
figlet JupyterLab

```

## 34、百度网盘相关

## 35、类似`QQ`的截图工具

> 
弃用`deepin-scrot`，请更新为[`deepin-screenshot`](https://pkgs.org/download/deepin-screenshot)


```
wget http://packages.linuxdeepin.com/deepin/pool/main/d/deepin-scrot/deepin-scrot_2.0-0deepin_all.deb
sudo dpkg -i deepin-scrot_2.0-0deepin_all.deb
# 修复依赖问题
sudo apt install -f
rm deepin-scrot_2.0-0deepin_all.deb

```

然后去`系统设置-键盘-快捷键-自定义快捷键`，之后就可以体验`QQ`那样的截图方式了。

当然`shutter`也很优秀，不过我更喜欢`deepin-scrot`

```
sudo apt-get install shutter

```

## 36、`dot`画图

```
sudo apt install graphviz

```

```
graph demo{
	1 -- 2
	2 -- 3
	3 -- 4
	1 -- 4
}

```

```
dot demo.dot -Tpng -o demo.png

```

## 37、`htop`进程管理工具

可以查看后台进程`PID`，方便`kill`进程.

```
sudo apt install htop

```

## 38、`fuck`终端工具

*[thefuck](https://github.com/nvbn/thefuck)

```
sudo pip3 install thefuck

```

## 39、查看电脑完整配置

```
lshw

```

## 40、标题栏实时显示上下行网速

下载安装运行`indicator-sysmonito`：

```
sudo apt-get install python3-psutil curl git gir1.2-appindicator3-0.1
git clone https://github.com/fossfreedom/indicator-sysmonitor.git
cd indicator-sysmonitor
sudo make install
nohup indicator-sysmonitor &amp;

```

## 41、万能解压工具`unar`

> 
通杀`7z zip tar rar gz`等等


```
sudo apt-get install unar

```

## 42、安装`aira2`及开机启动配置
