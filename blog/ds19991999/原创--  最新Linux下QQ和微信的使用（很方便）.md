# 原创
：  最新Linux下QQ和微信的使用（很方便）

# 最新Linux下QQ和微信的使用（很方便）

# Linux下QQ和微信的使用（很方便）

先安利一波，不少大佬将app做成了AppImage的格式，这可以说是Linux入门级用户的福音，不少app可以直接在linux上面运行，直接下载AppImage文件，无需配置。当然，qq和微信一直以来都是大家关注的焦点，所以这里为就分享一波在Linux系统上面qq和微信最简单的使用方法。

### 1. 第一步获取AppImage文件

官网地址：[https://appimage.github.io/apps/](https://appimage.github.io/apps/) ，这个网站都是为Linux用户提供的AppImage文件，方便用户在Linux系统上体验一些常用的app。

微信就用官网的：[electron-wechat ](https://appimage.github.io/electron-wechat/)，当然这个：[https://github.com/geeeeeeeeek/electronic-wechat](https://github.com/geeeeeeeeek/electronic-wechat) 也是非常优秀的，提供deb包，安装也很方便。

而qq这个项目做的比较好：[https://github.com/askme765cs/Wine-QQ-TIM](https://github.com/askme765cs/Wine-QQ-TIM)

好了，得到appimage文件就美滋滋了。

### 2. 更改appimage包权限

```
chmod a+x QQ-20171129-x86_64.AppImage 
chmod a+x electron-wechat-0.1.1-x86_64.AppImage

```

权限改完了就直接享受Linux版的微信和qq了，运行`./QQ-20171129-x86_64.AppImage`，或者直接点击运行。是不是很方便！

### 3. 上图
