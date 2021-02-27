# 原创
：  Shell流程控制：if 分支结构

# Shell流程控制：if 分支结构

## 流程控制：if 分支结构

### if

```
x=5
if [ $x = 5 ]; then
    echo "x equals 5."
else
    echo "x does not equal 5."
fi

```

`echo $?`查看命令执行返回的状态。经常与 if 一块使用的命令是 test，它执行各种各样的检查与比较：

```
test expression
[ expression ]

```

**测试文件表达式：**

|表达式|如果下列条件为真则返回True
|------
|file1 -ef file2|file1 和 file2 拥有相同的索引号（通过硬链接两个文件名指向相同的文件）。
|file1 -nt file2|file1新于 file2。
|file1 -ot file2|file1早于 file2。
|-b file|file 存在并且是一个块（设备）文件。
|-c file|file 存在并且是一个字符（设备）文件。
|-d file|file 存在并且是一个目录。
|-e file|file 存在。
|-f file|file 存在并且是一个普通文件。
|-g file|file 存在并且设置了组 ID。
|-G file|file 存在并且由有效组 ID 拥有。
|-k file|file 存在并且设置了它的“sticky bit”。
|-L file|file 存在并且是一个符号链接。
|-O file|file 存在并且由有效用户 ID 拥有。
|-p file|file 存在并且是一个命名管道。
|-r file|file 存在并且可读（有效用户有可读权限）。
|-s file|file 存在且其长度大于零。
|-S file|file 存在且是一个网络 socket。
|-t fd|fd 是一个定向到终端／从终端定向的文件描述符 。 这可以被用来决定是否重定向了标准输入／输出错误。
|-u file|file 存在并且设置了 setuid 位。
|-w file|file 存在并且可写（有效用户拥有可写权限）。
|-x file|file 存在并且可执行（有效用户有执行／搜索权限）。

```
test_file () {
    # test-file: Evaluate the status of a file
    FILE=~/.bashrc
    if [ -e "$FILE" ]; then
        if [ -f "$FILE" ]; then
            echo "$FILE is a regular file."
        fi
        if [ -d "$FILE" ]; then
            echo "$FILE is a directory."
        fi
        if [ -r "$FILE" ]; then
            echo "$FILE is readable."
        fi
        if [ -w "$FILE" ]; then
            echo "$FILE is writable."
        fi
        if [ -x "$FILE" ]; then
            echo "$FILE is executable/searchable."
        fi
    else
        echo "$FILE does not exist"
        #  函数中用return 语句来代替 exit 命令
        return 1
    fi
}

```

**测试字符串表达式：**

|表达式|如果下列条件为真则返回True
|------
|string|string 不为 null。
|-n string|字符串 string 的长度大于零。
|-z string|字符串 string 的长度为零。
|string1 = string2string1 == string2|string1 和 string2 相同。 单或双等号都可以，不过双等号更受欢迎。
|string1 != string2|string1 和 string2 不相同。
|string1 &gt; string2|sting1 排列在 string2 之后。
|string1 &lt; string2|string1 排列在 string2 之前。

> 
当与 test 一块使用的时候， &gt; 和 &lt; 表达式操作符必须用引号引起来(或者是用反斜杠转义)


### 整型表达式

测试整数表达式:

|表达式|如果为真…
|------
|integer1 -eq integer2|integer1 等于 integer2。
|integer1 -ne integer2|integer1 不等于 integer2。
|integer1 -le integer2|integer1 小于或等于 integer2。
|integer1 -lt integer2|integer1 小于 integer2。
|integer1 -ge integer2|integer1 大于或等于 integer2。
|integer1 -gt integer2|integer1 大于 integer2。

### 更现代的测试版本

```
# 加强的 test 命令替代物
[[ expression ]]
# 添加的另一个功能是==操作符支持类型匹配
if [[ $FILE == foo.* ]]; then
...

```

`string1 =~ regex`:匹配正则表达式则返回真

### (( )) - 为整数设计

`(( ))` 复合命令,支持一套 完整的算术计算，`(( ))`被用来执行算术真测试。如果算术计算的结果是非零值，则其测试值为真。

```
# 判断一个数的奇偶性
if (( ((INT % 2)) == 0)); then
	echo "INT is even."
else
	echo "INT is odd."

```

### 结合表达式

逻辑操作符：

|操作符|测试|[[ ]] and (( ))
|------
|AND|-a|&amp;&amp;
|OR|-o|||
|NOT|!|!

### 控制操作符：分支的另一种方法

```
command1 &amp;&amp; command2
command1 || command2

```

对于 &amp;&amp; 操作符，先执行 command1，只有command1 执行成功后， 才会执行 command2。对于 || 操作符，先执行 command1，只有command1 执行失败后， 才会执行 command2。

## 读取键盘输入

### read - 从标准输入读取数值

```
read [-options] [variable...]

```

```
#!/bin/bash
# read-integer: evaluate the value of an integer.
#  -n 选项（其会删除输出结果末尾的换行符）的 echo 命令，来显示提示信息
echo -n "Please enter an integer -&gt; "
read int
if [[ "$int" =~ ^-?[0-9]+$ ]]; then
    if [ $int -eq 0 ]; then
        echo "$int is zero."
    else
        if [ $int -lt 0 ]; then
            echo "$int is negative."
        else
            echo "$int is positive."
        fi
        if [ $((int % 2)) -eq 0 ]; then
            echo "$int is even."
        else
            echo "$int is odd."
        fi
    fi
else
    echo "Input value is not an integer." &gt;&amp;2
    exit 1
fi

```

```
alien@localhost:~ $ info-test
Please enter an integer -&gt; 3
3 is positive.
3 is odd.
alien@localhost:~ $ info-test
Please enter an integer -&gt; 6
6 is positive.
6 is even.

```

read 可以给多个变量赋值：

```
read var1 var2 var3 var4 var5

```

执行脚本时输入时以空格隔开，默认值为空，额外的输入数据会包含到最后一个变量中。

如果 read 命令之后没有列出变量名，则一个 shell 变量，默认的REPLY，将会包含 所有的输入：

**read选项：**

|选项|说明
|------
|-a array|把输入赋值到数组 array 中，从索引号零开始。我们 将在第36章中讨论数组问题。
|-d delimiter|用字符串 delimiter 中的第一个字符指示输入结束，而不是一个换行符。
|-e|使用 Readline 来处理输入。这使得与命令行相同的方式编辑输入。
|-n num|读取 num 个输入字符，而不是整行。
|-p prompt|为输入显示提示信息，使用字符串 prompt。
|-r|Raw mode. 不把反斜杠字符解释为转义字符。
|-s|Silent mode. 不会在屏幕上显示输入的字符。当输入密码和其它确认信息的时候，这会很有帮助。
|-t seconds|超时. 几秒钟后终止输入。若输入超时，read 会返回一个非零退出状态。
|-u fd|使用文件描述符 fd 中的输入，而不是标准输入。

-t和-sp 选项，读取“秘密”输入，在特定的时间内 输入没有完成，就终止输入。

### IFS

**IFS** 的默认值包含一个空格，一个 tab，和一个换行符，每一个都会把 字段分割开。

```
IFS=":" read user pw uid gid name home shell &lt;&lt;&lt; "$file_info"

```

这一行由三部分组成：对一个变量的赋值操作，一个带有一串参数的 read 命令，和一个奇怪的新的重定向操作符。这个 `&lt;&lt;&lt;` 操作符指示一个 here 字符串。**不能把 管道用在 read 上**----管道线 会创建子 shell。

### 菜单

```
#!/bin/bash
# read-menu: a menu driven system information program
clear
echo "
Please Select:

    1. Display System Information
    2. Display Disk Space
    3. Display Home Space Utilization
    0. Quit
"
read -p "Enter selection [0-3] &gt; "

if [[ $REPLY =~ ^[0-3]$ ]]; then
    if [[ $REPLY == 0 ]]; then
        echo "Program terminated."
        exit
    fi
    if [[ $REPLY == 1 ]]; then
        echo "Hostname: $HOSTNAME"
        uptime
        exit
    fi
    if [[ $REPLY == 2 ]]; then
        df -h
        exit
    fi
    if [[ $REPLY == 3 ]]; then
        if [[ $(id -u) -eq 0 ]]; then
            echo "Home Space Utilization (All Users)"
            du -sh /home/*
        else
            echo "Home Space Utilization ($USER)"
            du -sh $HOME
        fi
        exit
    fi
else
    echo "Invalid entry." &gt;&amp;2
    exit 1
fi

```

第一部分显示菜单和用户输入。第二部分确认用户反馈，并执行 选择的行动。
