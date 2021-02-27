# 原创
：  Numpy学习（一）——Numpy 简介

# Numpy学习（一）——Numpy 简介

# Numpy 简介

## 导入numpy

Numpy是Python的一个很重要的第三方库，很多其他科学计算的第三方库都是以Numpy为基础建立的。

Numpy的一个重要特性是它的**数组计算**。

```
from numpy import *
```

以下几种导入方式都行

```
import numpy
import numpy as np
from numpy import *
from numpy import array, sin
```

ipython中可以使用magic命令来快速导入Numpy的内容。

```
%pylab
```

```
Using matplotlib backend: TkAgg
Populating the interactive namespace from numpy and matplotlib

```

## 数组上的数学操作

```
a = [1, 2, 3, 4]
a + 1 # 直接运行报错
```

```
TypeErrorTraceback (most recent call last)

&lt;ipython-input-3-eb27785ac8c2&gt; in &lt;module&gt;()
      1 a = [1, 2, 3, 4]
----&gt; 2 a + 1 # 直接运行报错


TypeError: can only concatenate list (not "int") to list

```

```
# 使用array数组
a = array(a)
a
```

```
array([1, 2, 3, 4])

```

```
a + 1
```

```
array([2, 3, 4, 5])

```

```
b = array([2, 3, 4, 5])
a+b
```

```
array([3, 5, 7, 9])

```

```
a*b
```

```
array([ 2,  6, 12, 20])

```

```
a**b
```

```
array([   1,    8,   81, 1024])

```

## 提取数组中的元素

```
a[0]
```

```
1

```

```
a[:2]
```

```
array([1, 2])

```

```
a[-2:]
```

```
array([3, 4])

```

```
a[:2]+a[-2:]
```

```
array([4, 6])

```

## 修改数组形状

```
# 查看array的形状
a.shape
```

```
(4,)

```

```
# 修改array的形状
a.shape = 2,2
a
```

```
array([[1, 2],
       [3, 4]])

```

## 多维数组

```
a
```

```
array([[1, 2],
       [3, 4]])

```

```
a+a
```

```
array([[2, 4],
       [6, 8]])

```

```
a*a
```

```
array([[ 1,  4],
       [ 9, 16]])

```

## 画图

**linspace** 用来生成一组等间隔的数据：

```
# precision该方法用来定义小数点后的位数
a = linspace(0, 2*pi, 21)
%precision 3 
a
```

```
array([0.   , 0.314, 0.628, 0.942, 1.257, 1.571, 1.885, 2.199, 2.513,
       2.827, 3.142, 3.456, 3.77 , 4.084, 4.398, 4.712, 5.027, 5.341,
       5.655, 5.969, 6.283])

```

```
# 三角函数
b = sin(a)
b
```

```
array([ 0.000e+00,  3.090e-01,  5.878e-01,  8.090e-01,  9.511e-01,
        1.000e+00,  9.511e-01,  8.090e-01,  5.878e-01,  3.090e-01,
        1.225e-16, -3.090e-01, -5.878e-01, -8.090e-01, -9.511e-01,
       -1.000e+00, -9.511e-01, -8.090e-01, -5.878e-01, -3.090e-01,
       -2.449e-16])

```

```
# 画出三角函数图像
%matplotlib inline
plot(a, b)
```

```
[&lt;matplotlib.lines.Line2D at 0xab0fe10&gt;]

```

## 从数组中选择元素

```
b
```

```
array([ 0.000e+00,  3.090e-01,  5.878e-01,  8.090e-01,  9.511e-01,
        1.000e+00,  9.511e-01,  8.090e-01,  5.878e-01,  3.090e-01,
        1.225e-16, -3.090e-01, -5.878e-01, -8.090e-01, -9.511e-01,
       -1.000e+00, -9.511e-01, -8.090e-01, -5.878e-01, -3.090e-01,
       -2.449e-16])

```

```
# 假设我们想选取数组b中所有非负的部分，首先可以利用 b 产生一组布尔值
b &gt;= 0
```

```
array([ True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True, False, False, False, False, False, False, False,
       False, False, False])

```

```
mask = b &gt;= 0
```

```
# 画出所有对应的非负值对应的点：
plot(a[mask], b[mask], 'ro')
```

```
[&lt;matplotlib.lines.Line2D at 0xafd0e50&gt;]

```

```
plot(a[mask], b[mask], 'r')
```

```
[&lt;matplotlib.lines.Line2D at 0xa833ad0&gt;]

```
