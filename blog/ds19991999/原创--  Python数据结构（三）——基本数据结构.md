# 原创
：  Python数据结构（三）——基本数据结构

# Python数据结构（三）——基本数据结构

# 基本数据结构

# Contents

## 栈

### 简介

### Python实现栈

```
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        self.items.pop()
    def peek(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
```

```
# 创建一个空栈
s = Stack()
print s.isEmpty()
```

```
True

```

```
s.push(4)
s.push('dog')
s.items
```

```
[4, 'dog']

```

### 简单括号匹配

给出一个表达式(5+6)∗(7+8)/(4+3)，如何判断它的括号是否匹配,给出一个空栈，如果是’(‘就入栈,如果是’(‘就出栈，最后的栈如果是空栈则括号匹配，否则不匹配

```
from pythonds.basic.stack import Stack

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index &lt; len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        elif symbol == ")":
            # 空栈不能弹栈
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    # 两个条件，前面的"("匹配成功并且s为空栈
    if balanced and s.isEmpty():
        return True
    else:
        return False

print(parChecker('(2((3)2))'))
print(parChecker('(2(3)'))
print(parChecker('((((2(3)'))
```

```
True
False
False

```

### 符号匹配

在 Python 中，方括号 [ 和 ] 用于列表，花括号 { 和 } 用于字典。括号 ( 和 ) 用于元祖和算术表达式。只要每个符号都能保持自己的开始和结束关系，就可以混合符号

```
from pythonds.basic.stack import Stack
def parChecker(string):
    s = Stack()
    balanced = True
    index = 0

    while index&lt;len(string) and balanced:
        symbol = string[index]
        if symbol in "([{":
            s.push(symbol)
        elif symbol in ")}]":
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                    balanced = False

        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False                         

def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)

print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))

```

```
True
False

```

### 十进制转换成二进制

```
from pythonds.basic.stack import Stack
def divideBy2(number):
    remstack = Stack()

    while number&gt;0:
        rem = number%2
        # 入栈
        remstack.push(rem)
        number //= 2
    binString = ''
    while not remstack.isEmpty():
        # 出栈
        binString += str(remstack.pop())
    return binString
print divideBy2(7)
print divideBy2(43)
print divideBy2(6)
```

```
111
101011
110

```

更进一步，将基数2变为任意基数2-16

```
def baseConverter(number,base):
    digits = "0123456789ABCDEF"
    remstack = Stack()

    while number &gt; 0:
        rem = number%base
        remstack.push(rem)
        number //= base

    newString = ''
    while not remstack.isEmpty():
        newString += digits[remstack.pop()]
    return newString
print(baseConverter(30,2))
print(baseConverter(30,16))
```

```
11110
1E

```

### 中缀前缀和后缀表达式

我们生活中一般接触到的都是中缀运算符，所以不作介绍，而前缀和后缀运算符与中缀运算符的转换见下表： <br/> <img alt="" src="https://raw.githubusercontent.com/ds19991999/githubimg/master/picgo/20180729163838.png" title=""/> <br/> <img alt="" src="https://raw.githubusercontent.com/ds19991999/githubimg/master/picgo/20180729164150.png" title=""/>

#### 中缀转后缀算法

假设中缀表达式是一个由空格分隔的标记字符串。 操作符标记是`*，/，+和 -` ，以及左右括号。操作数是单字符 A，B，C 等。 以下步骤将后缀顺序生成一个字符串: <br/> * 创建一个名为 `opstack` 的空栈以保存运算符。给输出创建一个空列表。 <br/> * 通过使用字符串方法拆分将输入的中缀字符串转换为标记列表。 <br/> * 从左到右扫描标记列表。 <br/> * 如果标记是操作数，将其附加到输出列表的末尾。 <br/> * 如果标记是左括号，将其压到 opstack 上。 <br/> * 如果标记是右括号，则弹出 opstack，直到删除相应的左括号。将每个运算符附加到输出列表的末尾。 <br/> * 如果标记是运算符，`*，/，+或 -`，将其压入 `opstack`。但是，首先删除已经在 opstack 中具有更高或相等优先级的任何运算符，并将它们加到输出列表中。 <br/> * 当输入表达式被完全处理时，检查 opstack。仍然在栈上的任何运算符都可以删除并加到输出列表的末尾。 <br/> <img alt="" src="https://raw.githubusercontent.com/ds19991999/githubimg/master/picgo/20180729170448.png" title=""/>

```
from pythonds.basic.stack import Stack
def infixToPostfix(infixexpr):
    # 优先级字典
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    # 空格分隔的表达式
    tokenList = infixexpr.split()

    for token in tokenList:
        # 操作数
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        # 括号
        elif token == "(":
            opStack.push(token)
        elif token == ")":
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        # 操作符
        else:
            # 栈顶优先级大于当前操作符，并且栈不为空，弹栈加入输出列表
            # 并且将当前操作符入栈
            while (not opStack.isEmpty()) and (prec[opStack.peek()] &gt;= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)
    # 操作符栈不为空，全部弹出并加入输出链表    
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    # 以空格为界加上去
    return " ".join(postfixList)

print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
```

```
A B * C D * +
A B + C * D E - F G + * -

```

#### 后缀表达式求值

例如计算：`4 5 6 * +` <br/> <img alt="" src="https://raw.githubusercontent.com/ds19991999/githubimg/master/picgo/20180729184244.png" title=""/>

思路： <br/> 假设后缀表达式是一个由空格分隔的标记字符串。 运算符为`*，/，+和 -`，操作数假定为单个整数值。 输出将是一个整数结果。

```
from pythonds.basic.stack import Stack
def postfixEval(postfixExpr):
    openrandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            openrandStack.push(int(token))
        else:
            operand2 = openrandStack.pop()
            operand1 = openrandStack.pop()
            result = doMath(token,operand1,operand2)
            openrandStack.push(result)
    return openrandStack.pop()    

def doMath(op,op1,op2):
    if op == "*":
        return op1*op2
    elif op == "/":
        if op2 == 0:
            return False
        else:
            return op1/op2
    elif op == "+":
        return op1+op2
    elif op == "-":
        return op1-op2
```

```
print postfixEval('7 8 + 3 2 + /')
```

```
3

```

## 队列

### 简介

添加新项的一端称为队尾，移除项的一端称为队首，先进先出（FIFO） <br/> * `Queue()` 创建一个空的新队列。 它不需要参数，并返回一个空队列。 <br/> * `enqueue(item)` 将新项添加到队尾。 它需要 item 作为参数，并不返回任何内容。 <br/> * `dequeue()`从队首移除项。它不需要参数并返回 item。 队列被修改。 <br/> * `isEmpty()` 查看队列是否为空。它不需要参数，并返回布尔值。 <br/> * `size()`返回队列中的项数。它不需要参数，并返回一个整数。 <br/> <img alt="" src="https://raw.githubusercontent.com/ds19991999/githubimg/master/picgo/20180729190741.png" title=""/>

### Python实现队列

假定队尾在列表中的位置为 0，入队（队尾）为 O(n)，出队为 O(1)。

```
class Queue():
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self,item):
        self.items.pop()
    def size(self):
        return len(self.items)
```

```
q = Queue()
q.enqueue(888)
q.enqueue('11e')
print q.size()
print q.items
```

```
2
['11e', 888]

```

### 模拟：烫手山芋

首先，让我们看看孩子们的游戏烫手山芋，在这个游戏中，孩子们围成一个圈，并尽可能快的将一个山芋递给旁边的孩子。在某一个时间，动作结束，有山芋的孩子从圈中移除。游戏继续开始直到剩下最后一个孩子。

```
from pythonds.basic.queue import Queue
def hotPotato(namelist,num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)
    while simqueue.size()&gt;1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()
    return simqueue.dequeue()
print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))
```

```
Susan

```

## 双端队列Deque

### 简介

### Python实现Deque

```
class Deque:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def addFront(self,item):
        self.items.append(item)
    def addRear(self,item):
        self.items.insert(0,item)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
```

### 回文检查

如`radar toot madam`，我们先将字符串存入deque，如果队首队尾元素相同，删除队首队尾，直至只剩下一个字符或者0个字符

```
from pythonds.basic.deque import Deque
def palchecker(astring):
    chardeque = Deque()
    for ch in astring:
        chardeque.addRear(ch)
    stillEqual = True

    while chardeque.size()&gt;1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False
    return stillEqual
print(palchecker("lsdkjfskf"))
print(palchecker("radar"))
```

```
False
True

```

## 无序列表

### 简介

### 实现无序列表：链表

```
# 定义链表结点
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,newdata):
        self.data = newdata
    def setNext(self,newnext):
        self.next = newnext
```

```
temp = Node(666)
temp.getData()
```

```
666

```

```
# 定义无序链表类，只需要指出第一个结点的位置
# 空链表
class UnorderedList:
    def __init__(self):
        self.head = None
```

## 有序列表抽象数据结构
