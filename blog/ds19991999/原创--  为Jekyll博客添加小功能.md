# 原创
：  为Jekyll博客添加小功能

# 为Jekyll博客添加小功能

# 为博客添加各种功能

## 1.关于Jekyll本身插件的安装

一共三种方式: <br/> * 在根目录下新建`_plugins`文件夹, 然后把对应的`*.rb`插件文件放进去就行了; <br/> * 在`_config.yml`文件中增加一个`gems`关键字, 然后把要引用的插件用数组形式存储其中即可; <br/> * 在Gemfile中添加相关的插件;

三种方法都可以, 甚至完全可以同时使用~

## 2.用kramdown自动生成目录树

```
* 目录
{:toc}
```

第一行必须加！

## 3.添加标签归档页

```
---
layout: post
title: 标签
permalink: /tags/
---
&lt;ul class="tags"&gt;
    {% for tag in site.tags %}
    &lt;li&gt;
        &lt;a href="#{{ tag[0] }}"&gt;{{ tag[0] }}&lt;/a&gt; &lt;sup&gt;{{ tag[1].size }}&lt;/sup&gt;
    &lt;/li&gt;
    {% endfor %}
&lt;/ul&gt;

&lt;ul class="listing"&gt;
    {% for tag in site.tags %}
    &lt;li class="listing-seperator" id="{{ tag[0] }}"&gt;{{ tag[0] }}&lt;/li&gt;
    {% for post in tag[1] %}
    &lt;li class="listing-item"&gt;
        &lt;time datetime="{{ post.date | date:"%Y-%m-%d" }}"&gt;{{ post.date | date:"%Y-%m-%d" }}&lt;/time&gt;
        &lt;a href="{{ post.url }}" title="{{ post.title }}"&gt;{{ post.title }}&lt;/a&gt;
    &lt;/li&gt;
    {% endfor %}
{% endfor %}
&lt;/ul&gt;
```

## 4.添加日期归档页

```
---
layout: post
permalink: /archives/
title: "归档"
---
&lt;ul&gt;
  {% for post in site.posts %}

    {% unless post.next %}
      &lt;h2&gt;{{ post.date | date: '%Y年' }}&lt;/h2&gt;
    {% else %}
      {% capture year %}{{ post.date | date: '%Y' }}{% endcapture %}
      {% capture nyear %}{{ post.next.date | date: '%Y' }}{% endcapture %}
      {% if year != nyear %}
        &lt;h2&gt;{{ post.date | date: '%Y年' }}&lt;/h2&gt;
      {% endif %}
    {% endunless %}

    &lt;li&gt;{{ post.date | date:"%Y年%m月%d日：" }} &lt;a href="{{ post.url }}"&gt;{{ post.title }}&lt;/a&gt;&lt;/li&gt;
  {% endfor %}
&lt;/ul&gt;
```

## 5.添加网易云音乐插件

```
&lt;!-- cloud music --&gt;
&lt;!-- auto=1 可以控制自动播放与否，当值为 1 即打开网页就自动播放，值为 0 时需要访客手动点击播放 --&gt;
&lt;iframe frameborder="no" border="0" marginwidth="0" marginheight="0" width=330 height=86
        src="//music.163.com/outchain/player?type=2&amp;id={{ page.music-id }}&amp;auto=0&amp;height=66"&gt;
&lt;/iframe&gt;
```

```
  &lt;!-- 在正文开头添加网易云音乐插件 --&gt;
  {% if page.music-id %}
    {% include cloud-music.html %}
  {% endif %} 
  {{ content }}
```

## 6.添加站点访客数及文章浏览量

```
&lt;script async src="//dn-lbstatics.qbox.me/busuanzi/2.3/busuanzi.pure.mini.js"&gt;
&lt;/script&gt;
```

```
&lt;!-- pv的方式，单个用户连续点击n篇文章，记录n次访问量 --&gt;
&lt;span id="busuanzi_container_site_pv"&gt;
    本站总访问量&lt;span id="busuanzi_value_site_pv"&gt;&lt;/span&gt;次
&lt;/span&gt;
```

```
&lt;!-- uv的方式，单个用户连续点击n篇文章，只记录1次访客数 --&gt;
&lt;span id="busuanzi_container_site_uv"&gt;
  本站访客数&lt;span id="busuanzi_value_site_uv"&gt;&lt;/span&gt;人次
&lt;/span&gt;
```
1. 显示单页面访问量
```
&lt;!-- pv的方式，单个用户点击1篇文章，本篇文章记录1次阅读量 --&gt;
&lt;span id="busuanzi_container_page_pv"&gt;
  本文总阅读量&lt;span id="busuanzi_value_page_pv"&gt;&lt;/span&gt;次
&lt;/span&gt;
```

## 7.添加中英文字数统计
<li>英文字数统计 <br/>
</li><li>中文字数统计 <br/>
</li>
## 8.添加评论

使用[intensedebate](https://intensedebate.com/)，注册账号什么得不说了，将得到的html文件，即`intensedebate-comments.html`保存到`include`目录下，在`post.html`正文结束处添加：

```
  {% if site.intensedebate_comments %}
    {% include intensedebate-comments.html %}
  {% endif %} 
```

## 9.添加动态网站运行时间

```
&lt;!-- 计算网站运行时间 --&gt;
&lt;span style="font-size:12px;"&gt;&lt;script language=JavaScript&gt; 
 function secondToDate(second) {
     if (!second) {
        return 0;
     }

 var time = new Array(0, 0, 0, 0, 0);

 if (second &gt;= 365 * 24 * 3600) {
     time[0] = parseInt(second / (365 * 24 * 3600));
     second %= 365 * 24 * 3600;
 }  

 if (second &gt;= 24 * 3600) {
     time[1] = parseInt(second / (24 * 3600));
     second %= 24 * 3600;
 }

 if (second &gt;= 3600) {
     time[2] = parseInt(second / 3600);
     second %= 3600;
 }

 if (second &gt;= 60) {
     time[3] = parseInt(second / 60);
     second %= 60;
 }

 if (second &gt; 0) {
     time[4] = second;
 }
    return time;
}
&lt;/script&gt;

&lt;!-- 动态显示网站运行时间 --&gt;
&lt;script type="text/javascript" language="javascript"&gt;
    function setTime() {
        var create_time = Math.round(new Date(Date.UTC(2018, 05, 05, 0, 0, 0)).getTime() / 1000);
        var timestamp = Math.round((new Date().getTime() + 8 * 60 * 60 * 1000) / 1000);
        currentTime = secondToDate((timestamp - create_time));
        currentTimeHtml = '本站已安全运行' + currentTime[0] + '年' + currentTime[1] + '天' + currentTime[2] + '时' + currentTime[3] + '分' + currentTime[4] + '秒';
        document.getElementById("htmer_time").innerHTML = currentTimeHtml;
    }
    setInterval(setTime, 1000);
&lt;/script&gt;&lt;/span&gt;
```

> 
添加百度统计和Google分析以及站内搜索引擎，甚至自定义搜索引擎，以及更多细节操作见个人主页下的链接

