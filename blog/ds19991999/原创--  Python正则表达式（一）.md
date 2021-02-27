# 原创
：  Python正则表达式（一）

# Python正则表达式（一）

# 正则表达式

> 
参考：[正则表达式](https://github.com/CyC2018/Interview-Notebook/blob/master/notes/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F.md)


## 一、概述

## 二、匹配单个字符

```
# 正则表达式
nam.
# 匹配结果
My name is DS中的name

```

## 三、匹配一组字符串

```
abcd
abc1
abc2
# 匹配到了abcd

```

## 四、使用元字符

### 匹配空白字符

<th align="center">元字符</th><th align="center">说明</th>
|------
<td align="center">[\b]</td><td align="center">回退（删除一个字符）</td>
<td align="center">\f</td><td align="center">换页符</td>
<td align="center">\n</td><td align="center">换行符</td>
<td align="center">\r</td><td align="center">回车符</td>
<td align="center">\t</td><td align="center">制表符</td>
<td align="center">\v</td><td align="center">垂直制表符</td>

### 匹配特定的字符类别

#### 数字元字符

<th align="center">元字符</th><th align="center">说明</th>
|------
<td align="center">\d</td><td align="center">数字字符，等价于[0-9]</td>
<td align="center">\D</td><td align="center">非数字字符，等价于[^0-9]</td>

#### 字母数字元字符

<th align="center">元字符</th><th align="center">说明</th>
|------
<td align="center">\w</td><td align="center">大小写字母，下划线和数字，等价于[a-zA-Z0-9]</td>
<td align="center">\W</td><td align="center">对\w取非</td>

#### 空白字符元字符

<th align="center">元字符</th><th align="center">说明</th>
|------
<td align="center">\s</td><td align="center">任何一个空白字符，等价于[\f\n\r\t\v]</td>
<td align="center">\S</td><td align="center">对\s取非</td>

## 五、重复匹配

```
[\w.]+@\w+\.\w+
[\w.]+@[\w]+[\.][\w]+

```

## 六、位置匹配

### 单词边界

### 字符串边界

## 七、使用子表达式

```
192.168.0.1
00.00.00.00
555.555.555.555

```

匹配到了第一个

## 八、回溯引用

```
&lt;h1&gt;x&lt;/h1&gt;
&lt;h2&gt;x&lt;/h2&gt;
&lt;h3&gt;x&lt;/h1&gt;
匹配到了前面两个

```

<th align="center">元字符</th><th align="center">说明</th>
|------
<td align="center">\l</td><td align="center">把下个字符转换成小写</td>
<td align="center">\u</td><td align="center">把下个字符转换成大写</td>
<td align="center">\L</td><td align="center">把\L和\E之间的字符全部转换成小写</td>
<td align="center">\U</td><td align="center">把\U和\E之间的字符全部转换成大写</td>
<td align="center">\E</td><td align="center">结束\L或者\U</td>

## 九、前后查找

## 十、嵌入条件

### 回溯引用条件

### 前后查找条件
