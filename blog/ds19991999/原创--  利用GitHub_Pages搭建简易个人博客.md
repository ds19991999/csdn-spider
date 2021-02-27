# 原创
：  利用GitHub_Pages搭建简易个人博客

# 利用GitHub_Pages搭建简易个人博客

个人博客已经开通：[https://ds19991999.github.io](https://ds19991999.github.io)，欢迎访问

# 1.基本实现
1. 在github上建库，库名必须是usrname.github.com,usr必须是你github账号的用户名；1. 在Jekyll上面选择喜欢的模板下载到本地（以Bef为例）；1. Git操作，建议使用客户端Git命令行操作
```
//1.打开git bash，配置用户名和邮件
git config --global user.name "your name"
git config --global user.email "your email"

//2.克隆你在github上建立的要建立个人博客的库
git svn clone url

//3.提交文件测试
touch test.c //新建一个文件用于测试
git add test.c
git commit -m "第一次提交测试"
git remote add test.c https://github.com/ds19991999/ds19991999.github.com.git
git push //可能不成功，按照提示进行操作，可能是config里面的文件没有用户名和邮箱

//我用下面命令就就正常了，应该是之前的库是空的需要先建一个banch分支
git push test.c
git push --set-upstream test.c master

//4.直接将本地的Bef博客模板clone到远程库上
git banch //查看本地分支，此刻应该只有master一个分支
//git checkout -b  本地分支名 //新建本地分支并切换分支（在本地分支进行开发）
//git pull origin 远程仓库分支名//将远程仓库分支上的代码更新到本地
git status //查看当前状态
git add .  //提交所有  或者git add  提交文件名，此前应该将Bef模板中的文件直接clone到本地仓库
git commit -m "提交信息备注" //提交到本地仓库
git push origin 要提交的分支名称(一般是master)  //将本地仓库推送到远程仓库里面

//注：傻瓜式操作：直接将Bef文件夹中所有文件拖动到github仓库
```

4.访问自己的博客主页 <br/> [https://usrname.github.io](https://usrname.github.io),比喻我的：[https://ds19991999.github.io](https://ds19991999.github.io)

# 2.关于GitHub Pages

GitHub Pages 是 GitHub 面向用户、组织和项目开放的公共静态页面搭建托管服 <br/> 务，允许站内生成网页，也允许用户自己编写网页，然后上传。站点可以被免 <br/> 费托管在 GitHub 上，可以选择使用 GitHub Pages 默认提供的域名 github.io <br/> 或者自定义域名来发布站点。GitHub Pages 支持自动利用 Jekyll 生成站点， <br/> GitHub Pages 可以被认为是用户编写的、托管在 GitHub 上的静态网页。

搭建中小型 Blog，特别是个人博客，确实是个很好的选择。既拥有绝对管理权， <br/> 又享受 GitHub 带来的便利，更主要的是，这一切是免费的，GitHub 提供无限流量.

# 3.关于Jekyll的结构

```
|-- _config.yml
|-- _includes
|-- _layouts
|   |-- default.html
|   `-- post.html
|-- _posts
|   |-- 2007-10-29-why-every-programmer-should-play-nethack.textile
|   `-- 2009-04-26-barcamp-boston-4-roundup.textile
|-- _site
`-- index.html
```

## _config.yml

配置文件，用来定义你想要的效果，设置之后就不用关心了。

## _includes

## _layouts

模板文件存放的位置。模板需要通过[YAML front matter](https://github.com/jekyll/jekyll/wiki/YAML-Front-Matter)来定义 <br/> 来定义，{ { content }}标记用来将数据插入到这些模板中来。

发布的文章会根据文章顶部的 yaml 文件头来设置一些元数据，如 layout:default，表示该文章的模板使用 _layouts 目录下的 post.html 文件；title:，表示该文章的标题，如果不设置这个值，默认使用嵌入文件名的标题等等。

## _posts

你的动态内容，一般来说就是你的博客正文存放的文件夹。他的命名有严格的规定，必须是**2012-02-22-artical-title.MARKUP**这样的形式， <br/> MARKUP是你所使用标记语言的文件后缀名，根据_config.yml中设定的链接规则，可以根据你的文件名灵活调整，文章的日期和标记语言后缀与文章的标题是独立的。

在博客上发布文章的时候，只需要在此文件夹中加入带有 YAML 头信息的 MarkDown 文件，然后 push 到 GitHub，就会被自动渲染成 HTML。

## _site

这个是Jekyll生成的最终的文档，不用去关心。最好把他放在你的.gitignore文件中忽略它。

## 其他文件夹

你可以创建任何的文件夹，在根目录下面也可以创建任何文件,假设你创建了project文件夹，下面有一个github-pages.md的文件,那么你就可以通过yoursite.com/project/github-pages访问的到，如果你是使用一级域名的话。

# 4.Jekyll的配置

配置文件在_config.yml文件中，不必一一追究了，需要的可以参考官方文档[关于Jekyll配置的官方文档](https://github.com/jekyll/jekyll/wiki),但Permalink和自定义项这两个很重要。

## `Permalink`

用来定义你最终的文章链接是什么形式，他有下面几个变量： <br/> - year 文件名中的年份 <br/> - month 文件名中的月份 <br/> - day 文件名中的日期 <br/> - title 文件名中的文章标题 <br/> - categories 文章的分类，如果文章没有分类，会忽略 <br/> - i-month 文件名中的除去前缀0的月份 <br/> - i-day 文件名中的除去前缀0的日期

配置效果 <br/> - `permalink: pretty` /2018/06/15/slap-chop/index.html <br/> - `permalink: /:month-:day-:year/:title.html` /06-15-2018/slap-chop.html <br/> - `permalink: /blog/:year/:month/:day/:title` /blog/2018/06/15/slap-chop/index.html <br/> - `permalink: /:title` /github-pages

## 自定义项

例如我们定义了`title:BeiYuu的博客`这样一项，那么你就可以在文章中使用{ { site.title }}来引用这个变量了，非常方便定义些全局变量。

# 5.YAML Front Matter和模板变量

对于YAML格式的文章，Jekyll的格式很严格，必须是这样的：

```
---
layout: post
title: Blogging Like a Hacker
---
```

前后的—不能省略，在这之间，你可以定一些你需要的变量，layout就是调用_layouts下面的某一个模板，他还有一些其他的变量可以使用： <br/> - permalink 你可以对某一篇文章使用通用设置之外的永久链接 <br/> - published 可以单独设置某一篇文章是否需要发布 <br/> - category 设置文章的分类 <br/> - tags 设置文章的tag

# 6.使用Disqus管理评论

注意是管理评论，Disqus支持很多的博客平台，注册账号什么的就不提了,参见下图：<img alt="image" src="http://beiyuu.com/images/githubpages/disqus-site.jpg" title=""/>

## Unversal Code

这里使用网友推荐的`Universal Code`,然后会看到一个介绍页面，把下面这段代码复制到你的模板里面，可以只复制到显示文章的模板中：

```
&lt;div id="disqus_thread"&gt;&lt;/div&gt;
&lt;script type="text/javascript"&gt;
    /* * * CONFIGURATION VARIABLES: EDIT BEFORE PASTING INTO YOUR WEBPAGE * * */
    var disqus_shortname = 'example'; // required: replace example with your forum shortname 这个地方需要改成你配置的网站名
    /* * * DON'T EDIT BELOW THIS LINE * * */
    (function() {
        var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
        dsq.src = 'http://' + disqus_shortname + '.disqus.com/embed.js';
        (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
    })();
&lt;/script&gt;
&lt;noscript&gt;Please enable JavaScript to view the &lt;a href="http://disqus.com/?ref_noscript"&gt;comments powered by Disqus.&lt;/a&gt;&lt;/noscript&gt;
&lt;a href="http://disqus.com" class="dsq-brlink"&gt;blog comments powered by &lt;span class="logo-disqus"&gt;Disqus&lt;/span&gt;&lt;/a&gt;
```

## 异步加载处理

为提高性能，需要进行异步加载处理，提高性能。比如在最开始页面打开的时候不显示评论，当你想看评论的时候，点击“显示评论”再加载Disqus的模块。

```
$('#disqus_container .comment').on('click',function(){
        $(this).html('加载中...');
        var disqus_shortname = 'beiyuu';
        var that = this;
        BYB.includeScript('http://' + disqus_shortname + '.disqus.com/embed.js',function(){$(that).remove()}); //这是一个加载js的函数
});
```

# 7.使用Gitalk添加评论功能
1. 注册 `GitHub Application`，`Authorization callback URL` 填写当前使用插件页面的域名,比喻我的`https//ds19991999.github.io/`,注意注意记住最后的clientID 和 clientSecret，owner 是自己的用户名.1. 创建 comments.html(以about页面为例)
```
{% if page.comments != false %}

    {% if site.comments_provider == 'gitalk' %}
        &lt;div id="gitalk-container"&gt;&lt;/div&gt;
        &lt;script src="/assets/js/gitalk.min.js"&gt;&lt;/script&gt;
        &lt;script&gt;
        var gitalk = new Gitalk({
            id: '{{ page.url }}',
            clientID: '{{ site.gitalk.clientID }}',
            clientSecret: '{{ site.gitalk.clientSecret }}',
            repo: '{{ site.gitalk.repo }}',
            owner: '{{ site.gitalk.owner }}',
            admin: ['{{ site.gitalk.owner }}'],
            labels: ['gitment'],
            perPage: 50,
        })
        gitalk.render('gitalk-container')
        &lt;/script&gt;
    {% endif %}
{% endif %}
```
1. 在 GitHub 上创建仓库 blog-comments，添加如下代码到 _config.yml <br/> clientID 和 clientSecret 是第一步注册的时候得到的，owner 是自己的用户名.
```
comments_provider: gitalk
gitalk:
    owner: jueye3
    repo: blog-comments
    clientID: fa5504fe07f319cba9ee
    clientSecret: 30532bea61e8b63dc5a852e448621a8c89cef99b
```
1. 下载 gitalk.min.js 和 gitalk.css <br/> 下载 gitalk.min.js（放到 assets/js 文件夹下）和 gitalk.css（放到assets/css 文件夹下）， push 后访问.1. 使用 GitHub 账号登陆初始化，就可以使用评论功能了.
# 8.添加代码高亮插件

两个可选插件[DlHightLight代码高亮组件](http://mihai.bazon.net/projects/javascript-syntax-highlighting-engine)和[Google Code Prettify](https://code.google.com/archive/p/google-code-prettify/)。DLHightLight支持的语言相对较少一些，有js、css、xml和html，Google的高亮插件基本上任何语言都支持，也可以自定义语言，也支持自动识别，也有行号的特别支持。

Google的高亮插件使用也比较方便，只需要在\

# 9.增加统计插件
1. 在百度统计上注册账号并登陆，然后新增网站 <br/> <img alt="image" src="http://images.gitbook.cn/a5501280-5bfa-11e8-9a68-fdee5b6ce888" title=""/> <br/> <img alt="image" src="http://images.gitbook.cn/d3a97590-5bfa-11e8-b9ab-abcfff93657e" title=""/>1. 在 _includes 下创建 baidu-anaylysis.html,内容是百度统计生成的代码，如下图: <br/> <img alt="image" src="http://images.gitbook.cn/d93486d0-5bfa-11e8-b5c3-3fe2bc231f99" title=""/>1. 在 head.html 文件中添加 {% include baidu-anaylysis.html %}，Push后可以检查是否成功 <br/> <img alt="image" src="http://images.gitbook.cn/fbd322f0-5bfa-11e8-9a68-fdee5b6ce888" title=""/>1. 代码正确安装，可以查看报告了 <br/> <img alt="image" src="http://images.gitbook.cn/00bfaa40-5bfb-11e8-b5c3-3fe2bc231f99" title=""/>
# 10.绑定域名

## 在github库中

新建一个 `CNAME` 文件（无后缀名）,用文本编辑器打开，在首行添加你的网站域名，如 [http://xxxx.com](http://xxxx.com)，注意前面没 [http://example.com](http://example.com) 或者 xxx.example.com。

## 在域名解析提供商

以百度云为例： <br/> - 先添加一个 CNAME，主机记录写 @，后面记录值写上你的 [http://xxxx.github.io](http://xxxx.github.io) <br/> - 再添加一个 CNAME，主机记录写 www，后面记录值也是 [http://xxxx.github.io](http://xxxx.github.io) <br/> - 这样别人用 www 和不用 www 都能访问你的网站（其实 www 的方式，会先解析成 [http://xxxx.github.io](http://xxxx.github.io)，然后根据 CNAME 再变成[http://xxx.com](http://xxx.com)，中间是经过一次转换的）。

# 11.参考资料

[https://github.com/ds19991999/ds19991999.github.com/blob/master/README.md](https://github.com/ds19991999/ds19991999.github.com/blob/master/README.md) <br/> [http://gitbook.cn/m/mazi/article/5af260fd6f98784056d381ce](http://gitbook.cn/m/mazi/article/5af260fd6f98784056d381ce) <br/> [http://beiyuu.com/github-pages](http://beiyuu.com/github-pages) <br/> [https://chrisniael.gitbooks.io/gitbook-documentation/content/index.html](https://chrisniael.gitbooks.io/gitbook-documentation/content/index.html)

# License

GNU General Public License v3.0
