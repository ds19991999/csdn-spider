# 原创
：  03-廖雪峰Git教程笔记

# 03-廖雪峰Git教程笔记

# 廖雪峰Git教程笔记

## 教程导图

## 集中式和分布式

## 配置信息

```
git config --global user.name "Your Name"
git config --global user.email "email@example.com"
```

## 创建版本库

## 修改文件并提交

```
git status  # 查看当前状态
git diff README.TXT # 查看被修改的文件具体修改的内容
```

## 版本回退

```
# version1 README.txt
Git is a version control system.
Git is free software.

# version2 README.txt
Git is a distributed version control system.
Git is free software.

# version3 README.txt
Git is a distributed version control system.
Git is free software distributed under the GPL.

```

```
git reset --hard &lt;版本号&gt;
```

## 工作区和暂存区

## 管理修改

## 撤销修改

## 删除文件

## 远程仓库

## 分支管理：

### 创建与合并分支：

### 删除指针，也就是删除指针而已

```
# 创建dev分支，此时远程库并没有dev分支，-b表示创建并切换
git checkout -b dev
# 相当于
git branch dev
git checkout dev

# 查看当前分支
git branch

# dev上面完成开发之后，合并到marster分支
git merge dev
# 这时master上面的内容就和dev一样,也就是直接把master指向dev的当前提交，所以合并速度非常快。

# 删除dev分支
git branch -d dev
# 安全起见，使用分支完成某个任务，合并后再删掉分支
```

### 冲突解决：

### 分支管理策略：

### Bug分支：

```
# 查看当前分支（dev），发现未提交的文件，但由于未完成，所以不想提交
git status

# 保存当前分支未提交的文件，即保存工作现场
git stash

# 假设master分支的bug需要修复
git checkout master

# 创建master的分支issue-101修复bug
git checkout -b issue-101

# 修复完bug之后，提交并合并
git add .
git commit -m "fix bug 101"
git checkout master
git merge --no-ff -m "merged bug fix 101" issue-101

# 切换至dev分支进行未完成的开发
git status   # 发现工作区是干净的
git stash list # 此时应该可以看到之前保存的信息

# 方式一
git stash apply # 恢复，但是恢复后，stash内容并不删除
git stash drop  #删除stash内容

# 方式二
git stash pop # 相当于上面的两步

git stash list # 此时就看不到保存的工作区现场了

# 对于多次stash
# 先查看stash
git stash list
# 再指定恢复的的现场
git stash apply stash@{0}
```

### Feature分支：

```
# 开发代号为Vulcan的新功能
git checkout -b feature-vulcan

# 之后就是git add, git commit

# 切回dev合并
git checkout dev
git branch -d feature-vulcan

# 如果此时还未提交，但由于紧急情况需要取消该任务，该分支必须删除的时候
git branch -d feature-vulcan   # 发现并不能删除分支
# 强行删除
git branch -D feature-vulcan
```

### 多人协作：

```
# 指定本地dev分支与远程origin/dev分支的链接
git branch --set-upstream-to=origin/dev dev

# 之后再pull
git pull

# 出现合并冲突--解决方法同上
# 最后push
git push origin dev
```

### Rebase：

## 标签管理

### 创建标签

```
# 切换打标签的分支
git branch
git checkout master

# 然后就可以打标签了
git tag v1.0

# 查看所有标签
git tag

# 为过去的提交打标签
git log --pretty=oneline --abbrev-commit
git tag v0.9 a793aa9 # a793aa9是commit id

# 标签是按字母排序的,可以查看标签信息
git show &lt;tagname&gt;

# 创建带有说明的标签，用-a指定标签名，-m指定说明文字：
git tag -a v0.1 -m "version 0.1 released" 1094adb

# 插卡说明文字
git show &lt;tagname&gt;
```

### 删除标签

```
# 删除标签
git tag -d v1.0

# 将某个标签对应的版本推送到远程仓
git push origin v1.0

# 一次性推送全部尚未推送的本地标签
git push origin --tags

# 删除远程标签
# 先本机删除
git tag -d v0.9
# 再远程删除
git push origin :refs/tags/v0.9
```

### GitHub Pages

### 使用码云仓

## 自定义Git

```
# 让Git显示颜色
git config --global color.ui true
```

### 忽略特殊文件

```
# Windows:
Thumbs.db
ehthumbs.db
Desktop.ini

# Python:
*.py[cod]
*.so
*.egg
*.egg-info
dist
build

# My configurations:
db.ini
deploy_key_rsa
```

### 配置别名

```
# 配置lg,查看分支合并情况
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)&lt;%an&gt;%Creset' --abbrev-commit"
```

## 搭建Git服务器

```
# 安装git
sudo apt-get install git

# 创建一个git用户，用来运行git服务
sudo adduser git

# 创建证书登录
收集所有需要登录的用户的公钥，就是他们自己的id_rsa.pub文件，
把所有公钥导入到/home/git/.ssh/authorized_keys文件里，一行一个

# 初始化Git仓库
# 先选定一个目录作为Git仓库，假定是/srv/sample.git，在/srv目录下输入命令：
sudo git init --bare sample.git
sudo chown -R git:git sample.git

# 禁用shell登录
# 编辑/etc/passwd文件完成
git:x:1001:1001:,,,:/home/git:/bin/bash
# 改为一旦登录就自动退出：
git:x:1001:1001:,,,:/home/git:/usr/bin/git-shell

# 克隆远程仓库
git clone git@server:/srv/sample.git

# 管理公钥
/home/git/.ssh/authorized_keys

# 管理权限
```
