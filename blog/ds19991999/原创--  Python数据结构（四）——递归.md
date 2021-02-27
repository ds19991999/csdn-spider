# 原创
：  Python数据结构（四）——递归

# Python数据结构（四）——递归

# 递归

递归是一种解决问题的方法，将问题分解为更小的子问题，直到得到一个足够小的问题可以被很简单的解决。通常递归涉及函数调用自身。递归允许我们编写优雅的解决方案，解决可能很难编程的问题。 

## 计算整数列表和

```
# version1
def list_sum(num_list):
    num_sum = 0
    for i in num_list:
        num_sum += i
    return num_sum
print list_sum([1,3,5,7,9])
```

```
25

```

```
# version2:不使用循环
def list_num2(num_list):
    if len(num_list)==1:
        return num_list[0]
    else:
        return num_list[0]+list_num2(num_list[1:])
print list_num2([1,3,5,7,9])


```

```
25

```

## 递归三定律

## 整数转任意进制字符

```
def to_str(n,base):
    conver_string = "0123456789ABCDEF"
    if n &lt; base:
        return conver_string[n]
    else:
        return str(to_str(n//base,base))+conver_string[n%base]
print to_str(1453,16)
```

```
5AD

```

## 栈帧：实现递归

```
from pythonds.basic.stack import Stack
rStack = Stack()

def to_str(n,base):
    conver_string = "0123456789ABCDEF"
    while n&gt;0:
        if n&lt;base:
            rStack.push(conver_string[n])
        else:
            rStack.push(conver_string[n%base])
        n //= base
    res = ""
    while not rStack.isEmpty():
        res += str(rStack.pop())
    return res

print to_str(1453,16)
```

```
5AD

```

## 可视化递归

```
# turtle 是 Python 所有版本的标准库，插图的工具
import turtle
```

```
myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle,linelen):
    if linelen &gt; 0:
        # 直走
        myTurtle.forward(linelen)
        # 右拐
        myTurtle.right(90)
        # 递归
        drawSpiral(myTurtle,linelen)
drawSpiral(myTurtle,100)
# 调用函数 myWin.exitonclick()，这是一个方便的缩小窗口的方法，
# 使乌龟进入等待模式，直到你单击窗口，然后程序清理并退出。
myWin.exitonclick()
```

```
# 绘制分型树
import turtle
def tree(branchlen,t):
    if branchlen &gt; 5:
        t.forward(branchlen)
        t.right(20)
        tree(branchlen-15,t)
        t.left(40)
        tree(branchlen-10,t)
        t.right(20)
        t.backward(branchlen)
def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()
main()
```

## 谢尔宾斯基三角形

```
import turtle

def drawTriangle(points,color,myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.end_fill()

def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points,degree,myTurtle):
    colormap = ['blue','red','green','white','yellow',
                'violet','orange']
    drawTriangle(points,colormap[degree],myTurtle)
    if degree &gt; 0:
        sierpinski([points[0],
                        getMid(points[0], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[1],
                        getMid(points[0], points[1]),
                        getMid(points[1], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[2],
                        getMid(points[2], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)

def main():
   myTurtle = turtle.Turtle()
   myWin = turtle.Screen()
   myPoints = [[-100,-50],[0,100],[100,-50]]
   sierpinski(myPoints,3,myTurtle)
   myWin.exitonclick()

main()
```

## 汉诺塔游戏

有一个印度教寺庙，将谜题交给年轻的牧师。在开始的时候，牧师们被给予三根杆和一堆 64 个金碟，每个盘比它下面一个小一点。他们的任务是将所有 64 个盘子从三个杆中一个转移到另一个。有两个重要的约束，它们一次只能移动一个盘子，并且它们不能在较小的盘子顶部上放置更大的盘子。牧师日夜不停每秒钟移动一块盘子。当他们完成工作时，传说，寺庙会变成灰尘，世界将消失。

虽然传说是有趣的，你不必担心世界不久的将来会消失。移动 64 个盘子的塔所需的步骤数是 2^64 -1 = 18,446,744,073,709,551,615264-1 = 18,446,744,073,709,551,615。以每秒一次的速度，即584,942,417,355584,942,417,355 年！。

这里是如何使用中间杆将塔从起始杆移动到目标杆的步骤：

```
# 一开始盘子都在起始杆上
# Python 提供了我们需要调用的隐含的栈。
def moveTower(height,fromPole, toPole, withPole):
    if height &gt;= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)
def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)
moveTower(4,'fromPole', 'toPole', 'withPole')
```

```
('moving disk from', 'fromPole', 'to', 'withPole')
('moving disk from', 'fromPole', 'to', 'toPole')
('moving disk from', 'withPole', 'to', 'toPole')
('moving disk from', 'fromPole', 'to', 'withPole')
('moving disk from', 'toPole', 'to', 'fromPole')
('moving disk from', 'toPole', 'to', 'withPole')
('moving disk from', 'fromPole', 'to', 'withPole')
('moving disk from', 'fromPole', 'to', 'toPole')
('moving disk from', 'withPole', 'to', 'toPole')
('moving disk from', 'withPole', 'to', 'fromPole')
('moving disk from', 'toPole', 'to', 'fromPole')
('moving disk from', 'withPole', 'to', 'toPole')
('moving disk from', 'fromPole', 'to', 'withPole')
('moving disk from', 'fromPole', 'to', 'toPole')
('moving disk from', 'withPole', 'to', 'toPole')

```

## 动态规划

假设你是一个自动售货机制造商的程序员。你的公司希望通过给每个交易最少硬币来简化工作。假设客户放入 1 美元的钞票并购买 37 美分的商品。你可以用来找零的最小数量的硬币是多少？

假设你的公司决定在埃尔博尼亚部署自动贩卖机，除了通常的 1，5，10 和 25 分硬币，他们还有一个 21 分硬币 。

```
def recMC(coinValueList,change):
    minCoins = change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c &lt;= change]:
            numCoins = 1 + recMC(coinValueList,change-i)
            if numCoins &lt; minCoins:
                minCoins = numCoins
    return minCoins
print recMC([1,5,10,25],63)
```

```
6

```

这种算法是非常低效的。事实上，它需要 67,716,925 个递归调用来找到 4 个硬币的最佳解决 63 美分问题的方案。

减少我们工作量的关键是记住一些过去的结果，这样我们可以避免重新计算我们已经知道的结果。一个简单的解决方案是将最小数量的硬币的结果存储在表中。

```
def recMC(coinValueList,change,knownResults):
    minCoins = change
    if change in coinValueList:
        knownResults[change] = 1
        return 1
    elif knownResults[change] &gt; 0:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c &lt;= change]:
            numCoins = 1 + recMC(coinValueList,change-i,knownResults)
            if numCoins &lt; minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins
    return minCoins
print recMC([1,5,10,25],63,[0]*64)
```

```
6

```

这个修改的算法减少了我们需要为四个硬币递归调用的数量，63美分问题只需 221 次调用！

使用动态规划算法:

```
def dpMakeChange(coinValueList,change,minCoins):
    for cents in range(change+1):
        coinCount = cents
        for j in [c for c in coinValueList if c&lt;= cents]:
            if minCoins[cents-j]+1&lt;coinCount:
                coinCounts = minCoins[cents-j]+1
        minCoins[cents] = coinCount
    return minCoins[change]
```

```
# 跟踪使用的硬币
def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
    for cents in range(change+1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c &lt;= cents]:
            if minCoins[cents-j] + 1 &lt; coinCount:
                coinCount = minCoins[cents-j]+1
                newCoin = j
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
    return minCoins[change]

def printCoins(coinsUsed,change):
    coin = change
    while coin &gt; 0:
        thisCoin = coinsUsed[coin]
        print thisCoin
        coin = coin - thisCoin

def main():
    amnt = 63
    clist = [1,5,10,21,25]
    coinsUsed = [0]*(amnt+1)
    coinCount = [0]*(amnt+1)

    print("Making change for",amnt,"requires")
    print(dpMakeChange(clist,amnt,coinCount,coinsUsed),"coins")
    print("They are:")
    printCoins(coinsUsed,amnt)
    print("The used list is as follows:")
    print(coinsUsed)
```

```
main()
```

```
('Making change for', 63, 'requires')
(3, 'coins')
They are:
21
21
21
The used list is as follows:
[1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 10, 1, 1, 1, 1, 5, 1, 1, 1, 1, 10, 21, 1, 1, 1, 25, 1, 1, 1, 1, 5, 10, 1, 1, 1, 10, 1, 1, 1, 1, 5, 10, 21, 1, 1, 10, 21, 1, 1, 1, 25, 1, 10, 1, 1, 5, 10, 1, 1, 1, 10, 1, 10, 21]

```
