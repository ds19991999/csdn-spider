# 原创
：  HTML语言笔记（一）

# HTML语言笔记（一）

 参考教程： [HTML教程](http://www.w3school.com.cn/html/index.asp)

##  1.简介

 HTML是**超文本标记语言**(Hyper Text Markup Language)，使用标记标签来描述网页。HTML 标签是由尖括号包围的关键词，比如 ，通常是成对出现的。Web的作用就是读取HTML文档，并以网页的形式来显示他们。
<li> &lt;html&gt; 与 &lt;/html&gt; 之间的文本描述网页  
     <hr/> </li><li> &lt;body&gt; 与 &lt;/body&gt; 之间的文本是可见的页面内容  
     <hr/> </li><li> &lt;h1&gt; 与 &lt;/h1&gt; 之间的文本被显示为1级标题  
     <hr/> </li><li> &lt;p&gt; 与 &lt;/p&gt; 之间的文本被显示为段落  
     <hr/> </li>
---


---


##  2.编辑器

 推荐使用Notepad或者TextEdit来编写HTML。

##  3.基础

 标题 &lt;h1&gt; - &lt;h6&gt;共六级<br/> 段落 &lt;p&gt; 标签<br/> 链接 &lt;a&gt; 标签，href属性指定链接的地址<br/> &lt;body&gt; 元素定义了 HTML 文档的主体，&lt;html&gt; 元素定义了整个 HTML 文档。`&lt;a href="http://www.w3school.com.cn"&gt;This is a link&lt;/a&gt;`<br/> 图像&lt;**img**&gt;标签 包含一些指定图像目录，大小。`&lt;img src="w3school.jpg" width="104" height="142" /img&gt;`

##  4.元素

 基本元素语法:

> 
HTML 元素以开始标签起始<br/> HTML 元素以结束标签终止<br/> 元素的内容是开始标签与结束标签之间的内容<br/> 某些 HTML 元素具有空内容（empty content）<br/> 空元素在开始标签中进行关闭（以开始标签的结束而结束）<br/> 大多数 HTML 元素可拥有属性


 示例：
<li> &lt;html&gt;  
     <hr/> </li><li>   
     <hr/> </li><li> &lt;body&gt;  
     <hr/> </li><li> &lt;p&gt;This is my first paragraph.&lt;/p&gt;  
     <hr/> </li><li> &lt;/body&gt;  
     <hr/> </li><li>   
     <hr/> </li><li> &lt;/html&gt;  
     <hr/> </li>
---


---


---


 没有内容的 HTML 元素被称为空元素，空元素是在开始标签中关闭的（无关闭标签），&lt;br&gt; 就是没有关闭标签的空元素（&lt;br&gt; 标签定义换行），单但我们最好用&lt;**br /**&gt;。**HTML标签对大小写不敏感**。

##  5.属性(加引号)

 [完整的HTML参考手册](http://www.w3school.com.cn/tags/index.asp)、[HTML标准属性参考手册](http://www.w3school.com.cn/tags/html_ref_standardattributes.asp)<br/> 标题居中`h1 align="center"&gt;This is heading 1&lt;/h1&gt; #弃用`<br/> 背景颜色`&lt;body bgcolor="yellow"&gt; #弃用`<br/> 表格&lt;table&gt;标签`&lt;table border="1"&gt; #拥有关于表格边框的附加信息`<br/> 属性值本身就含有双引号，那么你必须使用单引号`name='Bill "helloworld" Gates'`<br/> 常用HTML属性：

| 属性| 值| 描述
|------
| class| classname| 规定元素的类名(classname)
| id| id| 规定元素的唯一id
| style| style_defination| 规定元素的行内样式(inline style)
| title| text| 规定元素的额外信息(可在工具提示中显示)

##  6.标题 &lt;h1&gt;

 浏览器会自动地在标题的前后添加空行，默认情况下，HTML 会自动地在块级元素前后添加一个额外的空行，比如段落、标题元素前后。<br/> 水平线:&lt;hr /&gt; 标签在 HTML 页面中创建水平线。<br/> 注释：`&lt;!-- This is a comment --&gt;`<br/> 当显示页面时，浏览器会移除源代码中多余的空格和空行。所有连续的空格或空行都会被算作一个空格。需要注意的是，HTML 代码中的所有连续的空行（换行）也被显示为一个空格。

##  7.样式

 [style属性](http://www.w3school.com.cn/tiy/t.asp?f=html_styles):提供了一种改变所有HTML元素的样式的通用方法，淘汰了”旧的“bgcolor属性([CSS教程](http://www.w3school.com.cn/css/index.asp))<br/> 应该**避免使用下面这些标签的属性**：

| 标签| 描述
|------
| &lt;center&gt;| 定义居中的内容
| &lt;font&gt;和&lt;basfont&gt;| 定义HTML字体
| &lt;s&gt;和&lt;strike&gt;| 定义删除线文本
| &lt;u&gt;| 定义下划线文本

| 属性| 描述
|------
| align| 定义文本的对齐方式
| bgcolor| 定义背景颜色
| color| 定义文本颜色

 **示例：**<br/> 颜色示例：
<li> &lt;html&gt;  
     <hr/> </li><li>   
     <hr/> </li><li> &lt;body style="background-color:yellow"&gt;  
     <hr/> </li><li> &lt;h2 style="background-color:red"&gt;This is a heading&lt;/h2&gt;  
     <hr/> </li><li> &lt;p style="background-color:green"&gt;This is a paragraph.&lt;/p&gt;  
     <hr/> </li><li> &lt;/body&gt;  
     <hr/> </li><li>   
     <hr/> </li><li> &lt;/html&gt;  
     <hr/> </li>
---


---


---


---


 字体、颜色和尺寸：
<li> &lt;html&gt;  
     <hr/> </li><li>   
     <hr/> </li><li> &lt;body&gt;  
     <hr/> </li><li> &lt;h1 style="font-family:verdana"&gt;A heading&lt;/h1&gt;  
     <hr/> </li><li> &lt;p style="font-family:arial;color:red;font-size:20px;"&gt;A paragraph.&lt;/p&gt;  
     <hr/> </li><li> &lt;/body&gt;  
     <hr/> </li><li>   
     <hr/> </li><li> &lt;/html&gt;  
     <hr/> </li>
---


---


---


---


 [text-align](http://www.w3school.com.cn/tiy/t.asp?f=html_headeralign)属性规定了元素中文本的水平对齐方式：
<li> &lt;html&gt;  
     <hr/> </li><li>   
     <hr/> </li><li> &lt;body&gt;  
     <hr/> </li><li> &lt;h1 style="text-align:center"&gt;This is a heading&lt;/h1&gt;  
     <hr/> </li><li> &lt;p&gt;The heading above is aligned to the center of this page.&lt;/p&gt;  
     <hr/> </li><li> &lt;/body&gt;  
     <hr/> </li><li>   
     <hr/> </li><li> &lt;/html&gt;  
     <hr/> </li>
---


---


---


---

