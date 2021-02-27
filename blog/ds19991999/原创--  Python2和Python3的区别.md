# 原创
：  Python2和Python3的区别

# Python2和Python3的区别

### 目录

### print和input

Python2等价版本

```
print "fish"
print ("fish") #注意print后面有个空格
print("fish") #print()不能带有任何其它参数

```

Python3中没有print语句，由print()函数代替,可以有空格

```
&gt;&gt;&gt; print("fish", "panda", sep='#')
fish#panda

```

在python2.x中raw_input()和input( )，两个函数都存在:

python3.x中raw_input()和input( )进行了整合，去除了raw_input()，input()函数接收任意任性输入，将所有输入默认为字符串处理，并返回字符串类型。

### Unicode

```
# Python2
str = "我爱北京天安门"
str

```

```
'\xe6\x88\x91\xe7\x88\xb1\xe5\x8c\x97\xe4\xba\xac\xe5\xa4\xa9\xe5\xae\x89\xe9\x97\xa8'

```

```
str = u"我爱北京天安门"
str

```

```
u'\u6211\u7231\u5317\u4eac\u5929\u5b89\u95e8'

```

```
# Python3
str = "我爱北京天安门"
str    

```

```
'我爱北京天安门'

```

### 除法运算

**Python中的除法有两个运算符，/和//**

首先来说`/`除法:

```
#python2
4/3

```

```
1

```

```
# python 3.x中/除法对于整数之间的相除，结果也会是浮点数
4/3

```

```
1.3333333333333333

```

对于//除法:

```
# python2
-1//2

```

```
-1

```

```
# python3
-1//2

```

```
-1

```

### 异常

Python 3 中我们现在使用 as 作为关键词，捕获异常的语法由 `except exc, var` 改为 `except exc as var`。

### xrange

### 八进制字面量表示

```
# Python2
print 0o1000,01000

```

```
512 512

```

```
# Python3
print(0o1000)

```

```
512

```

```
print(01000)

```

```
  File "&lt;ipython-input-3-d096c5298f8d&gt;", line 1
    print(01000)
              ^
SyntaxError: invalid token

```

### 不等运算符

### 去掉了repr表达式``

### 多个模块被改名

<th align="center">旧的名字</th><th align="center">新的名字</th>
|------
<td align="center">`_winreg`</td><td align="center">winreg</td>
<td align="center">ConfigParser</td><td align="center">configparser</td>
<td align="center">copy_reg</td><td align="center">copyreg</td>
<td align="center">Queue</td><td align="center">queue</td>
<td align="center">SocketServer</td><td align="center">socketserver</td>
<td align="center">repr</td><td align="center">reprlib</td>

httplib, BaseHTTPServer, CGIHTTPServer, SimpleHTTPServer, Cookie, cookielib被合并到http包内。取消了exec语句，只剩下exec()函数

### 数据类型

```
# python3
b = b'china'
type(b)

```

```
bytes

```

### map、filter 和 reduce

```
# python2中他们都是内置函数，输出都是列表
&gt;&gt;&gt; map
&lt;built-in function map&gt;
&gt;&gt;&gt; filter
&lt;built-in function filter&gt;
&gt;&gt;&gt; map(lambda x:x *2, [1,2,3])
[2, 4, 6]
&gt;&gt;&gt; filter(lambda x:x %2 ==0,range(10))
[0, 2, 4, 6, 8]
&gt;&gt;&gt;

```

```
# python3中他们变成了类，返回结果变成了可迭代对象
&gt;&gt;&gt; map
&lt;class 'map'&gt;
&gt;&gt;&gt; map(print,[1,2,3])
&lt;map object at 0x10d8bd400&gt;
&gt;&gt;&gt; filter
&lt;class 'filter'&gt;
&gt;&gt;&gt; filter(lambda x:x % 2 == 0, range(10))
&lt;filter object at 0x10d8bd3c8&gt;
&gt;&gt;&gt; f =filter(lambda x:x %2 ==0, range(10))
&gt;&gt;&gt; next(f)
0
&gt;&gt;&gt; next(f)
2
&gt;&gt;&gt; next(f)
4
&gt;&gt;&gt; next(f)
6

```

注意：Python2中，next()函数 and .next()方法都能用，Python3中只有next()函数

### For循环变量和全局命名空间泄漏

```
# python2
i = 1
print 'before: i =', i
print 'comprehension: ', [i for i in range(5)]
print 'after: i =', i

```

```
 before: i = 1
comprehension:  [0, 1, 2, 3, 4]
after: i = 4

```

```
# python3
i = 1
print('before: i =', i)
print('comprehension:', [i for i in range(5)])
print('after: i =', i)

```

```
before: i = 1
comprehension: [0, 1, 2, 3, 4]
after: i = 1

```

### 返回可迭代对象，而不是列表

```
# python2
print range(3)
print type(range(3))

```

```
[0, 1, 2]
&lt;type 'list'&gt;

```

```
# python3
print(range(3))
print(type(range(3)))
print(list(range(3)))

```

```
range(0, 3)
&lt;class 'range'&gt;
[0, 1, 2]

```

Python 3 中一些经常使用到的不再返回列表的函数和方法：

```
zip()
map()
filter()
dictionary’s .keys() method
dictionary’s .values() method
dictionary’s .items() method

```

### 参考
