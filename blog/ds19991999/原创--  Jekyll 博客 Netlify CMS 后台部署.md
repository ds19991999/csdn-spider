# 原创
：  Jekyll 博客 Netlify CMS 后台部署

# Jekyll 博客 Netlify CMS 后台部署

### 文章目录

## 获取`Client ID`和`Secret`

在 [Github OAuth](https://github.com/settings/developers) 页面新建一个 `app` 获取 `Client ID`和`Secret`

其中`Authorization callback URL`必须填这个：[https://api.netlify.com/auth/done](https://api.netlify.com/auth/done) ，其余随意。

## 去`netlify` 后台绑定 `GitHub` 的 `repositorie`

绑定成功是这个样子的：

这个时候出现的错误暂时不要管。

`setting-&gt;Domain management` ，添加`github`自带的二级域名，如果在`github`上面自定义了域名，也要加上，不要管 `DNS` 验证.

## 在GitHub新建netlify分支

内容可以参考我的 [netlify](https://github.com/ds19991999/ds19991999.github.io/tree/netlify) 分支，其中 `config.yml`文件里的域名改成你的`github` 二级域名，如果自定义了域名请填自定义的域名

## 在主分支`master`创建`admin`文件夹

```
admin
 ├ index.html
 └ config.yml

```

我的就是：[admin](https://github.com/ds19991999/ds19991999.github.io/tree/master/admin)

## 配置`admin`里的`config`

我这个`jekyll`只用到发布文章的`post`，所以后台也只需要这个简单的功能，只需要加一点这个文章头部的选项，每个人不一样，需要自己写。官方文档可以参考：[netlifycms-docs](https://www.netlifycms.org/docs/intro/)<img alt="1552916047947"/>

到这里，`GitHub`仓库的修改基本上完成了。

## 去 netlify 后台配置编译

`setting-&gt;Buil &amp; deploy-&gt;Deploy contexts`，将`Production branch`改成`netlify`分支，将`Branch deploys`改成`master`分支。

然后就可以编译了：

## 登录博客后台

进入 `https://网站域名/admin` 后台登陆，大概就是这样子。
