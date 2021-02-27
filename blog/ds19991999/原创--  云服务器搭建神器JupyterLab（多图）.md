# 原创
：  云服务器搭建神器JupyterLab（多图）

# 云服务器搭建神器JupyterLab（多图）

# 云服务器搭建神器JupyterLab（多图）

> 
[`JupyterLab`](https://github.com/jupyterlab/jupyterlab)是一个交互式的开发环境，其用于应对包含着`notebook`、代码以及数据的工作场景。


## 1、前言

**如果说`vim`是编辑器之神，那么`JupyterLab`就是笔记本之神。**

从2017年开始我注意到这一神奇的`IDE`笔记本，第一眼见到它，就觉得它真的太强大了，作为一个交互式的`Python`开发工具，其实也不算开发工具，准确的来说，它是一个演示代码的科学数据工具，支持`markdown`预览，支持[Draw](https://www.draw.io/)扩展，支持丰富的文件格式和多种开发语言，拥有众多[插件](https://github.com/jupyterlab?utf8=%E2%9C%93&amp;q=extension&amp;type=&amp;language=)诸于`GitHub`， `Google-Dirve`， `Git`和`TOC`，更重要的是，它是把浏览器当作开发工具，十分有创意。[`JupyterLab`](https://github.com/jupyterlab/jupyterlab)的开发者众多，`GitHub`上面的`isuue`也十分活跃，众多的大牛开发者也纷纷加入到`JupyterLab`的阵营，为`JupyterLab`的发展作贡献，`JupyterLab`得到迅速发展。

好的工具当然是要好好利用了，回归正题，怎样通过云服务器搭建一个可远程使用的`JupyterLab`?

## 2、购买云服务器`ECS`

这里我就直接买了阿里的学生优惠的`ECS`，9.9元/月，价格算是良心了，这里可以领一下优惠券：[阿里云限时礼包](https://promotion.aliyun.com/ntms/yunparter/invite.html?userCode=vya2etaw)。亚马逊还有每个账户免费使用一年云服务器的机会，也可以用一用。购买之后创建实例，启动云服务器，我这里用的是`Ubuntu 16.04`镜像，记住你设置的`root`密码。如果没有特殊要求，可以直接使用`root`用户进行下面操作，不必新建用户。

## 3、登录ECS并安装必要软件

```
sudo apt-get install ssh
ssh root@公网ip

```

这个ip是公网ip，在你购买的服务器运营商的实例列表里，如果不出意外就可以登录ECS了。

### 3.1 先做好准备工作

比喻你添加ppa源的时候出现这种情况

```
root@iZwz9huxtbd86xp91s3j16Z:~# sudo add-apt-repository ppa:chronitis/jupyter
sudo: add-apt-repository: command not found

```

解决办法

```
sudo apt-get install software-properties-common

```

### 3.2 关于`pip`的问题

#### 安装pip

```
sudo apt-get install python-pip python-dev build-essential 
sudo pip install --upgrade pip 
sudo pip install --upgrade virtualenv 

```

```
sudo apt-get install python-setuptools python-dev build-essential 

```

```
sudo easy_install pip 

```

```
sudo pip install --upgrade virtualenv 

```

```
sudo apt-get install python3-pip

```

```
sudo apt-get install python-pip

```

#### 升级`pip`

```
sudo pip3 install --upgrade pip
sudo pip2 install --upgrade pip
sudo pip install --upgrade pip

```

#### 更换`pip`源加速下载

```
cat &gt; ~/.pip/pip.conf
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple

```

`npm`和`yarn`也可以换源，更简单，自行`google`。

`pip`国内的一些镜像包,换源之后出现`python2`版本过低的情况导致以前的包下载不了，那就直接将文件夹`~/.pip/pip.conf`删除就可以恢复原来的源。

#### `pip`指向问题

有时候会出现`pip,pip2,pip3`都TM指向`python2`，这个之后就需要改一下这这三个文件。

编辑这三个文件，将第一行注释分别改为python\python2\python3

```
~ $which pip
/usr/local/bin/pip
21:36 alien@alien-Inspiron-3443:
~ $which pip2
/usr/local/bin/pip2
21:36 alien@alien-Inspiron-3443:
~ $which pip3
/usr/local/bin/pip3

```

### 3.3 安装`yarn`和`nodejs`

#### 配置仓库

```
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list

```

#### 安装`yarn`

```
sudo apt-get update
sudo apt-get install yarn

```

注意这里`yarn`自动安装了`nodejs`，不过版本太低，安装`jupyterlab`的时候会出问题，而且使用`n`或者`nvm`安装的`nodejs`也有问题，总之`nodejs`要按照下面这种方式就没事，这个是官方的`bug`，官方`issue`也提到过，但是目前还未解决。

#### 安装`nodejs`

创建一个新文件，输入两行`deb`，结束之后`Ctrl+C`:

```
cat &gt; /etc/apt/sources.list.d/nodesource.list
deb https://deb.nodesource.com/node_6.x xenial main
deb-src https://deb.nodesource.com/node_6.x xenial main

```

导入公匙并安装`nodejs`，这个版本的`nodejs`对`jupyterlab`支持比较友好。

```
curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | sudo apt-key add -
sudo apt-get update
apt-cache policy nodejs
sudo apt-get install nodejs
nodejs --version

```

#### 安装`ipython,matplotlib,scipy,pandas,numpy`

最好`python2`和`python3`都安装。

## 4、安装`JupyterLab`及其配置

记住使用`pip2`安装，如果你用`pip3`安装的话可能会出现版本兼容问题。

```
sudo pip2 install jupyterlab

```

生成密码

```
jupyter-notebook password

```

### 4.1 创建哈希密码

```
ipython
from notebook.auth import passwd
passwd()
# 输入你自己设置登录JupyterLab界面的密码，
# 然后就会生产下面这样的密码，将它记下来，待会儿用
'sha1:b92f3fb7d848:a5d40ab2e26aa3b296ae1faa17aa34d3df351704'

```

### 4.2 修改`JupyterLab`配置文件

先生成一个配置文件，记下输出的配置文件地址

```
jupyter lab --generate-config

```

修改配置文件，找到下面这几行文件，注释掉并修改成这样。

```
c.NotebookApp.allow_root = True
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.notebook_dir = u'/root/JupyterLab'
c.NotebookApp.open_browser = False
c.NotebookApp.password = u'sha1:b92f3fb7d848:a5d40ab2e26aa3b296ae1faa17aa34d3df351704'
c.NotebookApp.port = 8080

```

对应每行稍微解释一下

```
允许以root方式运行jupyterlab
允许任意ip段访问
设置jupyterlab页面的根目录
默认运行时不启动浏览器，因为服务器默认只有终端嘛
设置之前生产的哈希密码
设置访问端口

```

到此，`JupyterLab`已经安装成功了。

```
jupyter-lab --version
0.33.12
jupyter lab build

```

`jupyter lab build`时间有点久，如果没报错就成功了。但此时你还不能访问`JupyterLab`，还需要添加端口规则，也就是所谓的添加安全组。

## 5、添加安全组

<img alt="" src="https://raw.githubusercontent.com/ds19991999/githubimg/master/picgo20181102230911.png"/><br/> 去ECS控制台添加安全组，不然你无法通过本地浏览器访问`JupyterLab`，设置`8080`端口入方向。<br/> <img alt="" src="https://raw.githubusercontent.com/ds19991999/githubimg/master/picgo20181102231126.png"/>

## 远程访问`JupyterLab`

运行下面命令。

```
# nohup表示ssh终端断开后仍然运行
# &amp;表示允许后台运行
nohup jupyter lab &amp;

```

浏览器输入`公网ip:8080`，就可以访问你的`JupyterLab`了，第一次访问比较慢，耐心一点，如果最终还是无法访问，那么就是你的安全组配置错啦。<br/> <img alt="" src="https://raw.githubusercontent.com/ds19991999/githubimg/master/picgo20181102231458.png"/><br/> 输入密码就可以用了。

## 6、`JupyterLab`扩展安装

查看已经安装的扩展及其状态：

```
jupyter labextension list

```

比喻安装一个扩展`jupyterlab_html`，支持html预览:

```
jupyter labextension install @mflevine/jupyterlab_html

```

卸载扩展:

```
jupyter labextension uninstall @mflevine/jupyterlab_html

```

更新所有扩展:

```
jupyter labextension update --all

```

下面以安装[GitHub](https://github.com/jupyterlab/jupyterlab-github)扩展为例。

### 安装`GitHub`扩展

先去`GitHub`生成一个`token`，记下`token`，待会儿配置要用。

下载安装扩展:

```
jupyter labextension install @jupyterlab/github

```

配置`token`

```
# 在之前的生成的config文件中添加
c.GitHubConfig.access_token = '&lt; YOUR_ACCESS_TOKEN &gt;'

```

需要其他扩展的在[GitHub](https://github.com/)可以自行下载。<br/> <img alt="" src="https://raw.githubusercontent.com/ds19991999/githubimg/master/picgo20181102234041.png"/>

## 7、内核安装与卸载

安装Python内核

```
sudo pip2 install ipykernel
sudo pip3 install ipykernel

```

如果`pip`指向正常的话就可以看到两个`Python`内核了。

查看已经安装的内核

```
jupyter kernelspec list

```

删除你不需要的内核

```
jupyter kernelspec remove &lt;kernel_name&gt;
/root/JupyterLab

```

## 8、域名和`https`配置

域名和SSL配置可以参考这两篇文章：

其实为觉得没必要，毕竟是个人用的工具，没必要搞个域名，不过强迫症就另说了。具体效果是这样的:

## 9、结语

`JupyterLab`的搭建就是这么简单，好的工具就应该好好利用，支持做图，`markdown`，多标签，内部打开网页，`latex`，网页预览，这么好的工具我应该早点发现呀。最后，以秀图结束本文，多多指教！

> 
原创博文，转载注明请注明出处： [https:www.ds-vip.top](https:www.ds-vip.top)

