# 原创
：  Python基础教程总结（下）

# Python基础教程总结（下）

# Python基础教程总结（下）

> 
参考：[https://book.douban.com/subject/4866934/](https://book.douban.com/subject/4866934/) ，基于Python2.x.
上一篇：[Python基础教程总结（上）](https://blog.csdn.net/ds19991999/article/details/83217617)


学东西快是我最大的优点和缺点，因为学的越快，忘的也越快，所以不得已才经常总结一些基本知识。。。

## 第十章 标准库

```
# sys.path里面存放供解释器查找模块的路径列表
import sys
sys.path.append("C:/python")
# Unix系统中必须使用完整路径，也可以用expanduser()
sys.path.expanduser("~/python")
if __name__=="__main__":
    main()
pprint.pprint(sys.path) #更高级的打印函数

# 假设有一个copy模块，用dir查看所有特性（类、函数、变量）
[n for n in dir(copy) if not n.startswith("_")]
copy.__all__ #模块的共有接口，比喻from copy import*的时候导入的就是这个列表里的模块

help(copy.copy) #查看copy函数
print copy.copy.__doc__ #查看文档字符串

# 源码阅读，查找copy模块的路径
&gt;&gt;&gt; print copy.__file__
D:\Soteware\Python\Python2\lib\copy.pyc

```

> 
一些常用的标准库见笔记：[Note](http://nbviewer.jupyter.org/github/ds19991999/Note/tree/dev/)


## 第十一章 文件和流

<th align="center">值</th>|描述
|------
<td align="center">`r`</td>|读模式
<td align="center">`w`</td>|写模式
<td align="center">`a`</td>|追加模式
<td align="center">`b`</td>|二进制模式(可添加到其他模式中使用)
<td align="center">`+`</td>|读/写模式(可添加到其他模式中使用)

```
f = open("PATH","w")
f.write("strings")
f.close()

# 文件会自动关闭
with open("PATH","rw"):
	do_something

f.seek(size) #指定当前位置
f.tell() #返回当前位置
read(n)\read()\readline()\readlines()的区别

```
