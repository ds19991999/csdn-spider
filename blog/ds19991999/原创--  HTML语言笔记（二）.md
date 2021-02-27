# 原创
：  HTML语言笔记（二）

# HTML语言笔记（二）

##  8.文本格式化

 &lt;pre&gt;标签：预格式文本，它保留了空格和换行。<br/> &lt;b&gt;标签：粗体<br/> &lt;code&gt;&lt;kbd&gt;&lt;tt&gt;&lt;samp&gt;&lt;var&gt;常用于计算机/编程<br/> title属性，缩写和首字母缩写：
<li> &lt;acronym title="World Wide Web"&gt;WWW&lt;/acronym&gt;  
     <hr/> </li><li> &lt;abbr title="etcetera"&gt;etc.&lt;/abbr&gt;  
     <hr/> </li>
---


 改变文字方向：`&lt;bdo dir="rtl"&gt;Here is some Hebrew text&lt;/bdo&gt;`

###  8.1 块引用：
<li> &lt;blockquote&gt;长引用&lt;/blockquote&gt; #浏览器会插入换行和外边距  
     <hr/> </li><li> &lt;q&gt;短引用&lt;/q&gt; #浏览器不会有任何特殊的呈现  
     <hr/> </li>
---


 删除字效果和插入字效果：`&lt;p&gt;一打有 &lt;del&gt;二十&lt;/del&gt; &lt;ins&gt;十二&lt;/ins&gt; 件。&lt;/p&gt;`<br/> 显示效果：

 一打有 ~~二十~~ <ins>十二</ins> 件。

 

###  8.2 文本格式化标签：

| 标签| 描述
|------
| [&lt;b&gt;](http://www.w3school.com.cn/tags/tag_font_style.asp)| 定义粗体文本
| [&lt;big&gt;](http://www.w3school.com.cn/tags/tag_font_style.asp)| 定义大号字
| [&lt;em&gt;](http://www.w3school.com.cn/tags/tag_phrase_elements.asp)| 定义着重文字
| [&lt;i&gt;](http://www.w3school.com.cn/tags/tag_font_style.asp)| 定义斜体字
| [&lt;small&gt;](http://www.w3school.com.cn/tags/tag_font_style.asp)| 定义小号子
| [&lt;strong&gt;](http://www.w3school.com.cn/tags/tag_phrase_elements.asp)| 定义加重语义
| [&lt;sub&gt;](http://www.w3school.com.cn/tags/tag_sup.asp)| 定义下标字
| [&lt;sup&gt;](http://www.w3school.com.cn/tags/tag_sup.asp)| 定义上标字
| [&lt;ins&gt;](http://www.w3school.com.cn/tags/tag_ins.asp)| 定义插入字
| [&lt;del&gt;](http://www.w3school.com.cn/tags/tag_del.asp)| 定义删除字
| [&lt;s&gt;](http://www.w3school.com.cn/tags/tag_strike.asp)| 弃用。使用&lt;del&gt;代替
| [&lt;strike&gt;](http://www.w3school.com.cn/tags/tag_strike.asp)| 弃用。使用&lt;del&gt;代替
| [&lt;u&gt;](http://www.w3school.com.cn/tags/tag_u.asp)| 弃用。使用样式（style）代替

###  8.3 计算机输出

| 标签| 描述
|------
| [&lt;code&gt;](http://www.w3school.com.cn/tags/tag_phrase_elements.asp)| 定义代码格式，不保留多余的空格和折行
| [&lt;kbd&gt;](http://www.w3school.com.cn/tags/tag_phrase_elements.asp)| 定义键盘输出
| [&lt;samp&gt;](http://www.w3school.com.cn/tags/tag_phrase_elements.asp)| 定义计算机代码的输出示例
| [&lt;tt&gt;](http://www.w3school.com.cn/tags/tag_font_style.asp)| 定义打字机代码
| [&lt;var&gt;](http://www.w3school.com.cn/tags/tag_phrase_elements.asp)| 定义数学变量，公式等
| [&lt;pre&gt;](http://www.w3school.com.cn/tags/tag_pre.asp)| 定义**预格式文本，不改变原有格式**
| &lt;listing&gt;| 弃用，使用&lt;pre&gt;代替
| &lt;plaintext&gt;| 弃用，使用&lt;pre&gt;代替
| &lt;xmp&gt;| 弃用，使用&lt;pre&gt;代替

###  8.4 引用、引用和术语定义**

| 标签| 描述
|------
| [&lt;abbr&gt;](http://www.w3school.com.cn/tags/tag_abbr.asp)| 定义缩写
| [&lt;acronym&gt;](http://www.w3school.com.cn/tags/tag_acronym.asp)| 定义首字母缩写
| [&lt;address&gt;](http://www.w3school.com.cn/tags/tag_address.asp)| 定义地址
| [&lt;bdo&gt;](http://www.w3school.com.cn/tags/tag_bdo.asp)| 定义文字方向，反向显示文本
| [&lt;blockquote&gt;](http://www.w3school.com.cn/tags/tag_blockquote.asp)| 定义长的引用
| [&lt;q&gt;](http://www.w3school.com.cn/tags/tag_q.asp)| 定义短的引用
| [&lt;cite&gt;](http://www.w3school.com.cn/tags/tag_phrase_elements.asp)| 定义著作标题，常以斜体表示
| [&lt;dfn&gt;](http://www.w3school.com.cn/tags/tag_phrase_elements.asp)| 定义一个项目定义

###  8.5 CSS样式

 **插入样式表**

####  8.5.1 外部样式表

 当页面具有普遍性，能应用与多个页面时用外部样式表，通过更改一个文件来改变整个站点的外观
<li> &lt;head&gt;  
     <hr/> </li><li> &lt;link rel="stylesheet" type="text/css" href="mystyle.css"&gt;  
     <hr/> </li><li> &lt;/head&gt;  
     <hr/> </li>
---


####  8.5.2 内部样式表

 当单个文件需要特别样式时，就可以使用内部样式表，即在head部分通过&lt;style&gt;标签定义内部样式表。
<li> &lt;head&gt;  
     <hr/> </li><li>   
     <hr/> </li><li> &lt;style type="text/css"&gt;  
     <hr/> </li><li> body {background-color: red}  
     <hr/> </li><li> p {margin-left: 20px}  
     <hr/> </li><li> &lt;/style&gt;  
     <hr/> </li><li> &lt;/head&gt;  
     <hr/> </li>
---


---


---


####  8.5.3 内联样式

 当特殊的样式需要用到个别元素时用到，方法即在相关标签中使用样式属性，样式属性可以包含任何<ins> [CSS](http://www.w3school.com.cn/css/index.asp) </ins>属性。
<li> &lt;!-- 以下实例显示出如何改变段落的颜色和左外边距 --&gt;  
     <hr/> </li><li> &lt;p style="color: red; margin-left: 20px"&gt;  
     <hr/> </li><li> This is a paragraph  
     <hr/> </li><li> &lt;/p&gt;  
     <hr/> </li>
---


---


| 标签| 描述
|------
| [&lt;style&gt;](http://www.w3school.com.cn/tags/tag_style.asp)| 定义样式定义
| [&lt;link&gt;](http://www.w3school.com.cn/tags/tag_link.asp)| 定义资源引用
| [&lt;div&gt;](http://www.w3school.com.cn/tags/tag_div.asp)| 定义文档中的节或区域（块级）
| [&lt;span&gt;](http://www.w3school.com.cn/tags/tag_span.asp)| 定义文档中的行内的小块或区域
| [&lt;font&gt;](http://www.w3school.com.cn/tags/tag_font.asp)| 规定文本的字体，字体尺寸，字体颜色（弃用）
| [&lt;basefont&gt;](http://www.w3school.com.cn/tags/tag_basefont.asp)| 定义基准字体（弃用）
| [&lt;center&gt;](http://www.w3school.com.cn/tags/tag_center.asp)| 对文本进行水平居中（弃用）

###  8.6 链接

 **&lt;a&gt;标签使用：**

####  8.6.1 通过使用 href 属性 - 创建指向另一个文档的链接
<li> &lt;!-- 文字超链接 --&gt;  
     <hr/> </li><li> &lt;a href="http://www.microsoft.com/"&gt;本文本&lt;/a&gt;   
     <hr/> </li><li>   
     <hr/> </li><li> &lt;!-- 图像作为链接 --&gt;  
     <hr/> </li><li> &lt;a href="/example/html/lastpage.html"&gt;  
     <hr/> </li><li> &lt;img border="0" src="/i/eg_buttonnext.gif" /&gt;  
     <hr/> </li><li> &lt;/a&gt;  
     <hr/> </li>
---


---


---


####  8.6.2 通过使用 name 属性 - 创建文档内的书签

 **name**属性规定锚（anchor）的名称，利用name属性可以**创建HTML页面中的书签**。当使用**命名锚**（named anchors）时，我们可以创建直接跳至该命名锚（比如页面中某个小节）的链接。
<li> &lt;!-- 锚，显示在页面上的文本 --&gt;  
     <hr/> </li><li> &lt;a name="lable"&gt;锚  
     <hr/> </li>
---


 **注意：**

> 
1.锚的名称可以是任何你喜欢的名字<br/> 2.您可以使用 id 属性来替代 name 属性，命名锚同样有效。<br/> 3.假如浏览器找不到已定义的命名锚，那么就会定位到文档的顶端。不会有错误发生。


 实例：
<li> &lt;!-- 在HTML文档中对锚进行命名，创建一个书签 --&gt;  
     <hr/> </li><li> &lt;a name="tips"&gt;基本的注意事项 - 有用的提示&lt;/a&gt;  
     <hr/> </li><li> &lt;!-- 在同一个文档中创建指向该锚的链接 --&gt;  
     <hr/> </li><li> &lt;a href="#tips"&gt;有用的提示&lt;/a&gt;  
     <hr/> </li><li> &lt;!-- 在其他页面中创建指向该锚的链接 --&gt;  
     <hr/> </li><li> &lt;a href="http://www.w3school.com.cn/html/html_links.asp#tips"&gt;有用的提示&lt;/a&gt;  
     <hr/> </li>
---


---


---


####  8.6.3 target属性

 定义被链接的文档在何处显示，_blank是在新窗口打开文档，_top是跳出框架，直接进入文档
<li> &lt;!-- 在新窗口中打开文档 --&gt;  
     <hr/> </li><li> &lt;html&gt;  
     <hr/> </li><li> &lt;body&gt;  
     <hr/> </li><li>   
     <hr/> </li><li> &lt;a href="http://www.w3school.com.cn/"  
     <hr/> </li><li> target="_blank"&gt;Visit W3School!&lt;/a&gt;  
     <hr/> </li><li>   
     <hr/> </li><li> &lt;/body&gt;  
     <hr/> </li><li> &lt;/html&gt;  
     <hr/> </li>
---


---


---


---


###  8.7 图像

 图像标签&lt;img&gt;和源属性&lt;Src&gt;，其中&lt;img&gt;是空标签`&lt;img src="url" /&gt;`，即没有闭合标签。

> 
**图像标签**



> 
**替换文本属性（Alt）:**



> 
**图像align属性：**



> 
**图像大小(width height):**



> 
**图像链接**



> 
**图像映射**

<li> &lt;img  
     <hr/> </li><li> src="/i/eg_planets.jpg"  
     <hr/> </li><li> border="0" usemap="#planetmap"  
     <hr/> </li><li> alt="Planets" /&gt;  
     <hr/> </li><li>   
     <hr/> </li><li> &lt;map name="planetmap" id="planetmap"&gt;  
     <hr/> </li>
---


---


---


> 
**图像转化为图像映射**

<li> &lt;a href="/example/html/html_ismap.html"&gt;  
     <hr/> </li><li> &lt;img src="/i/eg_planets.jpg" ismap /&gt;  
     <hr/> </li><li> &lt;/a&gt;  
     <hr/> </li>
---


###  8.8 表格

 每个表格由**table**标签开始，表格行由**tr**标签开始，表格数据由**td**标签开始，表头以**th**标签开始，表题以**caption**标签开始。

####  8.8.1 示例

 **示例1：**
<li> &lt;table border="1"&gt;  
     <hr/> </li><li> &lt;tr&gt;  
     <hr/> </li><li> &lt;td&gt;100&lt;/td&gt;  
     <hr/> </li><li> &lt;td&gt;200&lt;/td&gt;  
     <hr/> </li><li> &lt;td&gt;300&lt;/td&gt;  
     <hr/> </li><li> &lt;/tr&gt;  
     <hr/> </li><li> &lt;/table&gt;  
     <hr/> </li>
---


---


---


 **示例2（表格边框）:**

> 
border是边框属性，不定义的话不显示边框<br/> 带有普通的边框border="1"<br/> 带有粗的边框border="8"<br/> 带有很粗的边框border=“15”

<li> &lt;table border="1"&gt;  
     <hr/> </li><li> &lt;tr&gt;  
     <hr/> </li><li> &lt;td&gt;First&lt;/td&gt;  
     <hr/> </li><li> &lt;td&gt;Row&lt;/td&gt;  
     <hr/> </li><li> &lt;/tr&gt;   
     <hr/> </li><li> &lt;tr&gt;  
     <hr/> </li><li> &lt;td&gt;Second&lt;/td&gt;  
     <hr/> </li><li> &lt;td&gt;Row&lt;/td&gt;  
     <hr/> </li><li> &lt;/tr&gt;  
     <hr/> </li><li> &lt;/table&gt;  
     <hr/> </li>
---


---


---


---


---


 **表头:**<br/> 表格的表头采用&lt;th&gt;标签进行定义，一般显示为粗体。
<li> &lt;tr&gt;  
     <hr/> </li><li> &lt;th&gt;Heading&lt;/th&gt;  
     <hr/> </li><li> &lt;th&gt;Another Heading&lt;/th&gt;  
     <hr/> </li><li> &lt;/tr&gt;  
     <hr/> </li>
---


---


 **空单元格:**

> 
&lt;td&gt; &lt;/td&gt;，有些浏览器不会显示空格单元边框，为避免这种情况，最好加入一个空格占位符`&amp;nbsp;`


####  8.8.2 表格标签

| 表格| 描述
|------
| [&lt;table&gt;](http://www.w3school.com.cn/tags/tag_table.asp)| 定义表格
| [&lt;caption&gt;](http://www.w3school.com.cn/tags/tag_caption.asp)| 定义表格标题
| [&lt;th&gt;](http://www.w3school.com.cn/tags/tag_th.asp)| 定义表格的表头
| [&lt;tr&gt;](http://www.w3school.com.cn/tags/tag_tr.asp)| 定义表格的行
| [&lt;td&gt;](http://www.w3school.com.cn/tags/tag_td.asp)| 定义表格单元
| [&lt;thead&gt;](http://www.w3school.com.cn/tags/tag_thead.asp)| 定义表格的页眉
| [&lt;tbody&gt;](http://www.w3school.com.cn/tags/tag_tbody.asp)| 定义表格的主体
| [&lt;tfoot&gt;](http://www.w3school.com.cn/tags/tag_tfont.asp)| 定义表格的页脚
| [&lt;col&gt;](http://www.w3school.com.cn/tags/tag_col.asp)| 定义用于表格列的属性
| [&lt;colgroup&gt;](http://www.w3school.com.cn/tags/tag_colgroup.asp)| 定义表格列的组

####  8.8.3 杂项：

> 
表格标题:&lt;caption&gt;标签<br/> 横跨两列的单元格: colspan属性`&lt;th colspan="2"&gt;电话&lt;/th&gt;`<br/> 横跨两行的单元格: rowspan属性`&lt;th rowspan="2"&gt;电话&lt;/th&gt;`<br/> [表格内标签](http://www.w3school.com.cn/tiy/t.asp?f=html_table_elements)<br/> 单元格边距：cellpadding属性：`&lt;table border="1" cellpadding="10"&gt;`<br/> 单元格间距：cellspacing属性：`&lt;table border="1" cellspacing="10"&gt;`<br/> 向表格添加背景颜色：`&lt;table border="1" bgcolor="red"&gt;`<br/> 向表格添加背景图像：`&lt;table border="1" background="/i/eg_bg_07.gif"&gt;`<br/> 向表格单元添加背景颜色：`&lt;td bgcolor="red"&gt;First&lt;/td&gt;`<br/> 向表格单元添加背景图像`&lt;td background="/i/eg_bg_07.gif"&gt; Second&lt;/td&gt;`<br/> [表格align属性](http://www.w3school.com.cn/tiy/t.asp?f=html_table_align)<br/> [框架(fram)属性](http://www.w3school.com.cn/tiy/t.asp?f=html_table_frame):`&lt;table frame="above"&gt;`

