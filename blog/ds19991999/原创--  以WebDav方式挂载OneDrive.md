# 原创
：  以WebDav方式挂载OneDrive

# 以WebDav方式挂载OneDrive

玩`OneDrive`的时候，有时候会遇到没有`API`权限的帐号，这个时候我们就不能使用`rclone`挂载`OneDrive`，其他第三方也不行，这就有点难受了。<br/> 不过，我们还有另一种方式挂载，也就是以`WebDav`的方式挂载。<br/> 

### 文章目录

## 1、get cookie

网页登陆你的`OneDrive`。<br/> <img alt="mark" src="http://image.creat.kim/image/20190116/CpLEwlB3bCt1.png?imageslim"/><br/> 我们要拿到的就是如图所示的`FedAuth`和`rtFa`两个`cookie`的`Value`值，比较长的一串。**注意`Cookie`下的那几个网址选带有`sharepoint.com`的那个。**

拿到这两个值就可以进行下面的操作了。

## 2、install and config

### step1:

```
apt-get install davfs2

```

### step2:

IF Mount PATH: `/root/WebDav`

```
vi /etc/davfs2/davfs2.conf

add:
[/root/WebDav/]   # Mount PATH
ask_auth 0
add_header Cookie rtFa=XXXXXX;FedAuth=YYYYYY #Value

```

### revise url:

```
https://xxxxxxxcn-my.sharepoint.com/personal/rootmaster_xxxx_xxx_cn/_layouts/15/onedrive.aspx

to 

https://xxxxxxxcn-my.sharepoint.com/personal/rootmaster_xxxx_xxx_cn/Documents

```

## 3、mount

```
mount.davfs -o rw "https://xxxxxxxcn-my.sharepoint.com/personal/rootmaster_xxxx_xxx_cn/Documents" /root/WebDav

```

## 4、check

```
df -h

```

like this:

```
https://xxxxxxxcn-my.sharepoint.com/personal/rootmaster_xxxx_xxx_cn/Documents  1.3T  763G  509G  61% /root/WebDav
......

```

**Enjoy it!**
