# 原创
：  Python Tutorial 2.7.14总结

# Python Tutorial 2.7.14总结

### 目录

## 编码风格

[**PEP 8**](https://www.python.org/dev/peps/pep-0008) 引入了大多数项目遵循的风格指导，以下是比较实用的编码风格：

## 数据结构

### 列表常用函数

<th align="center">对象方法</th><th align="left">描述</th>
|------
<td align="center">`list.append`(**x**)</td><td align="left">把一个元素添加到链表的结尾（入栈）</td>
<td align="center">`list.pop`([**i**])</td><td align="left">从链表的指定位置删除元素，**并将其返回**，如果没有指定索引，`a.pop()` 返回最后一个元素。（出栈）</td>
<td align="center">`list.sort`(**cmp=None**, **key=None**, **reverse=False**)</td><td align="left">对链表中的元素就地进行排序</td>
<td align="center">`list.reverse`()</td><td align="left">就地倒排链表中的元素</td>
<td align="center">`list.remove`(**x**)</td><td align="left">删除链表中值为 **x** 的第一个元素。如果没有这样的元素，就会返回一个错误。</td>
<td align="center">`list.insert`(**i**, **x**)</td><td align="left">在指定位置插入一个元素</td>
<td align="center">`list.index`(**x**)</td><td align="left">返回链表中第一个值为 **x** 的元素的索引，如果没有匹配的元素就会返回一个错误</td>
<td align="center">`list.count`(**x**)</td><td align="left">返回 **x** 在链表中出现的次数</td>
<td align="center">`list.extend`(**L**)</td><td align="left">将一个给定列表中的所有元素都添加到另一个列表中，相当于 `a[len(a):] = L`</td>

队列实现`collections.deque()`，`append()`和`popleft()`

```
&gt;&gt;&gt; from collections import deque
&gt;&gt;&gt; queue = deque(["Eric", "John", "Michael"])
&gt;&gt;&gt; queue.append("Terry")           # Terry arrives
&gt;&gt;&gt; queue.append("Graham")          # Graham arrives
&gt;&gt;&gt; queue.popleft()                 # The first to arrive now leaves
'Eric'
&gt;&gt;&gt; queue.popleft()                 # The second to arrive now leaves
'John'
&gt;&gt;&gt; queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])

```

### 函数式编程工具

对于链表： [filter()](https://docs.python.org/2.7/library/functions.html#filter)，[map()](https://docs.python.org/2.7/library/functions.html#map) 以及 [reduce()](https://docs.python.org/2.7/library/functions.html#reduce)

```
&gt;&gt;&gt; def f(x): return x % 3 == 0 or x % 5 == 0
...
&gt;&gt;&gt; filter(f, range(2, 25))
[3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24]

```

```
&gt;&gt;&gt; def cube(x): return x*x*x
...
&gt;&gt;&gt; map(cube, range(1, 11))
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

```

```
&gt;&gt;&gt; def add(x,y): return x+y
...
&gt;&gt;&gt; reduce(add, range(1, 11))
55

```

列表推导式：

```
squares = [x**2 for x in range(10)]

```

### 元组和序列

元组不可变`&gt;&gt;&gt; singleton = 'hello', # &lt;-- note trailing comma`

### 集合

集合是一个无序不重复元素的集，基本功能包括关系测试和消除重复元素

```
&gt;&gt;&gt; a = set('abracadabra')
&gt;&gt;&gt; a                                  # unique letters in a
set(['a', 'r', 'b', 'c', 'd'])
&gt;&gt;&gt; a = {x for x in 'abracadabra' if x not in 'abc'}
&gt;&gt;&gt; a
{'r', 'd'}

```

### 字典

创建字典：

```
&gt;&gt;&gt; dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'jack': 4098, 'guido': 4127}
&gt;&gt;&gt; {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}

```

### 循环技巧

在**序列**中循环时，索引位置和对应值可以使用 [enumerate()](https://docs.python.org/2.7/library/functions.html#enumerate) 函数同时得到:

```
list = ['tic', 'tac', 'toe']
&gt;&gt;&gt; for i, v in enumerate(list):
...     print(i, v)
...
0 tic
1 tac
2 toe

```

多个循环，使用`zip()`整体打包循环：

```
&gt;&gt;&gt; questions = ['name', 'quest', 'favorite color']
&gt;&gt;&gt; answers = ['lancelot', 'the holy grail', 'blue']
&gt;&gt;&gt; for q, a in zip(questions, answers):
...     print 'What is your {0}?  It is {1}.'.format(q, a)
...
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.

```

遍历字典时，使用 `iteritems()` 方法可以同时得到键和对应的值。:

```
&gt;&gt;&gt; knights = {'gallahad': 'the pure', 'robin': 'the brave'}
&gt;&gt;&gt; for k, v in knights.iteritems():
...     print k, v
...
gallahad the pure
robin the brave

```

## 模块

### 包

包内引用：包中使用了子包结构，可以按绝对位置从相邻的包中引入子模块

```
from . import echo
from .. import formats
from ..filters import equalizer

```

## 输入与输出

### 格式化输出

```
&gt;&gt;&gt; s = 'Hello, world.'
&gt;&gt;&gt; str(s)
'Hello, world.'
&gt;&gt;&gt; repr(s)
"'Hello, world.'"

```

```
&gt;&gt;&gt; table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
&gt;&gt;&gt; print 'Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table)
Jack: 4098; Sjoerd: 4127; Dcab: 8637678

```

```
&gt;&gt;&gt; import math
&gt;&gt;&gt; print 'The value of PI is approximately %5.3f.' % math.pi
The value of PI is approximately 3.142.

```

## 文件读写

### 使用 [json](https://docs.python.org/2.7/library/json.html#module-json) 存储结构化数据

标准模块 [json](https://docs.python.org/2.7/library/json.html#module-json) 可以接受 Python 数据结构，并将它们转换为字符串表示形式；此过程称为 **序列化**。从字符串表示形式重新构建数据结构称为 **反序列化**。

> 
JSON 格式经常用于现代应用程序中进行数据交换。许多程序员都已经熟悉它了，使它成为相互协作的一个不错的选择。


```
&gt;&gt;&gt; json.dumps([1, 'simple', 'list'])
'[1, "simple", "list"]'

```

[dumps()](https://docs.python.org/2.7/library/json.html#json.dumps) 函数的另外一个变体 [dump()](https://docs.python.org/2.7/library/json.html#json.dump)，直接将对象序列化到一个文件。所以如果 `f` 是为写入而打开的一个 [文件对象](https://docs.python.org/2.7/glossary.html#term-file-object)，我们可以这样做:`json.dump(x, f)`

`x = json.load(f)`：重新解码对象。

## 错误和异常

```
try:
    raise ...
except Exception as e:
    ...
finally:
    ...

```

## 类

### 迭代器

大多数容器对象都可以用 [for](https://docs.python.org/2.7/reference/compound_stmts.html#for) 遍历:

在后台，[for](https://docs.python.org/2.7/reference/compound_stmts.html#for) 语句在容器对象中调用 [iter()](https://docs.python.org/2.7/library/functions.html#iter)。 该函数返回一个定义了 [next()](https://docs.python.org/2.7/library/stdtypes.html#iterator.next) 方法的迭代器对象，它在容器中逐一访问元素。没有后续的元素时，[next()](https://docs.python.org/2.7/library/stdtypes.html#iterator.next) 抛出一个 [StopIteration](https://docs.python.org/2.7/library/exceptions.html#exceptions.StopIteration) 异常通知 [for](https://docs.python.org/2.7/reference/compound_stmts.html#for) 语句循环结束。以下是其工作原理的示例:

```
&gt;&gt;&gt; s = 'abc'
&gt;&gt;&gt; it = iter(s)
&gt;&gt;&gt; it
&lt;iterator object at 0x00A1DB50&gt;
&gt;&gt;&gt; next(it)
'a'
&gt;&gt;&gt; next(it)
'b'
&gt;&gt;&gt; next(it)
'c'
&gt;&gt;&gt; next(it)
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in ?
    next(it)
StopIteration

```

### 给自己的类定义迭代器

定义一个 [`__iter__()`](https://docs.python.org/2.7/reference/datamodel.html#object.__iter__) 方法，使其返回一个带有 [next()](https://docs.python.org/2.7/library/stdtypes.html#iterator.next) 方法的对象。如果这个类已经定义了 [next()](https://docs.python.org/2.7/library/stdtypes.html#iterator.next)，那么 [`__iter__()`](https://docs.python.org/2.7/reference/datamodel.html#object.__iter__) 只需要返回 `self`:

```
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
&gt;&gt;&gt; rev = Reverse('spam')
&gt;&gt;&gt; iter(rev)
&lt;__main__.Reverse object at 0x00A1DB50&gt;
&gt;&gt;&gt; for char in rev:
...     print(char)
...
m
a
p
s

```

### 生成器

[yield](https://docs.python.org/2.7/reference/simple_stmts.html#yield) 语句，每次 [next()](https://docs.python.org/2.7/library/functions.html#next) 被调用时，生成器回复它脱离的位置(它记忆语句最后一次执行的位置和所有的数据值)。当发生器终结时，还会自动抛出 [StopIteration](https://docs.python.org/2.7/library/exceptions.html#exceptions.StopIteration)异常。

```
&gt;&gt;&gt; sum(i*i for i in range(10))                 # sum of squares
285

&gt;&gt;&gt; xvec = [10, 20, 30]
&gt;&gt;&gt; yvec = [7, 5, 3]
&gt;&gt;&gt; sum(x*y for x,y in zip(xvec, yvec))         # dot product
260

&gt;&gt;&gt; from math import pi, sin
&gt;&gt;&gt; sine_table = {x: sin(x*pi/180) for x in range(0, 91)}

&gt;&gt;&gt; unique_words = set(word  for line in page  for word in line.split())

&gt;&gt;&gt; valedictorian = max((student.gpa, student.name) for student in graduates)

&gt;&gt;&gt; data = 'golf'
&gt;&gt;&gt; list(data[i] for i in range(len(data)-1, -1, -1))
['f', 'l', 'o', 'g']

```

## Python标准库概览

### 操作系统接口

```
&gt;&gt;&gt; import os
&gt;&gt;&gt; os.getcwd()      # Return the current working directory
'C:\\Python27'
&gt;&gt;&gt; os.chdir('/server/accesslogs')   # Change current working directory
&gt;&gt;&gt; os.system('mkdir today')   # Run the command mkdir in the system shell
0

# 文件管理
&gt;&gt;&gt; import shutil
&gt;&gt;&gt; shutil.copyfile('data.db', 'archive.db')
&gt;&gt;&gt; shutil.move('/build/executables', 'installdir')

# 从目录通配符搜索中生成文件列表
&gt;&gt;&gt; import glob
&gt;&gt;&gt; glob.glob('*.py')
['primes.py', 'random.py', 'quote.py']

```

### random

```
&gt;&gt;&gt; import random
&gt;&gt;&gt; random.choice(['apple', 'pear', 'banana'])
'apple'
&gt;&gt;&gt; random.sample(xrange(100), 10)   # sampling without replacement
[30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
&gt;&gt;&gt; random.random()    # random float
0.17970987693706186
&gt;&gt;&gt; random.randrange(6)    # random integer chosen from range(6)
4

```

### 互联网访问

用于处理从 urls 接收的数据的 [urllib2](https://docs.python.org/2.7/library/urllib2.html#module-urllib2) 以及用于发送电子邮件的 [smtplib](https://docs.python.org/2.7/library/smtplib.html#module-smtplib):

```
&gt;&gt;&gt; import urllib2
&gt;&gt;&gt; for line in urllib2.urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
...     line = line.decode('utf-8')  # Decoding the binary data to text.
...     if 'EST' in line or 'EDT' in line:  # look for Eastern Time
...         print line

&lt;BR&gt;Nov. 25, 09:43:32 PM EST

# 需要在 localhost 运行一个邮件服务器 
&gt;&gt;&gt; import smtplib
&gt;&gt;&gt; server = smtplib.SMTP('localhost')
&gt;&gt;&gt; server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
... """To: jcaesar@example.org
... From: soothsayer@example.org
...
... Beware the Ides of March.
... """)
&gt;&gt;&gt; server.quit()

```

### 日期和时间

```
&gt;&gt;&gt; # dates are easily constructed and formatted
&gt;&gt;&gt; from datetime import date
&gt;&gt;&gt; now = date.today()
&gt;&gt;&gt; now
datetime.date(2003, 12, 2)
&gt;&gt;&gt; now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
'12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'

&gt;&gt;&gt; # dates support calendar arithmetic
&gt;&gt;&gt; birthday = date(1964, 7, 31)
&gt;&gt;&gt; age = now - birthday
&gt;&gt;&gt; age.days
14368

```

### 数据压缩

[zlib](https://docs.python.org/2.7/library/zlib.html#module-zlib)，[gzip](https://docs.python.org/2.7/library/gzip.html#module-gzip)，[bz2](https://docs.python.org/2.7/library/bz2.html#module-bz2)，[zipfile](https://docs.python.org/2.7/library/zipfile.html#module-zipfile) 以及 [tarfile](https://docs.python.org/2.7/library/tarfile.html#module-tarfile)

```
&gt;&gt;&gt; import zlib
&gt;&gt;&gt; s = b'witch which has which witches wrist watch'
&gt;&gt;&gt; len(s)
41
&gt;&gt;&gt; t = zlib.compress(s)
&gt;&gt;&gt; len(t)
37
&gt;&gt;&gt; zlib.decompress(t)
b'witch which has which witches wrist watch'
&gt;&gt;&gt; zlib.crc32(s)
226805979

```

### 性能度量

[timeit](https://docs.python.org/2.7/library/timeit.html#module-timeit)

```
&gt;&gt;&gt; from timeit import Timer
&gt;&gt;&gt; Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
0.57535828626024577
&gt;&gt;&gt; Timer('a,b = b,a', 'a=1; b=2').timeit()
0.54962537085770791

```

> 
更多细节见：[http://www.pythondoc.com/pythontutorial27/stdlib2.html](http://www.pythondoc.com/pythontutorial27/stdlib2.html)<br/> 参考书籍：[http://www.pythondoc.com/pythontutorial27/](http://www.pythondoc.com/pythontutorial27/)

