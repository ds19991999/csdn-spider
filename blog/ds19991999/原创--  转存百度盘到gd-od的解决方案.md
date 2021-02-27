# 原创
：  转存百度盘到gd/od的解决方案

# 转存百度盘到gd/od的解决方案

**首页：**[HomePage](https://telegra.ph/HomePage-01-03)<br/>[https://telegra.ph/Fuck-PanBaidu-02-19](https://telegra.ph/Fuck-PanBaidu-02-19) <br/>[https://graph.org/Fuck-PanBaidu-02-19](https://graph.org/Fuck-PanBaidu-02-19)

### 一、安装aria2

```
wget -N https://git.io/aria2.sh &amp;&amp; chmod +x aria2.sh &amp;&amp; bash aria2.sh

```

启动：/etc/init.d/aria2 start

停止：/etc/init.d/aria2 stop

重启：/etc/init.d/aria2 restart

查看状态：/etc/init.d/aria2 status

配置文件：/root/.aria2/aria2.conf （配置文件包含中文注释，但是一些系统可能不支持显示中文）

令牌密匙：随机生成（可以改配置文件）

默认下载目录：/root/Download

### 二、aria2离线gd/od方案

1、安装rclone

```
curl https://rclone.org/install.sh | sudo bash

```

rclone配置可以参考：[https://rclone.org/drive/](https://rclone.org/drive/)

2、修改脚本 **/root/.aria2/autoupload.sh**

```
name='Onedrive' #配置Rclone时的name
folder='/DRIVEX/Download' #网盘里的文件夹，留空为网盘根目录。

```

3、修改aria2配置文件：**/root/.aria2/aria2.conf 启用文件下载完成后脚本：**

```
# 调用 rclone 上传(move)到网盘
on-download-complete=/root/.aria2/autoupload.sh

```

4、重启 aria2

```
/root/aria2.sh  选6重启
或者运行：service aria2 restart

```

5、使用aria2前端面板进行文件下载：[aria2.ml](http://aria2.ml/)

填好vps端的aria2配置信息

 

点击新建粘贴下载链接进行文件下载

 

下载的文件会自动上传到gd/od

### 三、利用第三方百度盘

这里推荐速盘，可惜PanDownload没有开放aria2配置

 

如图，修改下载文件保存位置，GUI界面无法修改，请先退出软件，在config.ini文件中进行修改：

 

 

其中下载文件保存位置与远程服务器的aria2的配置一样，比喻此方式安装的aria2就是**/root/Download**

于是就可以把你的百度网盘文件直接下载到gd/od中了。

### 四、效果图

1.使用AriaNG面板下载文件到VPS，利用**autoupload.sh脚本实现gd离线下载电影**

 

2.利用速盘远程aria2的功能实现将百度网盘文件远程下载到VPS，再利用**autoupload.sh脚本实现自动转存到gd**

 
