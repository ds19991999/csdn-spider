# 原创
：  01-Latex简介

# 01-Latex简介

# LaTex简介

# Contents

## 优雅的LaTex

有很多 Geeks 或者 LaTeX’s Fanatical Fans 过分地强调了 LaTeX 的一些并非重点的特性，以至于很多初学者会觉得 LaTeX 很神秘很复杂，从而引发了初学者的畏难情绪甚至是负面情绪。尽管这些 Fans 说得并没有错，我是说在事实上，但是他们的表达方式和内心态度却间接阻碍了 LaTeX 的发展，我想这也是和他们的初衷相悖的。

*** LaTex—— 这个优雅，但有着自己高傲，却绝不复杂甚至神秘的东西。***

## Hello World!

输入：

```
\documentclass{article}
%这里是导言区
\begin{document}
Hello, world!
\end{document}
```

输出： <br/> 

此处的第一行 `\documentclass{article}` 中包含了一个控制序列（或称命令/标记）。所谓控制序列，是以反斜杠`\`开头，以第一个**空格或非字母** 的字符结束的一串文字，他们并不被输出，但是他们会影响输出文档的效果。这里的控制序列是 `documentclass`，它后面紧跟着的 `{article}` 代表这个控制序列有一个必要的参数，该参数的值为 `article`。这个控制序列的作用，是调用名为 “article” 的文档类。

****请注意，TeX 对控制序列的大小写是敏感的****

其后出现了控制序列 `begin`，这个控制序列总是与 `end`成对出现。这两个控制序列以及他们中间的内容被称为「环境」；他们之后的第一个必要参数总是一致的，被称为环境名。

只有在 “document” 环境中的内容，才会被正常输出到文档中去或是作为控制序列对文档产生影响。也就是说，在 \end{document} 之后插入任何内容都是无效的。

`\begin{document}`与 `\documentclass{article}`之间的部分被称为导言区。导言区中的控制序列，通常会影响到整个输出文档。比如，我们通常在导言区设置页面大小、页眉页脚样式、章节标题样式等等。

## 中英混排

CTeX 宏集的优势在于，它适用于多种编译方式；在内部处理好了中文和中文版式的支持，隐藏了这些细节；并且，提供了不少中文用户需要的功能接口。

请注意，CTeX 宏集和 CTeX 套装是两个不同的东西。CTeX 宏集本质是 LaTeX 宏的集合，包含若干文档类（.cls 文件）和宏包（.sty 文件）。CTeX 套装是一个 TeX 系统。

新版 CTeX 宏集的默认能够自动检测用户的操作系统，并为之配置合适的字库。对于 Windows 用户、Mac OS X 用户和 Linux 用户，都无需做任何配置，就能使用 CTeX 宏集来排版中文。[2015-05-20 更新]

```
\documentclass[UTF8]{ctexart}
\begin{document}
你好，world!
\end{document}
```

可以看到支持中文！仅仅加了UTF-8和`ctexart`，实际上Jupyter的md本身已经支持了中文，看下面一个例子。

```
\title{你好，world!}
\author{Liam}
\date{\today}
\begin{document}
\maketitle
你好，world!
\end{document}
```

\title{你好，world!} <br/> \author{Liam} <br/> \maketitle
