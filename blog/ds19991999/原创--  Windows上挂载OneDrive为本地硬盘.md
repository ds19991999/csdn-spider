# 原创
：  Windows上挂载OneDrive为本地硬盘

# Windows上挂载OneDrive为本地硬盘

> 
本文最新更新地址：[可能需要f…q](https://telegra.ph/Windows%E4%B8%8B%E7%94%A8rclone%E6%8C%82%E8%BD%BDOneDrive%E4%B8%BA%E6%9C%AC%E5%9C%B0%E7%A1%AC%E7%9B%98-01-03)


### 文章目录

## 1、rclone下载地址：

官网下载：[https://rclone.org/downloads/](https://rclone.org/downloads/)

`GitHub`下载：[https://github.com/ncw/rclone/releases/tag/v1.45](https://github.com/ncw/rclone/releases/tag/v1.45)

下载完成后在解压到你喜欢的文件夹下，例如我的：

另外Windows使用rclone还需要另一个依赖工具`winfsp`，下载地址：[http://www.secfs.net/winfsp/download/](http://www.secfs.net/winfsp/download/)

## 2、配置环境变量

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20181214195631596.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2RzMTk5OTE5OTk=,size_16,color_FFFFFF,t_70"/><br/> 双击`Path`，把刚才解压到的文件路径新加到`Path`，比喻我的`C:\Software\Tools\rclone-v1.45-windows-amd64`：

## 3、检查rclone是否配置成功

按`win`+`X`，然后按`A`，输入`rclone --version`，如果出现下面的输出则安装成功，否则重复上面步骤。

## 4、开始配置rclone

```
C:\WINDOWS\system32&gt;rclone config
2018/12/14 18:07:53 NOTICE: Config file "C:\\Users\\Alien\\.config\\rclone\\rclone.conf" not found - using defaults
No remotes found - make a new one
n) New remote
s) Set configuration password
q) Quit config
n/s/q&gt; n
name&gt; OneDrive
Type of storage to configure.
Enter a string value. Press Enter for the default ("").
Choose a number from below, or type in your own value
 1 / A stackable unification remote, which can appear to merge the contents of several remotes
   \ "union"
 2 / Alias for a existing remote
   \ "alias"
 3 / Amazon Drive
   \ "amazon cloud drive"
 4 / Amazon S3 Compliant Storage Providers (AWS, Ceph, Dreamhost, IBM COS, Minio)
   \ "s3"
 5 / Backblaze B2
   \ "b2"
 6 / Box
   \ "box"
 7 / Cache a remote
   \ "cache"
 8 / Dropbox
   \ "dropbox"
 9 / Encrypt/Decrypt a remote
   \ "crypt"
10 / FTP Connection
   \ "ftp"
11 / Google Cloud Storage (this is not Google Drive)
   \ "google cloud storage"
12 / Google Drive
   \ "drive"
13 / Hubic
   \ "hubic"
14 / JottaCloud
   \ "jottacloud"
15 / Local Disk
   \ "local"
16 / Mega
   \ "mega"
17 / Microsoft Azure Blob Storage
   \ "azureblob"
18 / Microsoft OneDrive
   \ "onedrive"
19 / OpenDrive
   \ "opendrive"
20 / Openstack Swift (Rackspace Cloud Files, Memset Memstore, OVH)
   \ "swift"
21 / Pcloud
   \ "pcloud"
22 / QingCloud Object Storage
   \ "qingstor"
23 / SSH/SFTP Connection
   \ "sftp"
24 / Webdav
   \ "webdav"
25 / Yandex Disk
   \ "yandex"
26 / http Connection
   \ "http"
Storage&gt; 18
** See help for onedrive backend at: https://rclone.org/onedrive/ **

Microsoft App Client Id
Leave blank normally.
Enter a string value. Press Enter for the default ("").
client_id&gt;
Microsoft App Client Secret
Leave blank normally.
Enter a string value. Press Enter for the default ("").
client_secret&gt;
Edit advanced config? (y/n)
y) Yes
n) No
y/n&gt; n
Remote config
Use auto config?
 * Say Y if not sure
 * Say N if you are working on a remote or headless machine
y) Yes
n) No
y/n&gt; y
If your browser doesn't open automatically go to the following link: http://127.0.0.1:53682/auth
Log in and authorize rclone for access
Waiting for code...

```

此时会浏览器会弹出登录Microsoft账号页面，输入账号密码登陆，点`是`

如果授权成功的话浏览器会出现这个页面

此时终端会提示你继续操作像这样：

因为我是拿个人账号写教程的，所以就选`1`

```
If your browser doesn't open automatically go to the following link: http://127.0.0.1:53682/auth
Log in and authorize rclone for access
Waiting for code...
Got code
Choose a number from below, or type in an existing value
 1 / OneDrive Personal or Business
   \ "onedrive"
 2 / Root Sharepoint site
   \ "sharepoint"
 3 / Type in driveID
   \ "driveid"
 4 / Type in SiteID
   \ "siteid"
 5 / Search a Sharepoint site
   \ "search"
Your choice&gt; 1
Found 1 drives, please select the one you want to use:
0:  (personal) id=28acee48ba0a80c9
Chose drive to use:&gt; 0
Found drive 'root' of type 'personal', URL: https://onedrive.live.com/?cid=28acee48ba0a80c9
Is that okay?
y) Yes
n) No
y/n&gt; y
--------------------
[OneDrive]
type = onedrive
token = {"access_token":"EwB4A8l74t6GzbtsBBeBUYAAZr+nsbvDJvpTZnIGTclACszh9PmiR6klQruRt9oBU5AD5ReAZLULrKBbFjgQzmUJHTW1Qg9EI2zCoj+/XMlp4M0V2sraXxwnDZvP/xHtLgMGIF3PLOjlSU0Thh3KCdA4/RIkAALoI7x5ycwXQLuBJ+D/iX3QwJFhVO4or7ogiaVUF0I3oF/A7dOEBJljUwHnBhYeyjOEpCRtoOXIrKl08afJbKtjVDXricLu4aXAIfBYibI7wffxQNxC2AWb5Z6TQ6BQUpUVs2Q48MUYCsDRshbyNhWxZOVlhtjOr3jRGVfDBb6iPuglwVaozSF68RRQbxc+L3QZ7aC4DZgAACLr0PZo0+g2xSAJr0YPcN9jCXJJvW9rHx9mt39W0nLlOUDzHTgi9mNNeAQmxfhFwlMxOr23MMW+Ux2fv7lg1uVdPdMsqsqsqq	sqqsSIPsRlNSD66FN/YwFHJ58NVZif+2CO38vFMgA5OCR0xV/AZ3OP4qhLt6eCGR4/AZ2L99UltF7pSNIGP6gkgdlyurEdsLZa/KhApGapSGNyKhhR9Eiwhdbnfksn5flspsFkjWEbu4IJ7I8v7SpNXvTcIErhc4fIR3Kdk+55owCbtpGjzU435RmTZDs0LqU09DLAobhPXAB0MiansnU5vsrlLvudbYm5n9To549gTkPfwCBCjPkr+Xlk8jeJ2prlDyksaXlX0EdukBbA+x0FBaEHmaxExK7w19DjmXXj8MCs1RF3dawbegyLwSnq2+V9M/sqUxVO4uHG+Pw1Bds7L+ysAM+Tcu9BBb7t8/XEpaHzYF5XO8Q9pCOhhcUO8fsI8aA1aupBSbVf0W/AyKsrasUTZiYLgFsz6lYDgF0t5XyD/YGmTHwgutPW32HfjlQ4Nd8g+be+Lllmyyywve28Ynyy7ZitKJkQ4OKRWcBwYyOikJNvG/RZYUXEy6XJtyDJqyaEwE7PVriEPGzPtmT49hixjamUbM42/UTMPxIKTFSJUpQwMgkzQU6hgqo6gPRrbC8XSR5qquRdvcSgfDTs+FaUgssCsxExPzUKqGFYitI9Wh16MjhteeUfLVOruJapGcSRgOOXmwE76qf+bSfN80jrZ+mIH0C","token_type":"Bearer","refresh_token":"MCdzaJTxbvjx0gqccalX3SwZ84Q1D*Hoc2plXP2lNLLyYXeseIDzIzXF9GSKcl35vabYNK1PlNbHkn7zJULI6TEHJkvsMj3vMGG9xODHnZhhoD6r74yYxBC9G72RhIwo2n*qA!rvP7yhGShwH8RC1DxmMhUtmfBO2kpXvkAONhNG8nN9zWaGQDpCIu2!rLrpqH0Bi0amMocXotNGEFHrASLP583x2fpX5Da3VY*AFM18uIpsvg7i0aTj*02e1fAplBUmMzDoo8gd*xqZYYe7eQWaAv1SYuMBFw5TsdYONN5y!ewQcrv9*hhxoLI8xK7VY8VSwG8!9e21N6yLYFFHsTYZMMUOcF0LFEJmo1b29xRkShfuXXk6mxajTCn3IUbOKKP9EW","expiry":"2018-12-14T19:12:44.8939629+08:00"}
drive_id = 28acce58ba0a81c9
drive_type = personal
--------------------
y) Yes this is OK
e) Edit this remote
d) Delete this remote
y/e/d&gt; y
Current remotes:

Name                 Type
====                 ====
OneDrive             onedrive

e) Edit existing remote
n) New remote
d) Delete remote
r) Rename remote
c) Copy remote
s) Set configuration password
q) Quit config
e/n/d/r/c/s/q&gt;

```

到这里已经把`OneDrive`配置好了，选择`q`结束配置，

> 
注：配置文件在当前用户家目录


## 5、挂载OneDrive为本地硬盘

```
rclone mount OneDrive:/ H: --cache-dir E:\OneDrive --vfs-cache-mode writes &amp;

```

如果出现：`The service rclone has been started.`则说明挂载成功(看到我很可怜了吧，只有15G的空间，求大佬送号?）。

效果图：

好了，就是这样，更多`rclone`相关的知识自行`Google`。

> 
最后说一点，执行上面这条命令退出终端后台挂载程序也会退出，达不到我们的目的，所以在命令后面加一个`&amp;`符号就行了，这样退出终端后台程序照样运行，像这样：


其他盘如`GoogleDrive`、`DropBox`等等也可以通过这种方式挂载，这样使得云端文件就像本地文件一样，只要你宽带够大，可以与本地硬盘一样无差别体验。

## 补充
