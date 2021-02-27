# 原创
：  01-第一次使用Jupyter

# 01-第一次使用Jupyter

# 第一次使用Jupyter

具体见个人Python图书馆：[https://ds-ebooks.github.io](https://ds-ebooks.github.io)

# Contents

## 一、更改Jupyter notebook的工作空间

[链接跳转测试](#七、Jupyter中的Markdown)

### 1.直接在工作目录打开

### 2.通过快捷方式属性修改

### 3.修改config文件

```
# The directory to use for notebooks and kernels.
c.NotebookApp.notebook_dir = u'D:\Jupyter'
```

所以，最后我选择第一种方式最直接。

## 二、常用命令

### 1.误删了jupyter notebook中的代码

```
for line in locals()['In']:
    print(line)
```

```
history
```

### 2.jupyter魔法

```
# 当前目录
%pwd
```

```
u'D:\\Python\\Scripts\\notebook'

```

```
%run name.py
# 或者
%matplotlib inline
```

```
# matplotlib画图
%matplotlib inline
```

```
%%writefile foo.py
```

```
%%script python
```

```
%debug
```

```
%autosave 3
```

## 三、Jupyter的各种快捷键

## 四、Jupyter Notebook如何导入代码

> 
即导入代码到jupyter notebook的cell中


### 1.将本地的.py文件load到jupyter的一个cell中

**问题背景**：有一个test.py文件，需要将其载入到jupyter的一个cell中 <br/> test.py内容如下：

```
print "Hello World!"
```

**方法步骤：**

```
# %load test.py
print "HellO World!"
```

Shift Enter运行后，%load test.py被自动加入了注释符号#，test.py中的所有代码都被load到了当前的cell中.

### 2.从网络load代码到jupyter

`%load https://matplotlib.org/examples/color/color_cycle_demo.html`

## 五、Jupyter运行python文件

```
%run test.py
```

```
HellO World!

```

## 六、Jupyter一些其他琐碎用法

### 1.jupyter的cell可以作为unix command使用

```
# 查看python版本：
!python --version 
```

```
Python 2.7.13

```

```
# 运行python文件：
!python test.py
```

```
HellO World!

```

### 2.Magic functions用法

待深究：[The cell magic in Ipython](http://nbviewer.jupyter.org/github/ipython/ipython/blob/1.x/examples/notebooks/Cell%20Magics.ipynb#The-cell-magics-in-IPython)

### 3.获取current working directory

```
current_path = %pwd 
print current_path
```

```
D:\Python\Scripts\notebook

```

### 4.使用Matplotlib绘图

```
# 有时是弹不出图像框的，此时，可以在开头加入:
%matplotlib inline
```

## 七、Jupyter中的Markdown

### 1.链接跳转

```
## 一、更改Jupyter notebook的工作空间
[链接跳转](#更改Jupyter notebook的工作空间)
...
&lt;a id='七、Jupyter中的Markdown'&gt;&lt;/a&gt;
## 七、Jupyter中的Markdown
```

### 2.添加目录功能

```
$ pip2 install jupyter_nbextensions_configurator
$ pip2 install jupyter_contrib_nbextensions
```

### 3.在Jupyter中打开md文件

让`jupyter notebook` 生成md这个大家都会，可是在github当中有很多很好的md文件，如果不能在`jupyter notebook`当中打开体验，实在是太让人难过了。

```
pip install notedown
```

```
c.NotebookApp.contents_manager_class = ‘notedown.NotedownContentsManager’
```

## 八、主题配置

```
pip install --upgrade jupyterthemes
jt -l     //查看能够使用得主题
jt -t chesterish -T -N    //配置主题，chesterish是主题名
jt -r   //恢复默认主题
```

更详细配置参考：[jupyter-themes](https://github.com/dunovank/jupyter-themes)

## 九、Ubuntu上面存在权限问题

### 修改权限

```
//问题1：jupyter无法访问python
sudo chmod 777 ~/.local/share/jupyter/
cd ~/.local/share/jupyter/
ls
sudo chmod 777 runtime/
cd runtime/
ls

//2.jupyter无法访问笔记本
//chown命令可以修改文件或目录所属的用户
$ sudo chown 用户 目录或文件名
//chgrp命令可以修改文件或目录所属的组
$ sudo chgrp 组 目录或文件名
```

### 查看token

```
jupyter-notebook list
```

## 十、Welcome to MkDocs

For full documentation visit [mkdocs.org](http://mkdocs.org).

### Commands

### Project layout

```
mkdocs.yml    # The configuration file.
docs/
    index.md  # The documentation homepage.
    ...       # Other markdown pages, images and other files.

```

## 十一、Git基本命令

```
//建立本地仓库

//初始化本地仓库
$ git init

//添加到暂存区
$ git add .

//提交到工作区
$ git commit -m "first commit"

//添加远程Git仓库
$ git remote add origin https://github.com/ds19991999/VerCodeMFC.git

//删除远程Git仓库
$  git remote rm origin

//合并pull两个不同的项目解决fatal: refusing to merge unrelated histories
$ git pull origin master --allow-unrelated-histories

//使用强制push的方法：
$ git push -u origin master -f
```

## 补充

### 指定图表格式

`Jupyter Notebook` 用 `Matplotlib` 画出来那一坨糊糊的东西会不会跟我一样浑身难受,在画图表的时候加上最后一行就行了，指定他为`'svg'`格式:

```
import matplotlib
import matplotlib.pyplot as plt
%matplotlib inline
%config InlineBackend.figure_format = 'svg'
```

### 导出md格式去掉代码

假如你的`jupyter notebook`是导出一个报告给业务人员看的，他们不想看到那些密密麻麻的代码，只想留下`markdown`和图表，在`jupyter notebook`加入下面这段代码就好:

```
import IPython.core.display as di
di.display_html('&lt;script&gt;jQuery(function(){if (jQuery("body.notebook_app").length == 0) { jQuery(".input_area").toggle();jQuery(".prompt").toggle();}});
                &lt;/script&gt;', raw=True)
```

### matplotlib显示中文

配置文件中加入：

Python27

```
import seaborn as sns
import sys# print sys.getdefaultencoding()# ipython notebook中默认是ascii编码 
reload(sys)
sys.setdefaultencoding('utf8')
```

具体参见：[装扮你的Jupyter](https://zhuanlan.zhihu.com/p/26739300?group_id=843868091631955968)
