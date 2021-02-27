# 原创
：  Shell流程控制：while/until 循环

# Shell流程控制：while/until 循环

## 流程控制：while/until 循环

### while

```
#!/bin/bash
# while-count: display a series of numbers
count=1
while [ $count -le 5 ]; do
    echo $count
    count=$((count + 1))
done
echo "Finished."

```

优化上一节的菜单脚本：

```
#!/bin/bash
# while-menu: a menu driven system information program
DELAY=3 # Number of seconds to display results
while true; do
    clear
    cat &lt;&lt;- _EOF_
        Please Select:
        1. Display System Information
        2. Display Disk Space
        3. Display Home Space Utilization
        0. Quit
    _EOF_
    read -p "Enter selection [0-3] &gt; "
    if [[ $REPLY =~ ^[0-3]$ ]]; then
        if [[ $REPLY == 1 ]]; then
            echo "Hostname: $HOSTNAME"
            uptime
            sleep $DELAY
            continue
        fi
        if [[ $REPLY == 2 ]]; then
            df -h
            sleep $DELAY
            continue
        fi
        if [[ $REPLY == 3 ]]; then
            if [[ $(id -u) -eq 0 ]]; then
                echo "Home Space Utilization (All Users)"
                du -sh /home/*
            else
                echo "Home Space Utilization ($USER)"
                du -sh $HOME
            fi
            sleep $DELAY
            continue
        fi
        if [[ $REPLY == 0 ]]; then
            break
        fi
    else
        echo "Invalid entry."
        sleep $DELAY
    fi
done
echo "Program terminated."

```

shell中的循环支持`break和continue`

### until

```
#!/bin/bash
# until-count: display a series of numbers
count=1
until [ $count -gt 5 ]; do
    echo $count
    count=$((count + 1))
done
echo "Finished."

```

## 疑难排解

```
#!/bin/bash
cd $dir_name
rm *

```

可以这样改进：`cd $dir_name &amp;&amp; rm *`，但是有可能未设置变量 dir_name 或其变量值为空，导致删除了用户家目录下面的所有文件。`&amp;&amp; cd $dir_name &amp;&amp; rm *`：

```
if [[ -d $dir_name ]]; then
    if cd $dir_name; then
        rm *
    else
        echo "cannot cd to '$dir_name'" &gt;&amp;2
        exit 1
    fi
else
    echo "no such directory: '$dir_name'" &gt;&amp;2
    exit 1
fi

```

### 测试

早发布，常发布：如果在开发周期的早期发现 bug，那么这些 bug 就越容易定位，而且越能低成本 的修复。比喻上述删除文件的操作非常危险，所以我们可以先这样进行测试，打印出要执行的语句就行：

```
if [[ -d $dir_name ]]; then
    if cd $dir_name; then
        echo rm * # TESTING
    else
        echo "cannot cd to '$dir_name'" &gt;&amp;2
        exit 1
    fi
else
    echo "no such directory: '$dir_name'" &gt;&amp;2
    exit 1
fi
exit # TESTING

```

### 测试案例

通过谨慎地选择输入数据或者运行边缘案例和极端案例来完成测试。比喻上述脚本，我们要测试：
1. dir_name 包含一个已经存在的目录的名字1. dir_name 包含一个不存在的目录的名字1. dir_name 为空
### 调试

一个设计良好的脚本会对查找错误有帮助。设计良好的脚本应该具备防卫能力， 能够监测异常条件，并能为用户提供有用的反馈信息。

### 找到问题区域

隔离脚本中与出现的问题相关的代码区域对查找问题很有帮助。 隔离的代码区域并不总是真正的错误所在，但是隔离往往可以深入了解实际的错误原因。

### 追踪

添加提示信息追踪代码片段。把提示信息输出到标准错误输出，让其从标准输出中分离出来。bash 还提供了一种名为追踪的方法，这种方法可通过 -x 选项和 set 命令加上 -x 选项两种途径实现。

```
#!/bin/bash -x
# trouble: script to demonstrate common errors
number=1
if [ $number = 1 ]; then
    echo "Number is equal to 1."
else
    echo "Number is not equal to 1."
fi

or

#!/bin/bash
# trouble: script to demonstrate common errors
number=1
echo "number=$number" # DEBUG
# 为脚本中的一块选择区域，而不是整个脚本启用追踪
set -x # Turn on tracing
if [ $number = 1 ]; then
    echo "Number is equal to 1."
else
    echo "Number is not equal to 1."
fi
set +x # Turn off tracing

```

行首的加号表明追踪的迹象，使其与常规输出结果区分开来。使用单引号是为了防止变量展开。
