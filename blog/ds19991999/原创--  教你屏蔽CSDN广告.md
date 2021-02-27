# 原创
：  教你屏蔽CSDN广告

# 教你屏蔽CSDN广告

## 吐槽一下

CSDN博客的优点就不提了，但是有一点很难忍受，那就是广告，几乎每一个页面都少不了广告。之前我就是因为受不了广告，所以干脆就不玩CSDN了，后来发现这些广告都是可以屏蔽的，只是我这种小白不清楚而已…

基本上就是安装几个插件就可以让CSDN变得绿色健康，不仅可以屏蔽广告，还能进行页面排版优化，简直不能再方便了。

废话不多说，开始安装插件。

## 步骤

### 1.Stylus插件

先在Google的扩展程序商店中搜索`Stylus`，第一个就是，有了这个插件，我们才能对网页进行自定义样式和排版修改。 <br/> <img alt="" src="https://raw.githubusercontent.com/ds19991999/githubimg/master/picgo/20180819214140.jpg" title=""/> <br/> 这个插件真的是一个插件神器，有了它，可以安装各种第三方插件进行各种网页的自定义样式修改，还可以使用自己写的`CSS`样式进行网页优化，十分方便，比喻在`Github`上面安装几个插件，然后页面就变成这个样子了。 <br/> <img alt="" src="https://raw.githubusercontent.com/ds19991999/githubimg/master/picgo/20180819214543.jpg" title=""/> <br/> 比喻在百度贴吧安装一个插件，然后页面就变成这个样子了，是不是很惊艳。 <br/> <img alt="" src="https://raw.githubusercontent.com/ds19991999/githubimg/master/picgo/20180819215228.jpg" title=""/> <br/> 这些网页样式插件在 [https://userstyles.org/](https://userstyles.org/) 上面都可以找到，之后直接傻瓜式的点安装就完事了。

好了，回到我们要解决的问题，屏蔽 `CSDN` 广告。

### 2.CSDN去广告插件

在 [https://userstyles.org/styles/browse/csdn](https://userstyles.org/styles/browse/csdn) 中搜索`CSDN去广告插件`，如下图，然后安装就可以了。 <br/> <img alt="" src="https://raw.githubusercontent.com/ds19991999/githubimg/master/picgo/20180819220008.jpg" title=""/> <br/> 可以看到这插件还是近两天更新的，然后就被我无意中发现了，源码其实就是下面几十行。

```
.aside-box div:first-child{
    display:none;
}
.box-box-large{
    display:none;
}
.box-box-aways{
    display:none;
}
main div:nth-child(5){
    display:none;
}
.csdn-tracking-statistics.mb8.box-shadow{
    display:none; 
}
.J_adv{
    display:none;
}
.post_body div:nth-last-child(2){
    display:none;
}
/*update 2018-08-15*/
#_360_interactive{
    display:none;
}
.meau-list li:nth-child(7){
    display:none;
}
.text.float-left{
    display:none;
}
.recommend-item-box.recommend-ad-box{
    display:none;
}
  /*update 2018-08-16*/
.bbs_detail_wrap div:nth-child(5){
    display:none;
}
.bbs_feed.bbs_feed_ad_box{
    display:none;
}
/* 分享请注明作者姓名  create by Demo_Liu */
```

这些东西对于前端的同学来说就太容易了，鼠标右键调试网页源码，找到广告位 <br/> <img alt="" src="https://raw.githubusercontent.com/ds19991999/githubimg/master/picgo/20180819221002.jpg" title=""/> <br/> 看这一行：

```
&lt;div class="csdn-tracking-statistics mb8 box-shadow" data-pid="blog" data-mod="popu_4" style="height:250px;"&gt;
...
```

这里就是广告位，那我们就在 `CSS` 中定义它不展示，也就是

```
.csdn-tracking-statistics.mb8.box-shadow{
    display:none; 
}
```

**通过这种方式我们可以自定义展示网页排版板块，比喻`background` 这个属性可以调节板块背景色和透明度，前面那两张图就是典型例子，有透明度的模块看起来总感觉有点 * 格，所以只要我们有了 [Stylus插件](https://chrome.google.com/webstore/detail/stylus/clngdbkpkpeebahjckkjfobafhncgmne?utm_source=chrome-ntp-icon)，就可以在各种网页随心所欲，为所欲为**。

基本上这个简短的`CSS`就可以屏蔽掉CSDN广告，感谢 [Demo_Liu](https://blog.csdn.net/demo_liu/article/month/2018/08?orderby=UpdateTime) 博主提供的插件。

### 3.其他优化

在 [https://userstyles.org/styles/browse/csdn](https://userstyles.org/styles/browse/csdn) 中可以看到其他不少插件，这里我推荐一个`CSDN正文前置` 插件。 <br/> <img alt="" src="https://raw.githubusercontent.com/ds19991999/githubimg/master/picgo/20180819222711.jpg" title=""/> <br/> 将所有样式统一换成这种左右排版格式。 <br/> <img alt="" src="https://raw.githubusercontent.com/ds19991999/githubimg/master/picgo/20180819222926.jpg" title=""/> <br/> 源码：

```
main {
    float: left;
}
aside {
    float: right;
}
```

没错就是这几行。。。当然你也可以试试其他样式，自己写一个自己喜欢的网页样式也不是很难，不过我还是太懒了，不想折腾这些东西，有别人造轮子就直接用了。。。
