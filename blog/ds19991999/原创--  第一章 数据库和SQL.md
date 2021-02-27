# 原创
：  第一章 数据库和SQL

# 第一章 数据库和SQL

> 
参考书籍：[https://book.douban.com/subject/27055712/](https://book.douban.com/subject/27055712/)


### 目录

## 1、法则

## 2、SQL书写规则

## 3、权限管理

MySQL 的账户信息保存在 mysql 这个数据库中。

```
USE mysql;
SELECT user FROM user;

```

**创建账户**

新创建的账户没有任何权限。

```
CREATE USER myuser IDENTIFIED BY 'mypassword';

```

**修改账户名**

```
RENAME myuser TO newuser;

```

**删除账户**

```
DROP USER myuser;

```

**查看权限**

```
SHOW GRANTS FOR myuser;

```

**授予权限**

账户用 username@host 的形式定义，username@% 使用的是默认主机名。

```
GRANT SELECT, INSERT ON mydatabase.* TO myuser;

```

**删除权限**

GRANT 和 REVOKE 可在几个层次上控制访问权限：

```
REVOKE SELECT, INSERT ON mydatabase.* FROM myuser;

```

**更改密码**

必须使用 Password() 函数

```
SET PASSWROD FOR myuser = Password('new_password');

```

## 4、SQL常用命令

修改MySQL提示符:

```
mysql -uroot -proot --prompt 提示符 # 连接客户端时通过参数指定
prompt 提示符 # 连接客户端之后，通过prompt指定

```

<th align="center">参数</th><th align="center">描述</th>
|------
<td align="center">\D</td><td align="center">完整的日期</td>
<td align="center">\d</td><td align="center">当前数据库</td>
<td align="center">\h</td><td align="center">服务器名称</td>
<td align="center">\u</td><td align="center">当前用户</td>

```
CREATE {DATEBASE | SCHEMA} [IF NOT EXISTS] db_name [DEFAULT] CHARACTER SET [=] charset_name

```

```
SHOW {DATABASE | SCHEMAS} [LIKE "pattern" | WHERE expr]

```

```
SHOW WARNINGS;

```

```
SHOW CREATE  DATABASE t1;

```

```
ALTER {DATABASE | SCHEMA} [db_name] [DEFAULT] CHARACTER SET [=] charset_name

```

```
DROP {DATABASE |SCHEMA} [IF EXISTS] db_name;

```

```
SELECT *
FROM mytable; -- 注释
/* 注释1
   注释2 */

```

## 5、表的创建、修改和插入

### 创建表

```

CREATE TABLE mytable (
  id INT NOT NULL AUTO_INCREMENT,
  col1 INT NOT NULL DEFAULT 1,
  col2 VARCHAR(45) NULL,
  col3 DATE NULL,+
  PRIMARY KEY (`id`)); --设定主键

```

### 修改表

添加列

```
ALTER TABLE mytable
ADD col CHAR(20);

```

删除列

```
ALTER TABLE mytable
DROP COLUMN col;

```

**删除表**

```
DROP TABLE mytable;

```

修改表名

```
ALTER TABLE &lt;原表名&gt; to &lt;新表名&gt;

```

### 插入表数据

普通插入，不指定列则要求全部要插入

```
START TRANSACTION; 
INSERT INTO mytable(col1, col2)
VALUES(val1, val2);
...
COMMIT;

```
