# 原创
：  Let's Encrypt 泛域名证书申请

# Let's Encrypt 泛域名证书申请

> 
github: [https://github.com/Neilpang/acme.sh](https://github.com/Neilpang/acme.sh)


通过acme申请Let’s Encrypt证书支持的域名DNS服务商有以下这些（国内用户较多的）：`cloudxns、dnspod、aliyun（阿里云）、cloudflare、linode、he、digitalocean、namesilo、aws、namecom、freedns、godaddy、yandex` 等等。

### 目录

## [安装acm.sh](http://xn--acm-pd0fq01r.sh)

```
curl  https://get.acme.sh | sh

```

`acme.sh`被安装在了`~./.acme.sh`，创建 一个 `bash` 的 `alias`, 方便你的使用: `alias acme.sh=~/.acme.sh/acme.sh`

通过`acme.sh`安装的证书会自动为你创建 `cronjob`, 每天 0:00 点自动检测所有的证书, 如果快过期了, 需要更新, 则会自动更新证书.

## DNS方式验证域名所有权

```
acme.sh  --issue  --dns   -d mydomain.com

```

`acme.sh` 会生成相应的解析记录显示出来, 你只需要在你的域名管理面板中添加这条 `txt` 记录即可.

## 获取`DNS API`

获取`DNS`域名商的`DNS API` ，`api` 也会将 上面的`txt` 记录自动添加到域名解析商。比喻阿里的`api`：[https://ak-console.aliyun.com/#/accesskey](https://ak-console.aliyun.com/#/accesskey) ，然后看说明进行配置 [https://github.com/Neilpang/acme.sh/tree/master/dnsapi](https://github.com/Neilpang/acme.sh/tree/master/dnsapi) 阿里的就是：

```
export Ali_Key="sdfsdfsdfljlbjkljlkjsdfoiwje"
export Ali_Secret="jlsdflanljkljlfdsaklkjflsa"
acme.sh --issue --dns dns_ali -d example.com -d *.example.com

```

这个`*`值的就是泛域名。运行一次之后Ali_Key和Ali_Secret将被保存`~/.acme.sh/account.conf`，生成的SSL证书目录在`~/.acme.sh/example.com`

## 安装证书

> 
详见：[copy/安装 证书](https://github.com/Neilpang/acme.sh/wiki/%E8%AF%B4%E6%98%8E#3-copy%E5%AE%89%E8%A3%85-%E8%AF%81%E4%B9%A6)


使用 `--installcert` 命令,并指定目标位置, 然后证书文件会被copy到相应的位置, 例如:

```
acme.sh  --installcert  -d  &lt;domain&gt;.com   \
        --key-file   /etc/nginx/ssl/&lt;domain&gt;.key \
        --fullchain-file /etc/nginx/ssl/fullchain.cer \
        --reloadcmd  "service nginx force-reload"

```

宝塔用户在SSL选项选择其他证书，把SSL证书内容粘贴上面去就行了<br/> <img alt="" src="http://image.creat.kim/picgo/20190314132922.png"/><br/> 这里改一下证书路径<br/> <img alt="" src="http://image.creat.kim/picgo/20190314132617.png"/><br/> 目前证书在 60 天以后会自动更新, 你无需任何操作. 今后有可能会缩短这个时间, 不过都是自动的, 你不用关心.

## 更新 `acme.sh`

自动更新：`acme.sh --upgrade --auto-upgrade`<br/> 关闭更新：`acme.sh --upgrade --auto-upgrade 0`

有问题看 [wiki](https://github.com/Neilpang/acme.sh/wiki) 和 [dubug](https://github.com/Neilpang/acme.sh/wiki/How-to-debug-acme.sh)
