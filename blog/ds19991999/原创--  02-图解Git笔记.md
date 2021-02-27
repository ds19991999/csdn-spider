# 原创
：  02-图解Git笔记

# 02-图解Git笔记

# 图解Git笔记

> 
参考：[图解 Git](http://marklodato.github.io/visual-git-guide/index-zh-cn.html)


## 基本用法

## 命令详解

### Diff

```
git diff maint(分支名)
git diff b325c da985
git diff --cached
git diff
git diff HEAD
```

### Commit

或者

如果想**更改一次提交**，使用 `git commit --amend`。git会使用与当前提交相同的父节点进行一次新提交，旧的提交会被取消。 

### Checkout

### Reset

### Merge

### Cherry Pick

### Rebase
