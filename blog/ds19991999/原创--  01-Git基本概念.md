# 原创
：  01-Git基本概念

# 01-Git基本概念

# Git基本概念

> 
参考：[CyC2018-Git](https://github.com/CyC2018/Interview-Notebook/blob/master/notes/Git.md)


## Git常用命令步骤

### 第一次提交

```
//初始化本地仓库
git init

//登录信息
git config --global user.name "ds19991999"
git config --global user.email "2508328787@qq.com"

//添加到暂存区
git add .

//提交到工作区
git commit -m "first commit"

//添加远程Git仓库
git remote add origin https://github.com/ds-ebooks/jupyter-notebook.git

//在本地产生一个gh-pages分支，前提是你的Github上面也有一个gh-pages分支
git branch gh-pages

//切换本地分支
git checkout gh-pages

//查看分支
git branch -a

//查看当前状态
git status

//合并pull两个不同的项目
//解决fatal: refusing to merge unrelated histories
//远端中的文件，本地如果不存在会保留，这一步可以跳过
git pull origin master --allow-unrelated-histories

//使用强制push的方法：
git push -u origin master -f
```

### 之后的本地提交

```
git add .

git commit -m "..."

//这一步可以忽略
git pull origin master --allow-unrelated-histories

git push -u origin master -f
```

## 集中式和分布式

## Git 的中心服务器

## 工作流

可以跳过暂存区域直接从分支中取出修改或者直接提交修改到分支中 :

## 分支实现

## 冲突

```
&lt;&lt;&lt;&lt;&lt;&lt;&lt; HEAD
Creating a new branch is quick &amp; simple.
=======
Creating a new branch is quick AND simple.
&gt;&gt;&gt;&gt;&gt;&gt;&gt; feature1
```

## Fast forward

```
git merge --no-ff -m "merge with no-ff" dev
```

## 分支管理策略

## 储藏（Stashing）

## SSH 传输设置

## .gitignore 文件

忽略以下文件：

## 参考资料
