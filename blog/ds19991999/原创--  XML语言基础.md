# 原创
：  XML语言基础

# XML语言基础
1. #XML声明，定义版本（1.0）和使用编码（ISO-8859-1 = Latin-1/西欧字符集）1. &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;1. #文档**根元素** 1. &lt;note&gt;1. #接下来四行描述根的4个子元素1. &lt;to&gt;George&lt;/to&gt;1. &lt;from&gt;John&lt;/from&gt;1. &lt;heading&gt;Reminder&lt;/heading&gt;1. &lt;body&gt;Don't forget the meeting!&lt;/body&gt;1. #定义**根元素的结尾**1. &lt;/note&gt;| &amp;lt;| &lt;| 小于
| &amp;gt;| &gt;| 大于
| &amp;amp;| &amp;| 和号
| &amp;apos;| '| 单引号
| &amp;quot;| "| 双引号
1. 名称可以含字母、数字以及其他的字符1. 名称不能以数字或者标点符号开始1. 名称不能以字符 “xml”（或者 XML、Xml）开始1. 名称不能包含空格1. 最好使用&lt;book_title&gt;这种命名方式1. 属性无法包含多重的值（元素可以）1. 属性无法描述树结构（元素可以）1. 属性不易扩展（为未来的变化）1. 属性难以阅读和维护