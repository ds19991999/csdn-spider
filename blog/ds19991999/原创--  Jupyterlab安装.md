# 原创
：  Jupyterlab安装

# Jupyterlab安装

# Jupyter小结

### 安装JupyterLab

使用`pip`安装：

```
pip install jupyterlab
# 必须将用户级目录添加 到环境变量才能启动
pip install --userbinPATHjupyter lab

```

使用以前版本的`Notebook`安装：

```
jupyter serverextension enable --py jupyterlab --sys-prefix

```

启动`JupyterLab`

```
jupyter lab

```

由于`JupyterLab`是经典`Jupyter Notebook`服务器的服务器扩展，因此您可以通过调用 和访问URL 来启动JupyterLab 。`jupyter notebook /lab`

修改`config`:`jupyter notebook --generate-config` ，找到配置文件目录修改

```
# The directory to use for notebooks and kernels.
c.NotebookApp.notebook_dir = u'D:\Jupyter'

```

安装常用插件：

```
# 目录功能
$ pip2 install jupyter_nbextensions_configurator
$ pip2 install jupyter_contrib_nbextensions
# 支持md文件
pip install notedown
配置c.NotebookApp.contents_manager_class = ‘notedown.NotedownContentsManager’
# 主题
pip install --upgrade jupyterthemes0

```

### 常用命令

```
######################## magic命令 ##########################
# 找回误删的代码,使用locals()函数
for line in locals()["In"]:
    print line
# 或者
%hist/hist/%history/history

%pwd         # 显示当前目录，目录'/'由'\\'代替

%matplotlib #在笔记本内部加这行就不需要plt.show()函数
# 脚本里去掉这行加上 plt.show()显示图片

# 重写test.py文件
%%writefile test.py 或者 %%file test.py

# 加载文件
%load test.py

%run name.py # 运行脚本

# Debug模式
%debug  输入exit退出

# 设置当前文件每三秒保存一次
%autosave 3

# 查看当前变量空间
%whos

# 重置当前变量空间
%reset -f

# mkdir产生新文件夹
%mkdir test

# rmdir删除文件夹
%rmdir test

# `_`使用上个cell的输出结果

######################作为unix command使用###################
# 查看python版本
!python --version

# 运行Python文件
!python test.py

!ping baidu.com

!python -m pip install update pip

```

### Jupyter的各种快捷键

一下都是退出编辑模式的命令：
