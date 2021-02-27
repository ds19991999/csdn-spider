# 原创
：  Python基础教程总结（上）

# Python基础教程总结（上）

### 目录

> 
参考：[https://book.douban.com/subject/4866934/](https://book.douban.com/subject/4866934/) ，基于Python2.x.


## 第一章 基础知识

```
#!/usr/bin/python2
# coding=utf-8
chmod 755 hello.py #给Python脚本添加可执行权限
math.floor(num) #将给定的数值转换为小于或等于它的最小整数
math.ceil(num) #将给定的数值转换为大于或等于它的最小整数
math.sqrt(num) #计算平方根
&gt;&gt;&gt; foo=math.sqrt
&gt;&gt;&gt; foo(3)
1.7320508075688772
cmath.sqrt(-3) #复数模块，Python本身支持复数计算
r'C:\path\where' #原始字符串，其最后一个字符不能是反斜杠

```

```
&gt;&gt;&gt; temp = 43
&gt;&gt;&gt; print "The temperature is "+`temp`
The temperature is 43

```

<th align="center">函数</th>|描述
|------
<td align="center">abs(num)</td>|返回数字的绝对值
<td align="center">cmath.sqrt(num)</td>|返回平方根，也可以用于复数
<td align="center">pow(x,y[,z])</td>|x^y所求结果对z取模
<td align="center">repr(object)</td>|返回值的字符串表示形式
<td align="center">round(num[, ndigits])</td>|根据给定的精度对数字进行四舍五入

## 第二章 列表和元祖

**6中内建序列：列表、元祖、字符串、Unicode字符串、buffer对象、xrange对象**

列表可以修改，元祖不能。

```
&gt;&gt;&gt; list("Python")
['P', 'y', 't', 'h', 'o', 'n']
# 不替换原有元素得情况下插入新元素
&gt;&gt;&gt; num = [1,5]
&gt;&gt;&gt; num[1:1]=[2,3,4]
&gt;&gt;&gt; num
[1, 2, 3, 4, 5]

```

sort()有两个可选参数

```
&gt;&gt;&gt; x = ['sss',"sww1w","sqwsqwd","sddd"]
&gt;&gt;&gt; x.sort(key=len)
&gt;&gt;&gt; x
['sss', 'sddd', 'sww1w', 'sqwsqwd']
&gt;&gt;&gt; x = [4,5,2,4,231,24]
&gt;&gt;&gt; x.sort(reverse=True)  # 这里和seq.reverse()方法或reversed(seq)函数有区别
&gt;&gt;&gt; x
[231, 24, 5, 4, 4, 2]

```

注意只有一个元素的元组：`42,`必须要有一个逗号，元组中的`tupul()`函数相当于列表中的`list()`

```
&gt;&gt;&gt; tuple("Python")
('P', 'y', 't', 'h', 'o', 'n')
&gt;&gt;&gt; list("Python")
['P', 'y', 't', 'h', 'o', 'n']

```

```
cmp(x,y) # 比较x,y的大小，x&gt;y返回1，x&lt;y返回-1，x=y返回0

```

## 第三章 字符串

**字符串不可变**

```
# 个人感觉这种格式化字符串很好，一个字符串一个元组
&gt;&gt;&gt; format = "hello, %s. %s enough for ya?"
&gt;&gt;&gt; values = ('world','Hot')
&gt;&gt;&gt; print format % values
hello, world. Hot enough for ya?

```

表3-1 字符串转换类型，P46

str.find(“strings”)查找字串并返回，如果找到返回字串的左端索引，没找到返回-1，find(“strings”,1,3)，起始索引

sep.join(str):连接字符串列表并返回，sep是分割符字串，与split()相对，str.split(sep)

str.strip()，去掉字符串**两侧空格**字符串，str.strip(“ !*”)指定去掉两侧空格和！和*

str.lower()和str.upper()，大小写转换

str.replace(“aaa”,“bbb”)，把字符串中的aaa全都替换为bbb

```
from string import maketrans
table = maketrans("cs","kj") # 将c、s分别替换为k、j
strs="   ddd    dddwdd   eed       "
strs.translate(str)

```

string.capwords(str[, sep]) 使用split()函数将字符串str分割（sep为分割符），使用capitalize()函数将分割得到的各单词首字母大写，并且使用join()函数以sep为分隔符连接各单词

## 第四章 字典–映射

> 
字典无序，当索引不好用时用字典，字典的格式化字符串很常用P58


```
dic.clear() #清除字典中所有的项
dic.copy() #返回一个具有相同键值对的新字典----浅复制，不是副本 P60需要注意一下
from copy import deepcopy
dic.deepcopy() #这时不随原字典改变
&gt;&gt;&gt; {}.fromkeys(["name","age"]，可选默认值) #使用给定的键建立一个空字典
{'age': None, 'name': None}
dic.get("name") #访问键name，不存在返回None，否则返回键值
dic.has_key("name") #返回True或False
dic.items() #将字典所有项以列表的形式返回

dic.iteritems() #返回一个列表的迭代器
dic = {'age': None, 'name': None}
&gt;&gt;&gt; for k,v in dic.iteritems():
...     print k,v
...
age None
name None

dic.keys() # 以列表形式返回
dic.values()
dic.iterkeys() #返回键的迭代器
dic.itervalues() #返回值的迭代器
dic.pop("name") #删除并返回键值
dic.popitem() #弹出随机的项

# 不给定键的情况下设定键值
&gt;&gt;&gt; dic={}
&gt;&gt;&gt; dic.setdefault("name","N/A")
'N/A'

dic.update(x) #将字典dic更新到字典x

```

## 第五章 条件、循环和其他语句

假：`False 0 “” None () [] {}`，其他一切都是真

```
name = raw_input("Please enter your name: ") or "&lt;unknown&gt;"
就是说如果输入为空，则将name="&lt;unknown&gt;"

```

```
&gt;&gt;&gt; zip(range(5),xrange(8))
[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]

```

```
&gt;&gt;&gt; [x*x for x in range(10) if x%3==0]
[0, 9, 36, 81]
&gt;&gt;&gt; [(x,y) for x in range(3) for y in range(2)]
[(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]

```

```
# 这里的scope就是起到放置字符串命名空间的字典
&gt;&gt;&gt; from math import sqrt
&gt;&gt;&gt; scope={}
&gt;&gt;&gt; exec "sqrt =  1" in scope
&gt;&gt;&gt; sqrt(4)
2.0
&gt;&gt;&gt; scope["sqrt"]
1

# eval 用于求值，类似于exec的内建函数，eval会计算写在字符串中的Python表达式并返回值 P85

```

```
ord("a") #返回字符串a的值

```

## 第七章 抽象

> 
**多态**可以让用户对于**不知道是什么类的对象**进行方法调用；而**封装**是可以**不用关心对象是如何构建的**而直接进行使用。


```
class Secretive:
    def __inaccessible(self):
        ...
    def accessible(self):
        self.__inaccessible()
s = Secretive()
s.__inaccessible() # 会报错
s.accessible() #这样才是正常的，相当于调用
Secretive._Secretive__inaccessible

```

```
issubclass(SPAMFilter,Filter) # 判断一个类是否是另一个类的子类 返回True、False
SPAMFFilter.__base__ # 返回子类的基类
isinstance(s,Filter) #判断一个对象的实例是否是一个类的实例
s.__class__ # 返回对象s的类

```

## 第八章 异常

```
try raise [except else] finally
# 同一个try中except和finally不能同时使用

```

## 第九章 魔法方法、属性、迭代器

> 
魔法方法一般指`__future__`这样的双下划线


`__init__`：构造方法

`__del__`：析构方法，在对象被垃圾回收之前调用，但调用的时间不可知，所以我们一般不用
