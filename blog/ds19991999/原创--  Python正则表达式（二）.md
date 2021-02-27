# 原创
：  Python正则表达式（二）

# Python正则表达式（二）

官方文档：[re](https://docs.python.org/3/library/re.html?highlight=re#module-re)

# Contents

## re模块

① Python 1.5.2 版中新增；2.4 版中增加 flags 参数

② Python 2.2 版中新增；2.4 版中增加 flags 参数

③ Python 2.7 和 3.1 版中增加 flags 参数

主要学习match()和 search()，以及 compile()函数

## re常用函数

### 使用 match()方法匹配字符串

`match(pattern ， string ， flags=0)`

尝试使用带有可选的标记的正则表达式的模式来匹配字符串。如果匹配成功，就返回匹配对象；如果失败，就返回 None

他是从字符串**起始部位开始匹配**,一旦第一个字符匹配失败，就是不匹配

匹配对象的 group()方法能够用于显示那个成功的匹配。

```
<code>import re
m = re.match('foo','foo')
if m is not None:
    regex1 = m.group()
regex1
</code>
```

```
'foo'

```

```
<code>m
</code>
```

```
&lt;_sre.SRE_Match at 0x522adb0&gt;

```

```
<code>m = re.match('foo','bar')
if m is not None:m.group()# 单行版本的if语句
print m  # 不匹配
</code>
```

```
None

```

**后面操作省去if语句**，实际开发要加上，避免 AttributeError 异常

```
<code>m = re.match("foo","food on the table")
m.group()
</code>
```

```
'foo'

```

```
<code>re.match("foo","food on the table").group()
</code>
```

```
'foo'

```

### 使用search()在一个字符串中查找模式（搜索与匹配的对比）

`search(pattern ， string ， flags=0)`

使用可选标记搜索字符串中**第一次出现的正则表达式模式**。如果匹配成功，则返回匹配对象；如果失败，则返回 None

```
<code>m = re.match('foo','seafood')
if m is not None:print m.group()#匹配失败
</code>
```

```
<code>m = re.search('foo','searchfood')
if m is not None:regex3 = m.group()
print regex3 # 搜索成功，但是匹配失败
</code>
```

```
foo

```

### 匹配多个字符串（|）

```
<code>bt = 'bat|bet|bit'
m = re.match(bt,'bat')
if m is not None:print m.group() # Pytho2这里不加print就打印不出结果
</code>
```

```
bat

```

```
<code>m = re.match(bt,'blt')
if m is not None:print m.group() # 匹配失败
</code>
```

```
<code>m = re.match(bt, 'he bit me') 
if m is not None:print m.group() # 匹配失败：不能匹配字符串
</code>
```

```
<code>m = re.search(bt,'he bit me')
if m is not None:print m.group() 
</code>
```

```
bit

```

到这里match()和search()的区别基本上就清晰了

### 匹配任何单个字符

点号（.）不能匹配一个换行符\n 或者非字符，也就是说，一个空字符串

```
<code>anyend = '.end'
m = re.match(anyend, 'bend')
if m is not None:print m.group() 
</code>
```

```
bend

```

```
<code>m = re.match(anyend, 'end')
if m is not None:print m.group() # 匹配失败
</code>
```

```
<code>m = re.match(anyend, '\nend')
if m is not None:print m.group() # 除了\n之外的任何字符
</code>
```

```
<code>m = re.search(anyend, 'The end.')
if m is not None:str = m.group() # 可以匹配' '
str
</code>
```

```
' end'

```

```
<code>pat314 = '3.14'    # 表示正则表达式的点号
pi_pat = '3\.14'   # 表示字面量的点号 (dec. point)
m = re.match(pi_pat,'3.14')  #精确匹配
if m is not None:str = m.group() 
str
</code>
```

```
'3.14'

```

```
<code>m = re.match(pat314,'3014') # 点号匹配0
if m is not None:str = m.group() 
str
</code>
```

```
'3014'

```

```
<code>m = re.match(pat314,'3.14') # 点号匹配.
if m is not None:str = m.group() 
str
</code>
```

```
'3.14'

```

### 创建字符集([ ])

```
<code>m = re.match('[cr][23][dp][o2]', 'c3po')  # 匹配 'c3po'
if m is not None:str = m.group()
str
</code>
```

```
'c3po'

```

```
<code>m = re.match('r2d2|c3po', 'r2d2')# 匹配 'r2d2'
if m is not None:str = m.group()
str
</code>
```

```
'r2d2'

```

### 重复、特殊字符以及分组

简单电子邮件地址的正则表达式`（\w+@\w+\.com）`, `www.xxx.com`，仅仅允许 [xxx.com](http://xxx.com) 作为整个域名，必须修改现有的正则表达式.为了表示主机名是可选的，即`\w+@(\w+\.)?\w+\.com`

```
<code>patt  = '\w+@(\w+\.)?\w+\.com'  # “？”操作符来表示该模式出现零次或者一次
re.match(patt, 'nobody@xxx.com').group()
</code>
```

```
'nobody@xxx.com'

```

```
<code># 允许任意数量的中间子域名存在
patt = '\w+@(\w+\.)*\w+\.com'
re.match(patt, 'nobody@www.xxx.yyy.zzz.com').group()
</code>
```

```
'nobody@www.xxx.yyy.zzz.com'

```

更进一步

```
<code>m = re.match('(\w\w\w)-(\d\d\d)','abc-123')
if m is not None:str = m.group()
str
</code>
```

```
'abc-123'

```

```
<code>m.group(1)  #子组1
</code>
```

```
'abc'

```

```
<code>m.group(2)
</code>
```

```
'123'

```

```
<code>m.groups()
</code>
```

```
('abc', '123')

```

更具体的分组操作

```
<code>m = re.match('ab','ab')
m.group()
</code>
```

```
'ab'

```

```
<code>m.groups()  # 只抓取子组信息
</code>
```

```
()

```

```
<code>m = re.match('(ab)','ab')
m.group()
</code>
```

```
'ab'

```

```
<code>m.group(1)
</code>
```

```
'ab'

```

```
<code>m.groups() # 注意到元祖里面如果只有一个元素，需要加一个','号
</code>
```

```
('ab',)

```

```
<code>m = re.match('(a(b))', 'ab') # 两个子组
m.group()
</code>
```

```
'ab'

```

```
<code>m.group(1)
</code>
```

```
'ab'

```

```
<code>m.group(2)
</code>
```

```
'b'

```

```
<code>m.groups()
</code>
```

```
('ab', 'b')

```

### 匹配字符串的起始和结尾以及单词边界

更多用于表示搜索而不是匹配

```
<code>m = re.search('The','The end.')
if m is not None: print m.group()
</code>
```

```
The

```

```
<code>m = re.search('^The','end. The')
if m is not None:print m.group()
</code>
```

```
<code>m = re.search(r'\bthe','bite the dog')# 在边界
if m is not None: print m.group()
</code>
```

```
the

```

```
<code>m = re.search(r'\bthe', 'bitethe dog') # 有边界
if m is not None: print m.group()
</code>
```

```
<code>m = re.search(r'\Bthe', 'bitethe dog') # 有边界
if m is not None: print m.group()
</code>
```

```
the

```

### 使用 findall()和 finditer()查找每一次出现的位置

```
findall(pattern ， string [, flags] )

```

查找字符串中所有（非重复）出现的正则表达式模式，并返回一个匹配列表

```
finditer(pattern ， string [, flags] )

```

与 findall()函数相同，但返回的不是一个列表，而是一个迭代器。对于每一次匹配，迭<br/> 代器都返回一个匹配对象

```
<code>re.findall('car','car')
</code>
```

```
['car']

```

```
<code>re.findall('car','scary')
</code>
```

```
['car']

```

```
<code>re.findall('car','carry the barcardi to the car')
</code>
```

```
['car', 'car', 'car']

```

```
<code>s = 'This and that.'
re.findall(r'(th\w+) and (th\w+)',s,re.I)
</code>
```

```
[('This', 'that')]

```

```
<code>re.finditer(r'(th\w+) and (th\w+)', s,re.I).next().groups()
</code>
```

```
('This', 'that')

```

```
<code>re.finditer(r'(th\w+) and (th\w+)', s,re.I).next().group(1)
</code>
```

```
'This'

```

```
<code> [g.groups() for g in re.finditer(r'(th\w+) and (th\w+)',s, re.I)]
</code>
```

```
[('This', 'that')]

```

多重匹配

```
<code>re.findall(r'(th\w+)', s, re.I)
</code>
```

```
['This', 'that']

```

```
<code>it = re.finditer(r'(th\w+)', s, re.I)
g = it.next()
g.groups()
</code>
```

```
('This',)

```

```
<code>g.group(1)
</code>
```

```
'This'

```

```
<code>g = it.next()
g.groups()
</code>
```

```
('that',)

```

```
<code>g.group(1)
</code>
```

```
'that'

```

```
<code>[g.group(1) for g in re.finditer(r'(th\w+)',s,re.I)]
</code>
```

```
['This', 'that']

```

### 使用 sub()和 subn()搜索与替换

两者几乎一样，都是将某字符串中所有匹配正则表达式的部分进行某种形式的替换，但它也可能是一个函数，该函数返回一个用来替换的字符串。

subn()还返回一个表示替换的总数，**替换后的字符串和表示替换总数的数字**一起作为一个拥有两个元素的元组返回。

```
<code>re.sub('X', 'Mr. Smith', 'attn: X\n\nDear X,\n')
</code>
```

```
'attn: Mr. Smith\n\nDear Mr. Smith,\n'

```

```
<code>re.subn('X', 'Mr. Smith', 'attn: X\n\nDear X,\n')
</code>
```

```
('attn: Mr. Smith\n\nDear Mr. Smith,\n', 2)

```

```
<code>print re.sub('X', 'Mr. Smith', 'attn: X\n\nDear X,\n')
</code>
```

```
attn: Mr. Smith

Dear Mr. Smith,

```

```
<code>re.sub('[ae]', 'X', 'abcdef')
</code>
```

```
'XbcdXf'

```

```
<code>re.subn('[ae]', 'X', 'abcdef')
</code>
```

```
('XbcdXf', 2)

```

**另一种分组编号：**

group（）方法除了能够取出匹配分组编号外，还可以使用\N，其中 N 是在替换字符串中使用的分组编号

```
<code>re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})',r'\2/\1/\3', '2/20/91') # 分组重排
</code>
```

```
'20/2/91'

```

```
<code>re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})',r'\2/\1/\3', '2/20/1991')
</code>
```

```
'20/2/1991'

```

### 在限定模式上使用 split()分隔字符串

```
<code>DATA = (
    'Mountain View, CA 94040',
    'Sunnyvale, CA',
    'Los Altos, 94023',
    'Cupertino 95014',
    'Palo Alto CA',
    )
for datum in DATA:
    # 如果空格紧跟在五个数字（ZIP 编码）或者两个大写字母（美国联邦州缩
    # 写）之后，就用 split 语句分割该空格。
    print re.split(', |(?= (?:\d{5}|[A-Z]{2})) ', datum) 
</code>
```

```
['Mountain View', 'CA', '94040']
['Sunnyvale', 'CA']
['Los Altos', '94023']
['Cupertino', '95014']
['Palo Alto', 'CA']

```

### 扩展符号

** i不区分大小写 **

```
<code>re.findall(r'(?i)yes', 'yes? Yes. YES!!')
</code>
```

```
['yes', 'Yes', 'YES']

```

```
<code>re.findall(r'(?i)th\w+', 'The quickest way is through thistunnel.')
</code>
```

```
['The', 'through', 'thistunnel']

```

```
<code>re.findall(r'(?im)(th[\w ]+)',"""
    This line is the first,
    another line,
    that line, it's the best
    """)
# 这里貌似书籍翻译错了
</code>
```

```
['This line is the first', 'ther line', 'that line', 'the best']

```

```
<code>re.findall(r'th.+', '''
    The first line
    the second line
    the third line
    ''')
</code>
```

```
['the second line', 'the third line']

```

x该标记允许用户通过抑制在正则表达式中使用空白符（除了在字符类中或者在反斜线转义中）来创建更易读的正则表达式

```
<code>re.search(r'''(?x)
    \((\d{3})\)             # 区号
    [ ]                     # 空白符
    (\d{3})                 # 前缀
    -                       # 横线
    (\d{4})                 # 终点数字
    ''', '(800) 555-1212').groups()
</code>
```

```
('800', '555', '1212')

```

(?:…)对部分正则表达式进行分组，但是**并不会保存该分组**用于后续的检索或者应用

```
<code>re.findall(r'http://(?:\w+\.)*(\w+\.com)',
           'http://google.com http://www.google.com http://code.google.com')
</code>
```

```
['google.com', 'google.com', 'google.com']

```

**对于正则表达式，尽量使用原始字符串**

## 正则表达式示例

### 复习jupyter魔法
1. 这个是Jupyter的魔法使用，将字符串写入文件，回顾一下算了,具体见笔记：<br/> [Ipython解释器](/notebooks/python-tools/02-ipython-interpreter.ipynb)
```
<code>%%writefile whodata.txt
wesley console Jun 20 20:33
wesley pts/9 Jun 22 01:38 (192.168.0.6)
wesley pts/1 Jun 20 20:33 (:0.0)
wesley pts/2 Jun 20 20:33 (:0.0)
wesley pts/4 Jun 20 20:33 (:0.0)
wesley pts/3 Jun 20 20:33 (:0.0)
wesley pts/5 Jun 20 20:33 (:0.0)
wesley pts/6 Jun 20 20:33 (:0.0)
wesley pts/7 Jun 20 20:33 (:0.0)
wesley pts/8 Jun 20 20:33 (:0.0) 
</code>
```

```
Overwriting whodata.txt

```
1. 加载文件
```
<code># %load whodata.txt
wesley console Jun 20 20:33
wesley pts/9 Jun 22 01:38 (192.168.0.6)
wesley pts/1 Jun 20 20:33 (:0.0)
wesley pts/2 Jun 20 20:33 (:0.0)
wesley pts/4 Jun 20 20:33 (:0.0)
wesley pts/3 Jun 20 20:33 (:0.0)
wesley pts/5 Jun 20 20:33 (:0.0)
wesley pts/6 Jun 20 20:33 (:0.0)
wesley pts/7 Jun 20 20:33 (:0.0)
wesley pts/8 Jun 20 20:33 (:0.0) 
</code>
```

```
  File "&lt;ipython-input-69-851b49c8cf42&gt;", line 2
    wesley console Jun 20 20:33
                 ^
SyntaxError: invalid syntax

```

```
<code>%%writefile test.py
print 'Hello world'
</code>
```

```
Writing test.py

```
1. 运行文件
```
<code>%run test.py
</code>
```

```
Hello world

```

```
<code>!python test.py
</code>
```

```
Hello world

```
1. 删除文件
```
<code>import os
os.remove('test.py')
</code>
```

```
<code>%ls
</code>
```

```
 驱动器 E 中的卷是 File Sharing
 卷的序列号是 8EC1-8F11

 E:\01-note\02-python27\python-essentials 的目录

2018/07/27  16:39    &lt;DIR&gt;          .
2018/07/27  16:39    &lt;DIR&gt;          ..
2018/07/27  16:37    &lt;DIR&gt;          .ipynb_checkpoints
2018/07/04  13:52            43,159 01-introduction-python.ipynb
2018/07/04  14:00             2,128 02-date-types.ipynb
2018/07/04  16:38            16,521 03-numbers.ipynb
2018/07/04  17:12            20,246 04-strings.ipynb
2018/07/04  17:24             6,082 05-indexing-slicing.ipynb
2018/07/17  10:46            17,320 06-lists.ipynb
2018/07/27  16:39            88,439 07-python-regular-expression.ipynb
2018/07/17  08:57             6,674 08-mutable-and-immutable-data-types.ipynb
2018/07/17  09:19             5,501 09-tuples.ipynb
2018/07/18  06:48             4,489 10-speed-comparison-between-list-&amp;-tuple.ipynb
2018/07/17  10:27            18,421 11-dictionary.ipynb
2018/07/17  10:56            14,120 12-set.ipynb
2018/07/17  11:09             3,317 13-frozen-sets.ipynb
2018/07/17  11:50            12,767 14-how-python-assignment-works.ipynb
2018/07/17  12:48             5,272 15-if-statement.ipynb
2018/07/17  13:19             7,893 16-loops.ipynb
2018/07/17  14:40             4,596 17-list-comprehension.ipynb
2018/07/17  15:04            11,776 18-functions.ipynb
2018/07/17  15:33            10,113 19-modules-and-packages.ipynb
2018/07/17  16:24            16,718 20-exceptions.ipynb
2018/07/17  16:30             2,893 21-warnings.ipynb
2018/07/17  16:57           177,920 22-file-IO.ipynb
2018/07/17  15:08               359 ex1.pyc
2018/07/17  15:19               739 ex2.pyc
2018/07/27  16:38               673 gendata.py
2018/07/27  16:38               255 retasklist.py
2018/07/27  16:38               152 whodata.py
2018/07/27  16:38               341 whodata.txt
              28 个文件        498,884 字节
               3 个目录 47,198,081,024 可用字节

```

### 正则表达式示例

```
<code>%%writefile whodata.py
import re
f = open('whodata.txt', 'r')
for eachLine in f:
    print re.split(r'\s\s+', eachLine)
f.close()
</code>
```

```
Overwriting whodata.py

```

```
<code>%run whodata.py
</code>
```

```
['wesley console Jun 20 20:33\n']
['wesley pts/9 Jun 22 01:38 (192.168.0.6)\n']
['wesley pts/1 Jun 20 20:33 (:0.0)\n']
['wesley pts/2 Jun 20 20:33 (:0.0)\n']
['wesley pts/4 Jun 20 20:33 (:0.0)\n']
['wesley pts/3 Jun 20 20:33 (:0.0)\n']
['wesley pts/5 Jun 20 20:33 (:0.0)\n']
['wesley pts/6 Jun 20 20:33 (:0.0)\n']
['wesley pts/7 Jun 20 20:33 (:0.0)\n']
['wesley pts/8 Jun 20 20:33 (:0.0) ']

```

#### 分割 POSIX 的 who 命令输出（[whodate.py](http://whodate.py))

```
<code>%%writefile whodata.py
import re
import os
with os.popen('whodata.txt', 'r') as f:
    for eachLine in f:
        print re.split(r'\s\s+|\t', eachLine.rstrip())
f.close()
</code>
```

```
Overwriting whodata.py

```

```
<code>%run whodata.py 
</code>
```

tasklist相当于linux里的who

```
<code>!tasklist
</code>
```

```
映像名称                       PID 会话名              会话#       内存使用 
========================= ======== ================ =========== ============
System Idle Process              0 Services                   0          8 K
System                           4 Services                   0        140 K
Registry                        96 Services                   0     46,220 K
smss.exe                       348 Services                   0        924 K
csrss.exe                      528 Services                   0      3,920 K
wininit.exe                    632 Services                   0      4,656 K
csrss.exe                      644 Console                    1      4,692 K
winlogon.exe                   736 Console                    1      7,132 K
services.exe                   856 Services                   0      7,540 K
lsass.exe                      868 Services                   0     14,756 K
svchost.exe                    984 Services                   0      3,236 K
fontdrvhost.exe                996 Console                    1     15,312 K
fontdrvhost.exe                992 Services                   0      2,564 K
svchost.exe                    464 Services                   0     26,972 K
WUDFHost.exe                   488 Services                   0      5,124 K
svchost.exe                    844 Services                   0     13,908 K
svchost.exe                    800 Services                   0      7,796 K
dwm.exe                       1108 Console                    1     54,276 K
svchost.exe                   1188 Services                   0      9,084 K
svchost.exe                   1244 Services                   0     13,952 K
svchost.exe                   1364 Services                   0      8,052 K
svchost.exe                   1444 Services                   0     10,832 K
svchost.exe                   1492 Services                   0     12,476 K
svchost.exe                   1500 Services                   0     13,180 K
svchost.exe                   1564 Services                   0      9,208 K
svchost.exe                   1640 Services                   0      5,972 K
svchost.exe                   1648 Services                   0      8,164 K
svchost.exe                   1724 Services                   0      7,712 K
nvvsvc.exe                    1756 Services                   0      7,916 K
svchost.exe                   1808 Services                   0      6,832 K
nvxdsync.exe                  1936 Console                    1     18,564 K
svchost.exe                   1964 Services                   0     10,720 K
svchost.exe                   1340 Services                   0      7,996 K
svchost.exe                   1612 Services                   0      8,768 K
suservice.exe                 2152 Services                   0      7,204 K
svchost.exe                   2188 Services                   0      6,672 K
svchost.exe                   2284 Services                   0      6,204 K
svchost.exe                   2292 Services                   0      6,048 K
svchost.exe                   2300 Services                   0     73,516 K
svchost.exe                   2316 Services                   0      4,888 K
svchost.exe                   2452 Services                   0      6,844 K
Memory Compression            2468 Services                   0    160,312 K
igfxCUIService.exe            2576 Services                   0      7,392 K
svchost.exe                   2648 Services                   0      6,096 K
svchost.exe                   2656 Services                   0      7,896 K
svchost.exe                   2680 Services                   0      6,988 K
svchost.exe                   2768 Services                   0      6,952 K
svchost.exe                   2776 Services                   0     13,684 K
winwfpmonitor.exe             2848 Services                   0      1,056 K
svchost.exe                   2880 Services                   0     10,888 K
RtkAudioService64.exe         2976 Services                   0      5,356 K
svchost.exe                   2984 Services                   0     14,408 K
svchost.exe                   2440 Services                   0     16,244 K
HaozipSvc.exe                 3076 Services                   0     13,784 K
svchost.exe                   3088 Services                   0      5,608 K
svchost.exe                   3104 Services                   0      9,408 K
RAVBg64.exe                   3444 Console                    1      8,172 K
RAVBg64.exe                   3464 Console                    1      7,988 K
svchost.exe                   3520 Services                   0     11,716 K
svchost.exe                   3616 Services                   0      9,416 K
svchost.exe                   3612 Services                   0      9,876 K
svchost.exe                   3664 Services                   0      5,572 K
svchost.exe                   3680 Services                   0      5,724 K
spoolsv.exe                   3832 Services                   0      8,436 K
CAJSHost.exe                  4016 Services                   0      4,828 K
svchost.exe                   4024 Services                   0      7,152 K
FlashHelperService.exe        4032 Services                   0      9,336 K
svchost.exe                   4040 Services                   0     24,172 K
svchost.exe                   4048 Services                   0     11,468 K
svchost.exe                   4068 Services                   0     24,496 K
OfficeClickToRun.exe          4080 Services                   0     22,356 K
QQProtect.exe                 4092 Services                   0     16,256 K
svchost.exe                   3304 Services                   0      5,224 K
svchost.exe                   2716 Services                   0      7,344 K
IpOverUsbSvc.exe              3396 Services                   0      7,328 K
sqlwriter.exe                 2932 Services                   0      5,556 K
svchost.exe                   2400 Services                   0      6,564 K
SynTPEnhService.exe           3944 Services                   0      3,612 K
SecurityHealthService.exe     4108 Services                   0     10,524 K
svchost.exe                   4164 Services                   0      4,768 K
MsMpEng.exe                   4240 Services                   0    156,676 K
svchost.exe                   4284 Services                   0     19,444 K
svchost.exe                   4444 Services                   0      5,400 K
svchost.exe                   4500 Services                   0      5,064 K
svchost.exe                   4628 Services                   0      5,480 K
svchost.exe                   4764 Services                   0      9,376 K
sihost.exe                    5948 Console                    1     19,596 K
svchost.exe                   6092 Console                    1     25,056 K
svchost.exe                   6100 Services                   0      5,180 K
SynTPEnh.exe                  6132 Console                    1     11,888 K
svchost.exe                   5592 Console                    1     25,740 K
explorer.exe                  5608 Console                    1    233,416 K
taskhostw.exe                 3172 Console                    1     16,976 K
svchost.exe                   6256 Services                   0     13,336 K
svchost.exe                   6708 Services                   0      5,964 K
svchost.exe                   6748 Services                   0      6,664 K
SearchIndexer.exe             6780 Services                   0     60,696 K
NisSrv.exe                    6788 Services                   0      9,220 K
svchost.exe                   6864 Services                   0     10,500 K
svchost.exe                   7012 Services                   0     10,748 K
SynTPHelper.exe               7104 Console                    1      3,472 K
svchost.exe                   5892 Services                   0      6,332 K
ctfmon.exe                    7048 Console                    1     49,308 K
ChsIME.exe                    5644 Console                    1     61,892 K
svchost.exe                   7116 Services                   0     14,660 K
RuntimeBroker.exe             7692 Console                    1     29,816 K
svchost.exe                   8188 Services                   0     17,808 K
PresentationFontCache.exe     7504 Services                   0     15,220 K
RAVBg64.exe                   7232 Console                    1        412 K
SettingSyncHost.exe           8276 Console                    1      3,648 K
igfxEM.exe                    8896 Console                    1     10,216 K
igfxHK.exe                    8920 Console                    1      7,376 K
Video.UI.exe                  8988 Console                    1     14,604 K
PicGo.exe                     6796 Console                    1     30,136 K
InputPersonalization.exe      1308 Console                    1     14,644 K
WindowsInternal.Composabl     3488 Console                    1     12,732 K
nvtray.exe                    4116 Console                    1     10,076 K
svchost.exe                   4656 Services                   0     13,196 K
dllhost.exe                    792 Console                    1      9,708 K
svchost.exe                   3048 Services                   0      6,844 K
NvBackend.exe                 3328 Console                    1      7,188 K
PicGo.exe                     1156 Console                    1      6,324 K
PicGo.exe                     8244 Console                    1      4,704 K
svchost.exe                   7084 Console                    1     22,936 K
GoogleCrashHandler.exe         788 Services                   0        172 K
RuntimeBroker.exe             9184 Console                    1      7,284 K
GoogleCrashHandler64.exe      3756 Services                   0        168 K
svchost.exe                  10064 Services                   0     16,176 K
svchost.exe                  10684 Services                   0      7,520 K
SgrmBroker.exe               10776 Services                   0      6,020 K
svchost.exe                   9684 Services                   0      8,256 K
svchost.exe                  10604 Services                   0     10,720 K
svchost.exe                  10396 Services                   0      6,992 K
explorer.exe                 10848 Console                    1    142,144 K
Microsoft.Photos.exe          5584 Console                    1     49,760 K
svchost.exe                  10836 Services                   0      8,348 K
RuntimeBroker.exe             2788 Console                    1     25,848 K
ApplicationFrameHost.exe      4496 Console                    1     25,076 K
WinStore.App.exe              9860 Console                    1     60,768 K
RuntimeBroker.exe             7160 Console                    1     12,256 K
Calculator.exe                2708 Console                    1     34,936 K
RuntimeBroker.exe             6884 Console                    1      5,744 K
SystemSettings.exe            5376 Console                    1     44,312 K
RuntimeBroker.exe            10620 Console                    1     11,640 K
svchost.exe                  12620 Services                   0      4,924 K
8021x.exe                    13008 Console                    1      3,228 K
SearchUI.exe                 11728 Console                    1     55,272 K
RuntimeBroker.exe            12796 Console                    1      7,052 K
taskhostw.exe                12672 Console                    1     12,572 K
WeChatStore.exe               3740 Console                    1     57,068 K
svchost.exe                  11684 Services                   0     13,028 K
svchost.exe                   1220 Services                   0      5,440 K
ShellExperienceHost.exe       6624 Console                    1     59,436 K
MicrosoftEdge.exe            15268 Console                    1     52,788 K
browser_broker.exe           14776 Console                    1     22,576 K
RuntimeBroker.exe            12564 Console                    1     10,632 K
MicrosoftEdgeCP.exe          14612 Console                    1     19,720 K
MicrosoftEdgeCP.exe           1460 Console                    1     21,660 K
RuntimeBroker.exe             3424 Console                    1     20,820 K
ClvAssist.exe                10988 Services                   0     11,344 K
Clover.exe                   21724 Console                    1     31,592 K
git-bash.exe                 18248 Console                    1      5,088 K
mintty.exe                   20748 Console                    1     26,736 K
conhost.exe                  20688 Console                    1     11,044 K
bash.exe                     20476 Console                    1      8,732 K
bash.exe                     21896 Console                    1      5,800 K
jupyter.exe                   5732 Console                    1      4,836 K
python.exe                   17704 Console                    1     10,552 K
jupyter-notebook.exe         21892 Console                    1      4,832 K
python.exe                   18980 Console                    1     52,948 K
chrome.exe                   17384 Console                    1    136,912 K
chrome.exe                   18088 Console                    1      8,448 K
chrome.exe                   22040 Console                    1      9,120 K
chrome.exe                   20764 Console                    1    128,852 K
chrome.exe                   20228 Console                    1     22,096 K
chrome.exe                    9104 Console                    1    302,556 K
chrome.exe                   19644 Console                    1     89,260 K
chrome.exe                    5852 Console                    1     39,672 K
chrome.exe                   12604 Console                    1     33,224 K
chrome.exe                   22100 Console                    1     33,048 K
chrome.exe                    1480 Console                    1     32,092 K
chrome.exe                   14536 Console                    1     47,936 K
svchost.exe                  12356 Services                   0     11,112 K
python.exe                   22440 Console                    1     31,472 K
SearchProtocolHost.exe       12252 Services                   0     10,796 K
SearchFilterHost.exe         20472 Services                   0      6,216 K
WmiPrvSE.exe                 20252 Services                   0      9,656 K
cmd.exe                      22188 Console                    1      3,588 K
tasklist.exe                 10920 Console                    1      8,004 K

```

```
<code>%%writefile retasklist.py
import re
import os
with os.popen('tasklist /nh', 'r') as f: # '/nh去掉进程池PID的表格头'
    for eachLine in f:
        print re.split(r'\s\s+|\t', eachLine.rstrip())
f.close()
</code>
```

```
Overwriting retasklist.py

```

```
<code>%run retasklist.py 
</code>
```

```
['']
['System Idle Process', '0 Services', '0', '8 K']
['System', '4 Services', '0', '140 K']
['Registry', '96 Services', '0', '46,004 K']
['smss.exe', '348 Services', '0', '924 K']
['csrss.exe', '528 Services', '0', '3,920 K']
['wininit.exe', '632 Services', '0', '4,656 K']
['csrss.exe', '644 Console', '1', '4,692 K']
['winlogon.exe', '736 Console', '1', '7,120 K']
['services.exe', '856 Services', '0', '7,544 K']
['lsass.exe', '868 Services', '0', '14,756 K']
['svchost.exe', '984 Services', '0', '3,236 K']
['fontdrvhost.exe', '996 Console', '1', '15,312 K']
['fontdrvhost.exe', '992 Services', '0', '2,564 K']
['svchost.exe', '464 Services', '0', '26,984 K']
['WUDFHost.exe', '488 Services', '0', '5,124 K']
['svchost.exe', '844 Services', '0', '13,956 K']
['svchost.exe', '800 Services', '0', '7,800 K']
['dwm.exe', '1108 Console', '1', '54,276 K']
['svchost.exe', '1188 Services', '0', '9,084 K']
['svchost.exe', '1244 Services', '0', '13,956 K']
['svchost.exe', '1364 Services', '0', '8,052 K']
['svchost.exe', '1444 Services', '0', '10,816 K']
['svchost.exe', '1492 Services', '0', '12,476 K']
['svchost.exe', '1500 Services', '0', '13,136 K']
['svchost.exe', '1564 Services', '0', '9,208 K']
['svchost.exe', '1640 Services', '0', '6,000 K']
['svchost.exe', '1648 Services', '0', '8,172 K']
['svchost.exe', '1724 Services', '0', '7,712 K']
['nvvsvc.exe', '1756 Services', '0', '7,916 K']
['svchost.exe', '1808 Services', '0', '6,832 K']
['nvxdsync.exe', '1936 Console', '1', '18,564 K']
['svchost.exe', '1964 Services', '0', '10,720 K']
['svchost.exe', '1340 Services', '0', '8,016 K']
['svchost.exe', '1612 Services', '0', '8,804 K']
['suservice.exe', '2152 Services', '0', '7,204 K']
['svchost.exe', '2188 Services', '0', '6,688 K']
['svchost.exe', '2284 Services', '0', '6,204 K']
['svchost.exe', '2292 Services', '0', '6,048 K']
['svchost.exe', '2300 Services', '0', '73,564 K']
['svchost.exe', '2316 Services', '0', '4,888 K']
['svchost.exe', '2452 Services', '0', '6,844 K']
['Memory Compression', '2468 Services', '0', '159,992 K']
['igfxCUIService.exe', '2576 Services', '0', '7,384 K']
['svchost.exe', '2648 Services', '0', '6,096 K']
['svchost.exe', '2656 Services', '0', '7,896 K']
['svchost.exe', '2680 Services', '0', '6,968 K']
['svchost.exe', '2768 Services', '0', '6,952 K']
['svchost.exe', '2776 Services', '0', '13,684 K']
['winwfpmonitor.exe', '2848 Services', '0', '1,056 K']
['svchost.exe', '2880 Services', '0', '10,888 K']
['RtkAudioService64.exe', '2976 Services', '0', '5,356 K']
['svchost.exe', '2984 Services', '0', '14,408 K']
['svchost.exe', '2440 Services', '0', '16,244 K']
['HaozipSvc.exe', '3076 Services', '0', '13,748 K']
['svchost.exe', '3088 Services', '0', '5,608 K']
['svchost.exe', '3104 Services', '0', '9,408 K']
['RAVBg64.exe', '3444 Console', '1', '8,172 K']
['RAVBg64.exe', '3464 Console', '1', '7,988 K']
['svchost.exe', '3520 Services', '0', '11,716 K']
['svchost.exe', '3616 Services', '0', '9,416 K']
['svchost.exe', '3612 Services', '0', '9,876 K']
['svchost.exe', '3664 Services', '0', '5,572 K']
['svchost.exe', '3680 Services', '0', '5,724 K']
['spoolsv.exe', '3832 Services', '0', '8,436 K']
['CAJSHost.exe', '4016 Services', '0', '4,828 K']
['svchost.exe', '4024 Services', '0', '7,148 K']
['FlashHelperService.exe', '4032 Services', '0', '9,336 K']
['svchost.exe', '4040 Services', '0', '24,200 K']
['svchost.exe', '4048 Services', '0', '12,260 K']
['svchost.exe', '4068 Services', '0', '24,496 K']
['OfficeClickToRun.exe', '4080 Services', '0', '22,356 K']
['QQProtect.exe', '4092 Services', '0', '16,256 K']
['svchost.exe', '3304 Services', '0', '5,224 K']
['svchost.exe', '2716 Services', '0', '7,344 K']
['IpOverUsbSvc.exe', '3396 Services', '0', '7,328 K']
['sqlwriter.exe', '2932 Services', '0', '5,556 K']
['svchost.exe', '2400 Services', '0', '6,564 K']
['SynTPEnhService.exe', '3944 Services', '0', '3,612 K']
['SecurityHealthService.exe', '4108 Services', '0', '10,524 K']
['svchost.exe', '4164 Services', '0', '4,764 K']
['MsMpEng.exe', '4240 Services', '0', '159,124 K']
['svchost.exe', '4284 Services', '0', '19,444 K']
['svchost.exe', '4444 Services', '0', '5,400 K']
['svchost.exe', '4500 Services', '0', '5,064 K']
['svchost.exe', '4628 Services', '0', '5,480 K']
['svchost.exe', '4764 Services', '0', '9,376 K']
['sihost.exe', '5948 Console', '1', '19,596 K']
['svchost.exe', '6092 Console', '1', '25,100 K']
['svchost.exe', '6100 Services', '0', '5,180 K']
['SynTPEnh.exe', '6132 Console', '1', '11,888 K']
['svchost.exe', '5592 Console', '1', '25,740 K']
['explorer.exe', '5608 Console', '1', '233,416 K']
['taskhostw.exe', '3172 Console', '1', '16,976 K']
['svchost.exe', '6256 Services', '0', '13,396 K']
['svchost.exe', '6708 Services', '0', '5,956 K']
['svchost.exe', '6748 Services', '0', '6,664 K']
['SearchIndexer.exe', '6780 Services', '0', '60,696 K']
['NisSrv.exe', '6788 Services', '0', '9,220 K']
['svchost.exe', '6864 Services', '0', '10,500 K']
['svchost.exe', '7012 Services', '0', '10,748 K']
['SynTPHelper.exe', '7104 Console', '1', '3,472 K']
['svchost.exe', '5892 Services', '0', '6,332 K']
['ctfmon.exe', '7048 Console', '1', '49,308 K']
['ChsIME.exe', '5644 Console', '1', '61,892 K']
['svchost.exe', '7116 Services', '0', '14,660 K']
['RuntimeBroker.exe', '7692 Console', '1', '29,816 K']
['svchost.exe', '8188 Services', '0', '17,808 K']
['PresentationFontCache.exe', '7504 Services', '0', '15,220 K']
['RAVBg64.exe', '7232 Console', '1', '412 K']
['SettingSyncHost.exe', '8276 Console', '1', '3,648 K']
['igfxEM.exe', '8896 Console', '1', '10,216 K']
['igfxHK.exe', '8920 Console', '1', '7,380 K']
['Video.UI.exe', '8988 Console', '1', '14,604 K']
['PicGo.exe', '6796 Console', '1', '30,136 K']
['InputPersonalization.exe', '1308 Console', '1', '14,644 K']
['WindowsInternal.Composabl', '3488 Console', '1', '12,732 K']
['nvtray.exe', '4116 Console', '1', '10,076 K']
['svchost.exe', '4656 Services', '0', '13,196 K']
['dllhost.exe', '792 Console', '1', '9,708 K']
['svchost.exe', '3048 Services', '0', '6,844 K']
['NvBackend.exe', '3328 Console', '1', '7,188 K']
['PicGo.exe', '1156 Console', '1', '6,324 K']
['PicGo.exe', '8244 Console', '1', '4,704 K']
['svchost.exe', '7084 Console', '1', '22,936 K']
['GoogleCrashHandler.exe', '788 Services', '0', '172 K']
['RuntimeBroker.exe', '9184 Console', '1', '7,284 K']
['GoogleCrashHandler64.exe', '3756 Services', '0', '168 K']
['svchost.exe', '10064 Services', '0', '16,176 K']
['svchost.exe', '10684 Services', '0', '7,520 K']
['SgrmBroker.exe', '10776 Services', '0', '6,020 K']
['svchost.exe', '9684 Services', '0', '8,256 K']
['svchost.exe', '10604 Services', '0', '10,720 K']
['svchost.exe', '10396 Services', '0', '6,992 K']
['explorer.exe', '10848 Console', '1', '142,144 K']
['Microsoft.Photos.exe', '5584 Console', '1', '49,760 K']
['svchost.exe', '10836 Services', '0', '8,348 K']
['RuntimeBroker.exe', '2788 Console', '1', '25,848 K']
['ApplicationFrameHost.exe', '4496 Console', '1', '25,076 K']
['WinStore.App.exe', '9860 Console', '1', '60,768 K']
['RuntimeBroker.exe', '7160 Console', '1', '12,256 K']
['Calculator.exe', '2708 Console', '1', '34,936 K']
['RuntimeBroker.exe', '6884 Console', '1', '5,744 K']
['SystemSettings.exe', '5376 Console', '1', '44,312 K']
['RuntimeBroker.exe', '10620 Console', '1', '11,640 K']
['svchost.exe', '12620 Services', '0', '4,924 K']
['8021x.exe', '13008 Console', '1', '3,920 K']
['SearchUI.exe', '11728 Console', '1', '55,272 K']
['RuntimeBroker.exe', '12796 Console', '1', '7,052 K']
['taskhostw.exe', '12672 Console', '1', '12,572 K']
['WeChatStore.exe', '3740 Console', '1', '57,068 K']
['svchost.exe', '11684 Services', '0', '13,028 K']
['svchost.exe', '1220 Services', '0', '5,400 K']
['ShellExperienceHost.exe', '6624 Console', '1', '59,376 K']
['MicrosoftEdge.exe', '15268 Console', '1', '52,788 K']
['browser_broker.exe', '14776 Console', '1', '22,576 K']
['RuntimeBroker.exe', '12564 Console', '1', '10,632 K']
['MicrosoftEdgeCP.exe', '14612 Console', '1', '19,720 K']
['MicrosoftEdgeCP.exe', '1460 Console', '1', '21,660 K']
['RuntimeBroker.exe', '3424 Console', '1', '20,820 K']
['ClvAssist.exe', '10988 Services', '0', '11,344 K']
['Clover.exe', '21724 Console', '1', '31,592 K']
['git-bash.exe', '18248 Console', '1', '5,088 K']
['mintty.exe', '20748 Console', '1', '26,736 K']
['conhost.exe', '20688 Console', '1', '11,044 K']
['bash.exe', '20476 Console', '1', '8,732 K']
['bash.exe', '21896 Console', '1', '5,800 K']
['jupyter.exe', '5732 Console', '1', '4,836 K']
['python.exe', '17704 Console', '1', '10,552 K']
['jupyter-notebook.exe', '21892 Console', '1', '4,832 K']
['python.exe', '18980 Console', '1', '52,952 K']
['chrome.exe', '17384 Console', '1', '136,880 K']
['chrome.exe', '18088 Console', '1', '8,448 K']
['chrome.exe', '22040 Console', '1', '9,120 K']
['chrome.exe', '20764 Console', '1', '125,724 K']
['chrome.exe', '20228 Console', '1', '22,096 K']
['chrome.exe', '9104 Console', '1', '303,500 K']
['chrome.exe', '19644 Console', '1', '89,260 K']
['chrome.exe', '5852 Console', '1', '39,672 K']
['chrome.exe', '12604 Console', '1', '33,224 K']
['chrome.exe', '22100 Console', '1', '33,048 K']
['chrome.exe', '1480 Console', '1', '32,092 K']
['chrome.exe', '14536 Console', '1', '47,936 K']
['svchost.exe', '12356 Services', '0', '11,112 K']
['python.exe', '22440 Console', '1', '31,564 K']
['SearchProtocolHost.exe', '12252 Services', '0', '10,732 K']
['SearchFilterHost.exe', '20472 Services', '0', '6,216 K']
['WmiPrvSE.exe', '20252 Services', '0', '9,832 K']
['cmd.exe', '20616 Console', '1', '3,544 K']
['tasklist.exe', '16932 Console', '1', '8,016 K']

```

此时PID和会话名称放在一起了，我们要将他分开，由于split的限制，所以要使用findall

```
<code>%%writefile retasklist.py
import re
import os

pat = r'([\w.]+(?: [\w.]+)*)\s\s+(\d+) \w+\s\s+\d+\s\s+([\d,]+ K)'
with os.popen('tasklist /nh', 'r') as f: # '/nh去掉进程池PID的表格头'
    for eachLine in f:
        print re.findall(pat, eachLine.rstrip())
f.close()
</code>
```

```
Overwriting retasklist.py

```

```
<code>%run retasklist.py
</code>
```

```
[]
[('System Idle Process', '0', '8 K')]
[('System', '4', '140 K')]
[('Registry', '96', '44,840 K')]
[('smss.exe', '348', '924 K')]
[('csrss.exe', '528', '3,920 K')]
[('wininit.exe', '632', '4,656 K')]
[('csrss.exe', '644', '4,692 K')]
[('winlogon.exe', '736', '7,116 K')]
[('services.exe', '856', '7,544 K')]
[('lsass.exe', '868', '14,756 K')]
[('svchost.exe', '984', '3,236 K')]
[('fontdrvhost.exe', '996', '15,312 K')]
[('fontdrvhost.exe', '992', '2,564 K')]
[('svchost.exe', '464', '26,984 K')]
[('WUDFHost.exe', '488', '5,124 K')]
[('svchost.exe', '844', '13,920 K')]
[('svchost.exe', '800', '7,804 K')]
[('dwm.exe', '1108', '51,672 K')]
[('svchost.exe', '1188', '9,084 K')]
[('svchost.exe', '1244', '14,080 K')]
[('svchost.exe', '1364', '8,052 K')]
[('svchost.exe', '1444', '10,816 K')]
[('svchost.exe', '1492', '12,476 K')]
[('svchost.exe', '1500', '13,136 K')]
[('svchost.exe', '1564', '9,208 K')]
[('svchost.exe', '1640', '6,000 K')]
[('svchost.exe', '1648', '8,172 K')]
[('svchost.exe', '1724', '7,712 K')]
[('nvvsvc.exe', '1756', '7,916 K')]
[('svchost.exe', '1808', '6,832 K')]
[('nvxdsync.exe', '1936', '18,564 K')]
[('svchost.exe', '1964', '10,720 K')]
[('svchost.exe', '1340', '8,000 K')]
[('svchost.exe', '1612', '8,764 K')]
[('suservice.exe', '2152', '7,204 K')]
[('svchost.exe', '2188', '6,688 K')]
[('svchost.exe', '2284', '6,204 K')]
[('svchost.exe', '2292', '6,048 K')]
[('svchost.exe', '2300', '73,572 K')]
[('svchost.exe', '2316', '4,888 K')]
[('svchost.exe', '2452', '6,844 K')]
[('Memory Compression', '2468', '159,452 K')]
[('igfxCUIService.exe', '2576', '7,384 K')]
[('svchost.exe', '2648', '6,096 K')]
[('svchost.exe', '2656', '7,896 K')]
[('svchost.exe', '2680', '6,968 K')]
[('svchost.exe', '2768', '6,952 K')]
[('svchost.exe', '2776', '13,700 K')]
[('winwfpmonitor.exe', '2848', '1,056 K')]
[('svchost.exe', '2880', '10,888 K')]
[('RtkAudioService64.exe', '2976', '5,356 K')]
[('svchost.exe', '2984', '14,408 K')]
[('svchost.exe', '2440', '16,244 K')]
[('HaozipSvc.exe', '3076', '13,748 K')]
[('svchost.exe', '3088', '5,608 K')]
[('svchost.exe', '3104', '9,408 K')]
[('RAVBg64.exe', '3444', '8,172 K')]
[('RAVBg64.exe', '3464', '7,988 K')]
[('svchost.exe', '3520', '11,716 K')]
[('svchost.exe', '3616', '9,416 K')]
[('svchost.exe', '3612', '9,876 K')]
[('svchost.exe', '3664', '5,572 K')]
[('svchost.exe', '3680', '5,724 K')]
[('spoolsv.exe', '3832', '8,436 K')]
[('CAJSHost.exe', '4016', '4,828 K')]
[('svchost.exe', '4024', '7,148 K')]
[('FlashHelperService.exe', '4032', '9,336 K')]
[('svchost.exe', '4040', '24,212 K')]
[('svchost.exe', '4048', '12,228 K')]
[('svchost.exe', '4068', '24,496 K')]
[('OfficeClickToRun.exe', '4080', '22,356 K')]
[('QQProtect.exe', '4092', '16,188 K')]
[('svchost.exe', '3304', '5,224 K')]
[('svchost.exe', '2716', '7,344 K')]
[('IpOverUsbSvc.exe', '3396', '7,328 K')]
[('sqlwriter.exe', '2932', '5,556 K')]
[('svchost.exe', '2400', '6,564 K')]
[('SynTPEnhService.exe', '3944', '3,608 K')]
[('SecurityHealthService.exe', '4108', '10,524 K')]
[('svchost.exe', '4164', '4,764 K')]
[('MsMpEng.exe', '4240', '159,172 K')]
[('svchost.exe', '4284', '19,424 K')]
[('svchost.exe', '4444', '5,400 K')]
[('svchost.exe', '4500', '5,064 K')]
[('svchost.exe', '4628', '5,480 K')]
[('svchost.exe', '4764', '9,376 K')]
[('sihost.exe', '5948', '19,596 K')]
[('svchost.exe', '6092', '25,084 K')]
[('svchost.exe', '6100', '5,180 K')]
[('SynTPEnh.exe', '6132', '11,888 K')]
[('svchost.exe', '5592', '25,740 K')]
[('explorer.exe', '5608', '233,444 K')]
[('taskhostw.exe', '3172', '16,976 K')]
[('svchost.exe', '6256', '13,396 K')]
[('svchost.exe', '6708', '5,956 K')]
[('svchost.exe', '6748', '6,664 K')]
[('SearchIndexer.exe', '6780', '60,696 K')]
[('NisSrv.exe', '6788', '9,220 K')]
[('svchost.exe', '6864', '10,500 K')]
[('svchost.exe', '7012', '10,748 K')]
[('SynTPHelper.exe', '7104', '3,472 K')]
[('svchost.exe', '5892', '6,332 K')]
[('ctfmon.exe', '7048', '49,308 K')]
[('ChsIME.exe', '5644', '61,892 K')]
[('svchost.exe', '7116', '14,660 K')]
[('RuntimeBroker.exe', '7692', '29,816 K')]
[('svchost.exe', '8188', '17,808 K')]
[('PresentationFontCache.exe', '7504', '15,220 K')]
[('RAVBg64.exe', '7232', '412 K')]
[('SettingSyncHost.exe', '8276', '3,648 K')]
[('igfxEM.exe', '8896', '10,216 K')]
[('igfxHK.exe', '8920', '7,380 K')]
[('Video.UI.exe', '8988', '14,604 K')]
[('PicGo.exe', '6796', '30,136 K')]
[('InputPersonalization.exe', '1308', '14,644 K')]
[('WindowsInternal.Composabl', '3488', '12,732 K')]
[('nvtray.exe', '4116', '10,076 K')]
[('svchost.exe', '4656', '13,196 K')]
[('dllhost.exe', '792', '9,708 K')]
[('svchost.exe', '3048', '6,844 K')]
[('NvBackend.exe', '3328', '7,188 K')]
[('PicGo.exe', '1156', '6,324 K')]
[('PicGo.exe', '8244', '4,704 K')]
[('svchost.exe', '7084', '22,936 K')]
[('GoogleCrashHandler.exe', '788', '172 K')]
[('RuntimeBroker.exe', '9184', '7,284 K')]
[('GoogleCrashHandler64.exe', '3756', '168 K')]
[('svchost.exe', '10064', '16,176 K')]
[('svchost.exe', '10684', '7,520 K')]
[('SgrmBroker.exe', '10776', '6,020 K')]
[('svchost.exe', '9684', '8,256 K')]
[('svchost.exe', '10604', '10,720 K')]
[('svchost.exe', '10396', '6,992 K')]
[('explorer.exe', '10848', '142,144 K')]
[('Microsoft.Photos.exe', '5584', '49,760 K')]
[('svchost.exe', '10836', '8,348 K')]
[('RuntimeBroker.exe', '2788', '25,848 K')]
[('ApplicationFrameHost.exe', '4496', '24,968 K')]
[('WinStore.App.exe', '9860', '60,768 K')]
[('RuntimeBroker.exe', '7160', '12,256 K')]
[('Calculator.exe', '2708', '34,936 K')]
[('RuntimeBroker.exe', '6884', '5,744 K')]
[('SystemSettings.exe', '5376', '44,312 K')]
[('RuntimeBroker.exe', '10620', '11,640 K')]
[('svchost.exe', '12620', '4,924 K')]
[('8021x.exe', '13008', '4,016 K')]
[('SearchUI.exe', '11728', '55,272 K')]
[('RuntimeBroker.exe', '12796', '7,052 K')]
[('taskhostw.exe', '12672', '12,572 K')]
[('WeChatStore.exe', '3740', '57,068 K')]
[('svchost.exe', '11684', '13,028 K')]
[('svchost.exe', '1220', '5,388 K')]
[('ShellExperienceHost.exe', '6624', '59,376 K')]
[('MicrosoftEdge.exe', '15268', '52,788 K')]
[('browser_broker.exe', '14776', '22,576 K')]
[('RuntimeBroker.exe', '12564', '10,632 K')]
[('MicrosoftEdgeCP.exe', '14612', '19,720 K')]
[('MicrosoftEdgeCP.exe', '1460', '21,660 K')]
[('RuntimeBroker.exe', '3424', '20,820 K')]
[('ClvAssist.exe', '10988', '11,344 K')]
[('Clover.exe', '21724', '31,592 K')]
[('bash.exe', '18248', '5,088 K')]
[('mintty.exe', '20748', '26,736 K')]
[('conhost.exe', '20688', '11,044 K')]
[('bash.exe', '20476', '8,732 K')]
[('bash.exe', '21896', '5,800 K')]
[('jupyter.exe', '5732', '4,836 K')]
[('python.exe', '17704', '10,552 K')]
[('notebook.exe', '21892', '4,832 K')]
[('python.exe', '18980', '52,952 K')]
[('chrome.exe', '17384', '136,880 K')]
[('chrome.exe', '18088', '8,448 K')]
[('chrome.exe', '22040', '9,120 K')]
[('chrome.exe', '20764', '125,712 K')]
[('chrome.exe', '20228', '22,096 K')]
[('chrome.exe', '9104', '310,240 K')]
[('chrome.exe', '19644', '89,260 K')]
[('chrome.exe', '5852', '39,672 K')]
[('chrome.exe', '12604', '33,224 K')]
[('chrome.exe', '22100', '33,048 K')]
[('chrome.exe', '1480', '32,092 K')]
[('chrome.exe', '14536', '47,936 K')]
[('svchost.exe', '12356', '11,112 K')]
[('python.exe', '22440', '31,564 K')]
[('SearchProtocolHost.exe', '12252', '10,636 K')]
[('SearchFilterHost.exe', '20472', '6,216 K')]
[('WmiPrvSE.exe', '20252', '9,876 K')]
[('cmd.exe', '18660', '3,564 K')]
[('tasklist.exe', '11796', '8,020 K')]

```

#### 实战示例

```
<code>%%writefile gendata.py
# coding=utf-8
# 创建随机数据，然后将生成的数据输出到屏幕
from random import randrange, choice
from string import ascii_lowercase as lc
from sys import maxint
from time import ctime

tlds = ( 'com', 'edu', 'net', 'org', 'gov' )

for i in xrange(randrange(5, 11)):
    dtint = randrange(maxint)	# pick date
    dtstr = ctime(dtint)	# date string
    llen = randrange(4, 7)	# login is shorter
    login = ''.join(choice(lc) for j in range(llen))
    dlen = randrange(llen, 13)	# domain is longer
    dom = ''.join(choice(lc) for j in xrange(dlen))
    print '%s::%s@%s.%s::%d-%d-%d' % (dtstr, login,
	dom, choice(tlds), dtint, llen, dlen)
</code>
```

```
Overwriting gendata.py

```

```
<code>%run gendata.py
</code>
```

```
Thu Dec 27 01:10:08 2035::dqtypg@iavqvgjwnvn.edu::2082301808-6-11
Fri May 13 20:51:55 2033::osxul@elfzkq.gov::1999601515-5-6
Mon Apr 06 22:52:20 2020::rehbg@yfdoy.edu::1586184740-5-5
Wed Dec 31 23:22:03 2008::legdw@tonqsajuiuch.edu::1230736923-5-12
Sat Sep 05 12:49:23 2015::tkyyb@oygzos.edu::1441428563-5-6
Mon May 27 08:00:35 2013::ztkuz@usczxpegy.gov::1369612835-5-9
Mon Jul 06 14:17:37 2015::urpy@eblts.org::1436163457-4-5

```

```
<code>import re
data = 'Thu Feb 15 17:46:04 2007::uzifzf@dpyivihw.gov::1171590364-6-8'
patt = '^(Mon|Tue|Wed|Thu|Fri|Sat|Sun)'
m = re.match(patt, data)
m.group()
</code>
```

```
'Thu'

```

```
<code>m.group(1)
</code>
```

```
'Thu'

```

```
<code>m.groups()
</code>
```

```
('Thu',)

```

```
<code>patt = '^(\w{3})'
m = re.match(patt, data)
if m is not None: print m.group()
</code>
```

```
Thu

```

```
<code>m.group(1)
</code>
```

```
'Thu'

```

```
<code>patt = '^(\w){3}'  # 注意区别
m = re.match(patt, data)
if m is not None: print m.group()
</code>
```

```
Thu

```

```
<code>m.group(1)
</code>
```

```
'u'

```

### 搜索、匹配和贪婪

```
<code>patt = '\d+-\d+-\d+'
re.search(patt, data).group() 
</code>
```

```
'1171590364-6-8'

```

```
<code>patt = '.+(\d+-\d+-\d+)'
re.search(patt, data).group(1)
</code>
```

```
'4-6-8'

```

这就是所谓的贪婪，`.`把前面的数字也给匹配了

```
<code>patt = '.+?(\d+-\d+-\d+)'  # ？是非贪婪操作符
re.search(patt, data).group(1)
</code>
```

```
'1171590364-6-8'

```

```
<code># 只要中间那个数字
patt = '-(\d+)-'
m = re.search(patt, data)
m.group()
</code>
```

```
'-6-'

```

```
<code>m.group(1)
</code>
```

```
'6'

```

> 
参考文献： 《Python核心编程第三版》 人民邮电出版社

