# 原创
：  Byte of Python3 总结

# Byte of Python3 总结

> 
总结入门书《Byte of Python》，找找新东西。


### 目录

## 格式化字符串

字符串不可变，正则表达式中的字符串应该使用原始字符串`r"strings"`

format方法：

```
&gt;&gt;&gt; age = 20
&gt;&gt;&gt; name = "ds19991999"
&gt;&gt;&gt; print('{} was {} years old'.format(name,age))
ds19991999 was 20 years old
&gt;&gt;&gt; print('{0} was {1} years old'.format(name,age))
ds19991999 was 20 years old
&gt;&gt;&gt; print("{0:.3f}".format(4.0/3))
1.333
&gt;&gt;&gt; print('{0:_^11}'.format('hello'))
___hello___
&gt;&gt;&gt; print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))
Swaroop wrote A Byte of Python

```

指定结尾符号

```
print('a', end='')
print('b', end=' ')
print('c', end='\n')

```

## 运算符与表达式

运算符与C/C++差异比较大

```
/ 除，结果是浮点数
// 整除，整数整除结果为int，否则为float,执行floor除法
% 取模，返回除法运算后的余数
&lt;&lt; 左移，2&lt;&lt;2------&gt;10--1000得8
&amp; 按位与，5&amp;3------&gt;101&amp;011得001，结果为1
| 按位或，5|3------&gt;101|011得111，结果为7
^ 按位异或，5^3-----&gt;101^011得110，结果为6（相同为0，不同为1）
~ 按位取反 x~ ------&gt;得-(x+1)
not and or

```

`continue`跳出当前循环块剩余语句，继续下一次迭代

## 参数

[https://www.douban.com/note/13413855/](https://www.douban.com/note/13413855/)

`gloabal`语句：定义全局变量，`gloabal x`

```
  1. `F(arg1,arg2,...)` 传统参数
  2. `F(arg2=&lt;value&gt;,arg3=&lt;value&gt;...)` 默认参数
  3. `F(*arg1)` 可变参数，函数实际参数个数是不一定的，存放在以形参名为标识符的tuple中
  4. `F(**arg1) ` 可变参数，在函数内部将被存放在以形式名为标识符的dictionary中。这时候调用函数**必须采用key1=value1、key2=value2...**的形式。

```

```
def addOn(**arg):
	sum = 0
    if len(arg) == 0: return 0
    else:
       for x in arg.itervalues():
          sum += x
    return sum
addOn(x=4,y=5,k=6)

```

注意：在定义或调用这种函数时，顺序不能变

```
def function(arg1,arg2=&lt;value&gt;,*arg3,**arg4)

```

首先按顺序把“arg”这种形式的实参给对应的形参<br/> 第二，把“arg=”这种形式的实参赋值给形参<br/> 第三，把多出来的“arg”这种形式的实参组成一个tuple给带一个星号的形参<br/> 第四，把多出来的“key=value”这种形式的实参转为一个dictionary给带两个星号的形参

## 模块

```
if __name__=="__main__":
	main()
else:
    print("Import from another module")

```

## 包

包的结构：

```
- world/
    - __init__.py
    - asia/
        - __init__.py
        - india/
            - __init__.py
            - foo.py
    - africa/
        - __init__.py
        - madagascar/
            - __init__.py
            - bar.py

```

如上，包的名称为world，asia和afica是它的子包，子包包含india、madagascar等模块

## 数据结构

列表的引用：`a=[1,2,3,4]; b=a`，a和b指向同一个对象，改变a或b，都会改变，b=a[:]，则相当于copy一个对象，a与b不会互相改变

```
for keys,vals in adic.items():
	print(keys,vals)

```

> 
更详细的总结见后续博客更新


一些方法：

```
time.strftime("Y%m%d%H%M%S%")  返回当前日期与时间
os.system(command_string) 执行系统命令行，执行成功返回0
if not os.path.exists(target_dir): 判断目标路径存不存在
    os.mkdir(target_dir)
seq.replace(" ","_")，序列（字符串）将空格取代为_

```

## 软件开发流程

what——&gt;how——&gt;do it——&gt;test——&gt;use——&gt;maintain

## 面向对象编程

`__init__`方法、类变量和对象变量、装饰器classmethod、继承

## 输入与输出

**Pickle:**将纯Python对象存储在一个文件中，并在稍后取回，这叫持久性(Persistently)存储对象.

```
pickle.dump(list,file) # 存储到文件
pickle.load(file)#加载文件

```

## 异常

```
# coding=UTF-8
class ShortInputException(Exception):
    '''一个由用户定义的异常类'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast
try:
    text = input('Enter something --&gt;')
    if len(text) &lt; 3:
        raise ShortInputException(len(text),3)
     # 其他工作能在此处继续正常运行
    else:
    	print('No exception was raised.)
except EOFError:
    print('Why did you do an EOF on me?')
except ShortInputException as ex:
    print(('ShortInputException: The input was' + 
           {0} long, expected at least {1}')
           .format(ex.length, ex.atleast))


```

`try except finally`

```
with open("poem.txt") as f:
	for line in f:
		print(line,end='') 

```

## 特殊方法

```
listone = [2, 3, 4]
listtwo = [2*i for i in listone if i &gt; 2]
print(listtwo)

```
