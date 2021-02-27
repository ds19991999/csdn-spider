# 原创
：  Shell流程控制：case 分支

# Shell流程控制：case 分支

## 流程控制：case 分支

### case

```
case word in
    [pattern [| pattern]...) commands ;;]...
esac

```

```
#!/bin/bash
# case-menu: a menu driven system information program
clear
echo "
Please Select:
1. Display System Information
2. Display Disk Space
3. Display Home Space Utilization
0. Quit
"
read -p "Enter selection [0-3] &gt; "
case $REPLY in
    0)  echo "Program terminated."
        exit
        ;;
    1)  echo "Hostname: $HOSTNAME"
        uptime
        ;;
    2)  df -h
        ;;
    3)  if [[ $(id -u) -eq 0 ]]; then
            echo "Home Space Utilization (All Users)"
            du -sh /home/*
        else
            echo "Home Space Utilization ($USER)"
            du -sh $HOME
        fi
        ;;
    *)  echo "Invalid entry" &gt;&amp;2
        exit 1
        ;;
esac

```

### 模式

case 语句使用的模式和路径展开中使用的那些是一样的。模式以一个 “)” 为终止符。这里是一些有效的模式。

|模式|描述
|------
|a)|若单词为 “a”，则匹配
|[[:alpha:]])|若单词是一个字母字符，则匹配
|???)|若单词只有3个字符，则匹配
|*.txt)|若单词以 “.txt” 字符结尾，则匹配
|*)|匹配任意单词。把这个模式做为 case 命令的最后一个模式，是一个很好的做法， 可以捕捉到任意一个与先前模式不匹配的数值；也就是说，捕捉到任何可能的无效值。

```
#!/bin/bash
read -p "enter word &gt; "
case $REPLY in
    [[:alpha:]])        echo "is a single alphabetic character." ;;
    [ABC][0-9])         echo "is A, B, or C followed by a digit." ;;
    ???)                echo "is three characters long." ;;
    *.txt)              echo "is a word ending in '.txt'" ;;
    *)                  echo "is something else." ;;
esac

```

还可以使用竖线字符作为分隔符，把多个模式结合起来。这就创建了一个 “或” 条件模式。这对于处理诸如大小写字符很有用处。例如：

```
#!/bin/bash
# case-menu: a menu driven system information program
clear
echo "
Please Select:
A. Display System Information
B. Display Disk Space
C. Display Home Space Utilization
Q. Quit
"
read -p "Enter selection [A, B, C or Q] &gt; "
case $REPLY in
q|Q) echo "Program terminated."
     exit
     ;;
a|A) echo "Hostname: $HOSTNAME"
     uptime
     ;;
b|B) df -h
     ;;
c|C) if [[ $(id -u) -eq 0 ]]; then
         echo "Home Space Utilization (All Users)"
         du -sh /home/*
     else
         echo "Home Space Utilization ($USER)"
         du -sh $HOME
     fi
     ;;
*)   echo "Invalid entry" &gt;&amp;2
     exit 1
     ;;
esac

```

添加的 “;;&amp;” 的语法允许 case 语句继续执行下一条测试，而不是简单地终止运行。

```

#!/bin/bash
# case4-2: test a character
read -n 1 -p "Type a character &gt; "
echo
case $REPLY in
    [[:upper:]])    echo "'$REPLY' is upper case." ;;&amp;
    [[:lower:]])    echo "'$REPLY' is lower case." ;;&amp;
    [[:alpha:]])    echo "'$REPLY' is alphabetic." ;;&amp;
    [[:digit:]])    echo "'$REPLY' is a digit." ;;&amp;
    [[:graph:]])    echo "'$REPLY' is a visible character." ;;&amp;
    [[:punct:]])    echo "'$REPLY' is a punctuation symbol." ;;&amp;
    [[:space:]])    echo "'$REPLY' is a whitespace character." ;;&amp;
    [[:xdigit:]])   echo "'$REPLY' is a hexadecimal digit." ;;&amp;
esac

```

## 位置参数

### 访问命令行

shell 提供了一个称为位置参数的变量集合，这个集合包含了命令行中所有独立的单词。这些变量按照从0到9给予命名。

```
#!/bin/bash
# posit-param: script to view command line parameters
echo "
\$0 = $0
\$1 = $1
\$2 = $2
\$3 = $3
\$4 = $4
\$5 = $5
\$6 = $6
\$7 = $7
\$8 = $8
\$9 = $9
"

```

```
[me@linuxbox ~]$ posit-param a b c d
$0 = /home/me/bin/posit-param
$1 = a
$2 = b
$3 = c
$4 = d
$5 =
$6 =
$7 =
$8 =
$9 =

```

### shift - 访问多个参数的利器

执行一次 shift 命令， 就会导致所有的位置参数 “向下移动一个位置”。

```
#!/bin/bash
# posit-param2: script to display all arguments
# 只要参数个数不为零就会继续执行的 while 循环
count=1
while [[ $# -gt 0 ]]; do
    echo "Argument $count = $1"
    count=$((count + 1))
    shift
done

```

```
[me@linuxbox ~]$ posit-param2 a b c d
Argument 1 = a
Argument 2 = b
Argument 3 = c
Argument 4 = d

```

### 处理集体位置参数

shell 提供了两种特殊的参数，他们二者都能扩展成完整的位置参数列表，但以相当微妙的方式略有不同。

|参数|描述
|------
|$*|展开成一个从1开始的位置参数列表。当它被用双引号引起来的时候，展开成一个由双引号引起来 的字符串，包含了所有的位置参数，每个位置参数由 shell 变量 IFS 的第一个字符（默认为一个空格）分隔开。
|$@|展开成一个从1开始的位置参数列表。当它被用双引号引起来的时候， 它把每一个位置参数展开成一个由双引号引起来的分开的字符串。

```
#!/bin/bash
# posit-params3 : script to demonstrate $* and $@
print_params () {
    echo "\$1 = $1"
    echo "\$2 = $2"
    echo "\$3 = $3"
    echo "\$4 = $4"
}
pass_params () {
    echo -e "\n" '$* :';      print_params   $*
    echo -e "\n" '"$*" :';    print_params   "$*"
    echo -e "\n" '$@ :';      print_params   $@
    echo -e "\n" '"$@" :';    print_params   "$@"
}
pass_params "word" "words with spaces"

```

```
[me@linuxbox ~]$ posit-param3
 $* :
$1 = word
$2 = words
$3 = with
$4 = spaces
 "$*" :
$1 = word words with spaces
$2 =
$3 =
$4 =
 $@ :
$1 = word
$2 = words
$3 = with
$4 = spaces
 "$@" :
$1 = word
$2 = words with spaces
$3 =
$4 =

```

### 一个更复杂的应用

```
#!/bin/bash
# sys_info_page: program to output a system information page
PROGNAME=$(basename $0)
TITLE="System Information Report For $HOSTNAME"
CURRENT_TIME=$(date +"%x %r %Z")
TIMESTAMP="Generated $CURRENT_TIME, by $USER"
report_uptime () {
    cat &lt;&lt;- _EOF_
        &lt;H2&gt;System Uptime&lt;/H2&gt;
        &lt;PRE&gt;$(uptime)&lt;/PRE&gt;
    _EOF_
    return
}
report_disk_space () {
    cat &lt;&lt;- _EOF_
        &lt;H2&gt;Disk Space Utilization&lt;/H2&gt;
        &lt;PRE&gt;$(df -h)&lt;/PRE&gt;
    _EOF_
    return
}
report_home_space () {
    if [[ $(id -u) -eq 0 ]]; then
        cat &lt;&lt;- _EOF_
            &lt;H2&gt;Home Space Utilization (All Users)&lt;/H2&gt;
            &lt;PRE&gt;$(du -sh /home/*)&lt;/PRE&gt;
        _EOF_
    else
        cat &lt;&lt;- _EOF_
            &lt;H2&gt;Home Space Utilization ($USER)&lt;/H2&gt;
            &lt;PRE&gt;$(du -sh $HOME)&lt;/PRE&gt;
        _EOF_
    fi
    return
}
usage () {
    echo "$PROGNAME: usage: $PROGNAME [-f file | -i]"
    return
}
write_html_page () {
    cat &lt;&lt;- _EOF_
        &lt;HTML&gt;
            &lt;HEAD&gt;
                &lt;TITLE&gt;$TITLE&lt;/TITLE&gt;
            &lt;/HEAD&gt;
            &lt;BODY&gt;
                &lt;H1&gt;$TITLE&lt;/H1&gt;
                &lt;P&gt;$TIMESTAMP&lt;/P&gt;
                $(report_uptime)
                $(report_disk_space)
                $(report_home_space)
            &lt;/BODY&gt;
        &lt;/HTML&gt;
    _EOF_
    return
}
# process command line options
interactive=
filename=
while [[ -n $1 ]]; do
    case $1 in
        -f | --file)          shift
                              filename=$1
                              ;;
        -i | --interactive)   interactive=1
                              ;;
        -h | --help)          usage
                              exit
                              ;;
        *)                    usage &gt;&amp;2
                              exit 1
                              ;;
    esac
    shift
done
# interactive mode
if [[ -n $interactive ]]; then
    while true; do
        read -p "Enter name of output file: " filename
        if [[ -e $filename ]]; then
            read -p "'$filename' exists. Overwrite? [y/n/q] &gt; "
            case $REPLY in
                Y|y)    break
                        ;;
                Q|q)    echo "Program terminated."
                        exit
                        ;;
                *)      continue
                        ;;
            esac
        fi
    done
fi
# output html page
if [[ -n $filename ]]; then
    if touch $filename &amp;&amp; [[ -f $filename ]]; then
        write_html_page &gt; $filename
    else
        echo "$PROGNAME: Cannot write file '$filename'" &gt;&amp;2
        exit 1
    fi
else
    write_html_page
fi

```
