# 原创
：  Git提交本地项目或文件

# Git提交本地项目或文件

> 
update: 2018-06-05


## 一、基本命令

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

## 二、常见问题汇总

### 1.出现邮箱限制
