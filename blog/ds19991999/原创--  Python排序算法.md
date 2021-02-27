# 原创
：  Python排序算法

# Python排序算法

```
# coding:utf-8
# 整数排序

# 插入排序1
def insert_sort1(A):
    length = len(A)
    if length &lt; 2:
        return A
    # 1---length-1
    for i in range(1, length):
        key = A[i]
        j = i - 1
        while j&gt;= 0 and A[j] &gt; key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    return A

# 插入排序2
def insert_sort2(A):
    length = len(A)
    # 0--length-1
    for i in range(0, length):
        for j in range(i+1, length):
            if A[i] &gt; A[j]:
                tmp = A[j]
                A.pop(j)
                A.insert(i, tmp)
    return A

# 冒泡排序1
def bubble_sort1(A):
    length = len(A)
    while length&gt;0:
        # 0--length-2
        for i in range(0, length-1):
            if A[i]&gt;A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
        length -= 1
    return A

# 冒泡排序2
def bubble_sort2(A):
    length = len(A)
    if length &lt; 2:
        return A
    for i in range(0, length):
        for j in range(0, length-i):
            if j + 1 &lt; length and A[j] &gt; A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A

# 选择排序
def select_sort(A):
    length = len(A)
    for i in range(0, length):
        x = A[i]
        index = i
        for j in range(i+1, length):
            if x &gt; A[j]:
                x = A[j]
                index = j
        A[i], A[index] = A[index], A[i]
    return A

# 快速排序1
def quik_sort(A, left, right):
    '''
    快速排序
    :param A:
    :param left:
    :param right:
    :return:
    '''
    # 跳出递归判断
    if left &gt;= right:
        return A

    # 选择参考点，该调整范围的第一个值
    key = A[left]
    low = left
    hight = right

    # 循环判断直到遍历全部
    while left &lt; right:
        # 从右边开始查找小于参考点的值
        while left &lt; right and A[right]&gt;=key:
            right -= 1
        # 这个位置的值先放在左边
        A[left] = A[right]

        # 从左边开始查找大于参考点的值
        while left &lt; right and A[left] &lt;= key:
            left +=1
        # 这个位置的值放在右边
        A[right] = A[left]

    # 写回改成的值
    A[left] = key

    # 递归，并返回结果
    quik_sort(A, low, left-1)
    quik_sort(A, left+1, hight)
    return A

# 堆排序
def sift_down(arr, start, end):
    root = start
    while True:
        # 从root开始对最大堆调整
        child = 2 * root + 1
        if child &gt; end:
            break

        # 找出两个child中交大的一个
        if child + 1 &lt;= end and arr[child] &lt; arr[child + 1]:
            child += 1

        if arr[root] &lt; arr[child]:
            # 最大堆小于较大的child, 交换顺序
            arr[root], arr[child] = arr[child], arr[root]

            # 正在调整的节点设置为root
            root = child
        else:
            # 无需调整的时候, 退出
            break

def heap_sort(A):
    # 从最后一个有子节点的孩子还是调整最大堆
    first = len(A) // 2 - 1
    for start in range(first, -1, -1):
        sift_down(A, start, len(A) - 1)

    # 将最大的放到堆的最后一个, 堆-1, 继续调整排序
    for end in range(len(A) -1, 0, -1):
        A[0], A[end] = A[end], A[0]
        sift_down(A, 0, end - 1)
    return A

# 二路归并排序
def merge_sort(A):
    if len(A) &lt;= 1:
        return A
    num = len(A) / 2
    left = merge_sort(A[:num])
    right = merge_sort(A[num:])
    return merge(left, right)


def merge(left, right):
    r, l = 0, 0
    result = []
    while l &lt; len(left) and r &lt; len(right):
        if left[l] &lt; right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += right[r:]
    result += left[l:]
    return result

def main():
    A = [9,10,8,3,4,6,1,2,0,5]
    # print insert_sort1(A)
    # print insert_sort2(A)
    # print bubble_sort1(A)
    # print bubble_sort2(A)
    # print select_sort(A)
    # print quik_sort(A, 0, len(A)-1)
    # print heap_sort(A)
    print merge_sort(A)

if __name__=='__main__':
    main()
```
