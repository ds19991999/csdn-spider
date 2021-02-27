# 原创
：  Ubuntu安装及配置

# Ubuntu安装及配置

**1.分区问题：**<br/> 1.swap分区，相当于虚拟内存<br/> 2./根目录，主分区，空间起始位置，越大越好<br/> 3./boot分区，逻辑分区，空间起始位置，200M即可，grub启动文件<br/> 4./home分区，逻辑分区，空间起始位置。<br/>  

**2.软件源安装**<br/> 1.建议改为国内软件源，https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu/<br/> 2.将系统自带的官方软件源进行备份，sudo cp /etc/apt/sources.list /etc/apt/sources.list.backup<br/> 3.将清华网站上的更新源复制，替换粘贴到sources.list中，用gedit打开<br/> 4.权限问题，先创建root用户:chmod 777 文件或文件夹

 

**3.主题优化**

参考：

[ubuntu16.04主题优化](http://www.linuxidc.com/Linux/2016-09/135165.htm)

[ubuntu装机优化](http://eldersword.leanote.com/post/ubuntu-%E8%A3%85%E6%9C%BA%E5%AE%8C%E6%88%90%E7%9A%84%E4%BC%98%E5%8C%96)

**3.1 安装 unity-tweak-tool**

```
sudo apt-get install unity-tweak-tool 
```

**3.2 安装 Flatabulous 主题**

```
# Flatabulous 主题
sudo add-apt-repository ppa:noobslab/themes
sudo apt-get update
sudo apt-get install flatabulous-theme

# 安装该主题配套的图标
sudo add-apt-repository ppa:noobslab/icons
sudo apt-get update
sudo apt-get install ultra-flat-icons
```

安装完成后，打开 unity-tweak-tool ，点击主题，修改为 Flatabulous；然后点击图标，修改为 Ultra-flat

**3.3 安装 Arc Theme 主题**

```
# 安装Arc Theme
sudo add-apt-repository ppa:noobslab/themes
sudo apt-get update
sudo apt-get install arc-theme
# 安装该主题配套的图标
sudo add-apt-repository ppa:noobslab/icons
sudo apt-get update
sudo apt-get install arc-icons
```

**3.2 安装 MAC OS 主题**

```
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

安装完成后，打开 unity-tweak-tool 软件，修改主题和图标，方法同上。

**4.安装Google**

sudo wget http://www.linuxidc.com/files/repo/google-chrome.list -P /etc/apt/sources.list.d/

wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -

sudo apt-get update

sudo apt-get install google-chrome-stable

/usr/bin/google-chrome-stable

 

**5.为浏览器安装flash**

1.去官网下载flash插件

2.解压

3.进入下载文件根目录

4.拷贝到本地firefox目录

sudo cp libflashplayer.so /usr/lib/firefox/browser/plugins

sudo cp -r usr/* /usr

 

**6.安装网易云音乐**

1.去官网下载包：[http://music.163.com/#/download](http://music.163.com/#/download)

2.安装：

sudo dpkg -i netease-cloud-music_1.1.0_amd64_ubuntu16.04.deb

sudo apt-get -f install

sudo dpkg -i netease-cloud-music_1.1.0_amd64_ubuntu16.04.deb

      不知道为什么这样安装的网易云音乐竟然没反应，我按照网上的教程各种试，添加了各种依赖，仍然不行，所以我老老实实的安装1.00版本

 

wget http://s1.music.126.net/download/pc/netease-cloud-music_1.0.0_amd64_ubuntu16.04.deb

sudo dpkg -i netease-cloud-music_1.0.0_amd64_ubuntu16.04.deb

sudo apt-get -y install -f #安装依赖

netease-cloud-music #启动网易云音乐

 

大功告成！

 

 

 

 

 

 

 

 
