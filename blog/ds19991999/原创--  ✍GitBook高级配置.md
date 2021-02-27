# 原创
：  ✍GitBook高级配置

# ✍GitBook高级配置

> 
先留链接防丢失：
- [gitbook-use](https://github.com/zhangjikai/gitbook-use/tree/master)- [使用GitBook打造自己的出版平台](https://blog.csdn.net/ds19991999/article/details/81275458)


## 安装?

## 常用命令?

> 
- `gitbook-cli` 和 `gitbook` 是两个软件;- `gitbook-cli` 会将下载的 gitbook 的不同版本放到 `~/.gitbook`中, 可以通过设置`GITBOOK_DIR`环境变量来指定另外的文件夹.


## 目录结构?

```
.
├── book.json
├── README.md
├── SUMMARY.md
├── chapter-1/
|   ├── README.md
|   └── something.md
└── chapter-2/
    ├── README.md
    └── something.md
```

### Summary?

**示例1：**以后会经常用到的

```
# Summary
* [Introduction](README.md)-------------------------------1.1
----
### [Part I](folder1/README.md)

* [Writing is nice](folder1/writing.md)-------------------2.1.
* [GitBook is nice](folder1/gitbook.md)-------------------2.2.

### Part II

* [We love feedback](folder2/feedback_please.md)----------3.1.
* [Better tools for authors](folder2/better_tools.md)-----3.2.

----

* [Last part without title](title.md)---------------------4.1.
```

**示例2：**以后会用的但不常用的

```
# Summary

### Part I(part1/README.md)---------------------------1.

* [section1](part1/section1/README.md)----------------1.1.
    * [Writing is nice](part1/section1/writing.md)----1.1.1
    * [GitBook is nice](part1/section1/gitbook.md)----1.1.2
* [We love feedback](part1/title1.md)-----------------1.2
* [Better tools for authors](part1/title2.md)---------1.3
```

**示例3**：最简版本

```
# Summary
### Part I
* [Introduction](README.md)
* [Writing is nice](writing.md)
* [GitBook is nice](gitbook.md)

### Part II

* [We love feedback](feedback_please.md)
* [Better tools for authors](better_tools.md)
```

### Glossary?

`GLOSSARY.md`。该文件主要存储词汇信息，如果在其他页面中出现了该文件中的词汇，鼠标放到词汇上会给出词汇示意。

`GLOSSARY.md` 格式：

```
## Git-----------------词汇
分散式版本控制软件--------词汇示意

## Markdown
Aaron Swartz 跟John Gruber共同设计的排版语言
```

## book.json?

`book.json` 最重要，故单独作为一节。

### title：设置书本的标题?

```
"title" : "Gitbook Use"
```

### author：作者的相关信息?

```
"author" : "ds"
```

### description：本书的简单描述?

```
"description" : "记录Gitbook的配置和一些插件的使用"
```

### language：Gitbook使用的语言?

版本2.6.4中可选的语言如下：

```
en, ar, bn, cs, de, en, es, fa, fi, fr, he, it, ja, ko, no, pl, pt, ro, ru, sv, uk, vi, zh-hans, zh-tw
```

配置使用简体中文:

```
"language" : "zh-hans",
```

### gitbook: 指定使用的gitbook版本?

```
"gitbook" : "3.2.2",
"gitbook" : "&gt;=3.0.0"
```

### root：指定根目录?

```
"root": "."
```

### links：左侧导航栏添加链接信息?

```
"links" : {
    "sidebar" : {
        "个人主页" : "http://www.ds-vip.top"
    }
}
```

### styles：自定义页面样式?

默认情况下各`generator`对应的`css`文件：

```
"styles": {
    "website": "styles/website.css",
    "ebook": "styles/ebook.css",
    "pdf": "styles/pdf.css",
    "mobi": "styles/mobi.css",
    "epub": "styles/epub.css"
}
```

例如使`&lt;h1&gt; &lt;h2&gt;`标签有下边框， 可以在`website.css`中设置，这个可以有。

```
h1 , h2{
    border-bottom: 1px solid #EFEAEA;
}
```

### plugins：配置使用的插件?

```
"plugins": [
    "disqus"
]
```

```
"plugins": [
    "-search"
]
```

### pluginsConfig：配置插件的属性?

```
"pluginsConfig": {
    "fontsettings": {
        "theme": "sepia",
        "family": "serif",
        "size":  1
    }
}
```

上面就是配置Gitbook界面那个`A`按钮的默认属性。

### structure?

指定 Readme、Summary、Glossary 和 Languages 对应的文件名，下面是这几个文件对应变量以及默认值：

|变量|含义和默认值
|------
|`structure.readme`|`Readme file name (defaults to README.md)`
|`structure.summary`|`Summary file name (defaults to SUMMARY.md)`
|`structure.glossary`|`Glossary file name (defaults to GLOSSARY.md)`
|`structure.languages`|`Languages file name (defaults to LANGS.md)`

## GitBook插件?

可以指定插件的版本可以使用 `plugin@0.3.1` ， 下面的插件在 GitBook 的 `3.2.3` 版本中可以正常工作，[插件官网](https://plugins.gitbook.com/)。

具体介绍看这里：[https://github.com/zhangjikai/gitbook-use/blob/master/plugins.md](https://github.com/zhangjikai/gitbook-use/blob/master/plugins.md)

## 主题?

我们常用的就是 Book 文档模式，所以只看这部分。

### theme-default?

默认的 Book 主题。将 `showLevel` 设为 `true`， 就可以显示标题前面的数字索引，默认不显示。 

```
{
    "theme-default": {
        "showLevel": true
    }
}
```

### theme-comscore?

这个主题为标题添加了颜色

```
{
"plugins": [
        "theme-comscore"
    ]
}
```

## book.json配置文件?
