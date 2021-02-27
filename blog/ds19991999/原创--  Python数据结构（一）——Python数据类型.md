# 原创
：  Python数据结构（一）——Python数据类型

# Python数据结构（一）——Python数据类型

# 回顾Python数据类型

本系列需要用到的源码：[Python数据结构类封装](https://download.csdn.net/download/ds19991999/10571330)

> 
Python支持面向对象的编程模式，这意味这Python在解决问题的过程中重点是数据.


## 基本类型

```
False or True
```

```
True

```

```
not (False or True)
```

```
False

```

```
myList = [1,2,3,4]
A = [myList]*3
print(A)
myList[2]=45
print(A)
```

```
[[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
[[1, 2, 45, 4], [1, 2, 45, 4], [1, 2, 45, 4]]

```

```
# 与sort方法合用有效果
myList.sort()
myList
```

```
[1, 2, 4, 45]

```

```
myList.reverse()
print myList
```

```
[45, 4, 2, 1]

```

```
myName = 'dsdshahahads'
myName.split('s')
```

```
['d', 'd', 'hahahad', '']

```

```
{3,6,"cat",4.5,False,6,6,6,6,6,6,6}
```

```
{False, 3, 4.5, 6, 'cat'}

```

## 输入与输出

```
aName = input("Please enter your name ")
print("Your name in all capitals is",aName.upper(),
      "and has length", len(aName))
```

```
Please enter your name  'ds'


Your name in all capitals is 'DS' and has length 4

```

```
# Python3支持，Python2不支持
print("Hello","World", sep = "***")
print("Hello","World", end = "***")
```

```
Hello***World
Hello World***

```

## 控制结构

## 异常

```
import math
try:
    anumber = int(input("Please enter an integer "))
    print(math.sqrt(anumber))
except:
    print("Bad Value for square root")
    print("Using absolute value instead")
    print(math.sqrt(abs(anumber)))
```

```
Please enter an integer  -3


Bad Value for square root
Using absolute value instead
1.73205080757

```

```
import math
try:
    anumber = int(input("Please enter an integer "))
    print(math.sqrt(anumber))
except Exception as msg:
    print msg
```

```
Please enter an integer  -33


math domain error

```

## 定义函数

```
def f(x):
    x *= x
    if not x &lt; 100:
        return x
    else:
        return f(x)
```

```
f(5)
```

```
625

```

```
f(f(3))
```

```
43046721

```

## 类

```
def gcd(m,n):
    """取余的公约数求法"""
    while m%n != 0:
        m,n = n,m%n
    return n

class Fraction:
     def __init__(self,top,bottom):
         self.num = top
         self.den = bottom

     def __str__(self):
         return str(self.num)+"/"+str(self.den)

     def show(self):
         print(self.num,"/",self.den)

     def __add__(self,otherfraction):
         newnum = self.num*otherfraction.den + \
                      self.den*otherfraction.num
         newden = self.den * otherfraction.den
         common = gcd(newnum,newden)
         return Fraction(newnum//common,newden//common)

     def __eq__(self, other):
        """
        覆盖__eq__方法，通过相同的值创建深相等,而不是相同的引用
        即"=="，返回bool值
        """
         firstnum = self.num * other.den
         secondnum = other.num * self.den

         return firstnum == secondnum

x = Fraction(1,2)
y = Fraction(2,3)
print(x+y)
print(x == y)
```

```
7/6
False

```

## 面向对象编程详见专题笔记

## 总结
