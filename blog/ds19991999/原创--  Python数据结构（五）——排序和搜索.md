# 原创
：  Python数据结构（五）——排序和搜索

# Python数据结构（五）——排序和搜索

# 排序和搜索

```
15 in [3,3,2,1,4]
```

```
False

```

```
3 in [3,4,5,6]
```

```
True

```

## 顺序查找

```
# 查找列表中的项,假设列表项无序
def sequence_search(alist,item):
    pos = 0
    found = False
    while pos&lt;len(alist) and not found:
        if alist[pos]==item:
            found = True
        else:
            pos += 1
    return found

testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequence_search(testlist, 3))
print(sequence_search(testlist, 13))        
```

```
False
True

```

```
# 查找列表中的项,假设列表项有序
def order_sequence_search(alist,item):
    pos = 0
    found = False
    stop = False
    while pos &lt; len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos]&gt;item:
                stop = True
            else:
                pos += 1
    return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(order_sequence_search(testlist, 3))
print(order_sequence_search(testlist, 13))
```

```
False
True

```

## 二分法查找

```
def binary_search(alist,item):
    first = 0
    last = len(alist)-1
    found = False

    while first&lt;=last and not found:
        mid = (first+last)/2
        if alist[mid]==item:
            found = True
        elif alist[mid]&gt;item:
            last = mid - 1
        else:
            first = mid + 1
    return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binary_search(testlist, 3))
print(binary_search(testlist, 13))        
```

```
False
True

```

```
# 递归实现
def bianary_search(alist,item):
    if len(alist)==0:
        return False
    else:
        mid = len(alist)//2
        if alist[mid]==item:
            return True
        else:
            if item&lt;alist[mid]:
                return bianary_search(alist[:mid],item)
            else:
                return bianary_search(alist[mid+1:],item)
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binary_search(testlist, 3))
print(binary_search(testlist, 13)) 
```

```
False
True

```

## Hash查找

哈希表 是以一种容易找到它们的方式存储的项的集合。哈希表的每个位置，通常称为一个槽，可以容纳一个项，并且由从 0 开始的整数值命名。例如，我们有一个名为 0 的槽，名为 1 的槽，名为 2 的槽，以上。最初，哈希表不包含项，因此每个槽都为空。我们可以通过使用列表来实现一个哈希表，每个元素初始化为None 。Figure 4 展示了大小 m = 11 的哈希表。换句话说，在表中有 m 个槽，命名为 0 到 10。 <br/> <img alt="" src="https://raw.githubusercontent.com/ds19991999/githubimg/master/picgo/20180730133625.png" title=""/>

具体介绍见：[Hash查找](https://github.com/facert/python-data-structure-cn/tree/master/5.%E6%8E%92%E5%BA%8F%E5%92%8C%E6%90%9C%E7%B4%A2/5.5.Hash%E6%9F%A5%E6%89%BE)

```
def hash(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum = sum+ord(astring[pos])
    return sum%tablesize
```

冲突解决： <br/> <img alt="" src="https://raw.githubusercontent.com/ds19991999/githubimg/master/picgo/20180730135953.png" title=""/>

## 排序

```
# 冒泡排序
def bubble_sort_1(alist):
    for j in range(len(alist)-1,0,-1):
        for i in range(j):
            if alist[i]&gt;alist[i+1]:
                alist[i],alist[i+1]=alist[i+1],alist[i]
    return alist
alist = [54,26,93,17,77,31,44,55,20]
print bubble_sort_1(alist)
```

```
[17, 20, 26, 31, 44, 54, 55, 77, 93]

```

```
# 优化冒泡排序，识别有序序列,修改冒泡排序提前停止
def bubble_sort_2(alist):
    exchange = True
    j = len(alist)-1
    while j&gt;0 and exchange:
        exchange = False
        for i in range(j):
            if alist[i] &gt; alist[i+1]:
                alist[i],alist[i+1]=alist[i+1],alist[i]
                exchange = True
        j -= 1
    return alist

alist=[30,20,40,90,50,60,70,80,100,110]
print bubble_sort_2(alist)
```

```
[20, 30, 40, 50, 60, 70, 80, 90, 100, 110]

```

```
# 简单选择排序
def select_sort(alist):
    for i in range(len(alist)):
        k = i
        for j in range(k,len(alist)):
            if alist[k]&gt;alist[j]:
                k = j
        alist[i],alist[k]=alist[k],alist[i]
    return alist
alist = [54,26,93,17,77,31,44,55,20]
print select_sort(alist)
```

```
[17, 20, 26, 31, 44, 54, 55, 77, 93]

```

```
# 插入排序
def insert_sort(alist):
    for i in range(0,len(alist)):
        for j in range(i+1,len(alist)):
            if alist[i]&gt;alist[j]:
                tmp = alist[j]
                alist.pop(j)
                alist.insert(i,tmp)
    return alist
alist = [54,26,93,17,77,31,44,55,20]
print insert_sort(alist)
```

```
[17, 20, 26, 31, 44, 54, 55, 77, 93]

```

```
# 插入排序2
def insert_sort_2(A):
    length = len(A)
    if length &lt; 2:
        return A

    for i in range(1,length-1):
        key = A[i]
        j = i-1
        while j&gt;=0 and A[j]&gt;key:
            A[j+1]=A[j]
            j -= 1
        A[j+1] = key
    return A
alist = [54,26,93,17,77,31,44,55,20]
print insert_sort_2(alist)
```

```
[17, 26, 31, 44, 54, 55, 77, 93, 20]

```

更多排序算法见博客：[Python排序算法](https://blog.csdn.net/ds19991999/article/details/79998011)
