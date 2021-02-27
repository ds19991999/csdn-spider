# 原创
：  解决套路云Debian新机update的时候出现Waiting for headers和404错误

# 解决套路云Debian新机update的时候出现Waiting for headers和404错误

```
rm -rf /root/.pip /root/.pydistutils.cfg /etc/apt/sources.list.d/sources-aliyun-0.list /etc/apt/sources.list.d/sources-aliyun* /var/lib/apt/lists/* 

```

```
deb http://mirrors.cloud.aliyuncs.com/debian/ jessie main contrib non-free
deb-src http://mirrors.cloud.aliyuncs.com/debian/ jessie main contrib non-free
deb http://mirrors.cloud.aliyuncs.com/debian/ jessie-proposed-updates main non-free contrib
deb-src http://mirrors.cloud.aliyuncs.com/debian/ jessie-proposed-updates main non-free contrib
deb http://mirrors.cloud.aliyuncs.com/debian/ jessie-updates main contrib non-free
deb-src http://mirrors.cloud.aliyuncs.com/debian/ jessie-updates main contrib non-free
 
## Uncomment the following two lines to add software from the 'backports'
## repository.
##
## N.B. software from this repository may not have been tested as
## extensively as that contained in the main release, although it includes
## newer versions of some applications which may provide useful features.
#deb http://mirrors.cloud.aliyuncs.com/debian/ jessie-backports main contrib non-free
#deb-src http://mirrors.cloud.aliyuncs.com/debian/ jessie-backports main contrib non-free

```

```
apt-get clean
apt-get update

```

套路云还是套路云，服气！！！
