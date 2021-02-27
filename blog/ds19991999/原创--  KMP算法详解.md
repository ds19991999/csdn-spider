# 原创
：  KMP算法详解

# KMP算法详解

> 
要求：对一个串中某个子串进行定位操作，返回匹配到的串的起始位置 <br/> 假设所有串的起始字符索引为1


数据结构定义

```
typedef struct
{
    char *ch;
    int length;
}Str;
```

# 一、简单模式匹配

```
//指向原串的索引i需要回溯，从原串中的每一个字符重新进行匹配，直到匹配成功
int index(Str str,Str substr)
{
    //i,j分别为原串和模式串的索引
    //k记录匹配时上一次的起始位置
    int i=1,j=1,k=i;
    while(i&lt;=str.length&amp;&amp;j&lt;=str.length)
    {
        if(str.ch[i]==substr.ch[j])++i,++j;
        //匹配失败则回溯到上一次开始匹配的位置加1
        else j=1,i=++k; //i的回溯  
    }
    if(j&gt;substr.length) return k;//返回匹配成功索引
    else return 0;//没有匹配到
}
```

# 二、KMP算法

## 1.思路

> 
- 主体思路： <br/> 1）i 不用进行回溯，当原串和模式串不发生匹配时，先找出模式串中的不匹配字符pj，取其模式串的子串F=p1p2p3…pj-1，找出F的前部分FL和后部分FR最先发生相重合的位置，将模式串后移到该位置，即j重新指向的位置是F串中前后重合的子串长度加1； <br/> 2) 我们可以定义一个next[j]数组表示模式串中第j个字符不发生匹配时，应该从next[j]处的字符重新与原串比较。- 特殊情况： <br/> 1）模式串的第一个字符与原串就不匹配，则从原串的下一个位置同模式串进行匹配； <br/> 2）当串F中不存在前后重合的部分，则从原串中不发生匹配的字符同模式串的第一个字符开始比较；- 求next[j]数组例子
<table><thead><th align="center">模式串</th><th align="center">A</th><th align="center">B</th><th align="center">A</th><th align="center">B</th><th align="center">A</th><th align="center">B</th><th align="center">B</th>
</thead><tbody><td align="center">j</td><td align="center">1</td><td align="center">2</td><td align="center">3</td><td align="center">4</td><td align="center">5</td><td align="center">6</td><td align="center">7</td>
<td align="center">next[j]</td><td align="center">0</td><td align="center">1</td><td align="center">1</td><td align="center">2</td><td align="center">3</td><td align="center">4</td><td align="center">5</td>
</tbody></table>


将上述描述转换成简洁的代码描述：

```
//t=next[j]
//这一点是KMP的核心，仔细琢磨
if(pj=pt)next[j+1]=t+1;
else t=next[t];
```

# 2.next[ j ]数组代码实现

```
void getnext(Str substr, int next[])
{
    int i=1,j=0;
    //对next[1]进行初始化,即next[i]=j,这一点也很重要
    next[1]=0;
    while(i&lt;substr.length)
    {
        //模式串匹配
        //如果pi=pj,则，next[i+1]=j+1
        //如果不匹配，则j=next[j];
        if(j==0||substr.ch[i]==substr[j])next[++i]=++j;
        else j=next[j];
    }
}
```

# 3.著名的KMP算法

```
int KMP(Str str, Str substr, int next[])
{
    int i=1,j=1;
    while(i&lt;=str.length&amp;&amp;j&lt;=str.length)
    {
        if(j==0||str.ch[i]==substr.ch[j])++i,++j;
        else j=next[j];
        //没有了i的回溯，这是KMP算法的精髓
        //充分利用了模式串的重复性
        //即使不存在重复字段，在比较时，实现最大的移动量
    }
    if(j&gt;substr.length)return i-substr.length;//返回匹配成功索引
    else return 0;//没有匹配到
}
```

# 三、上述KMP算法的改进

> 
上述KMP算法在一种特殊情况下有些匹配显得有些多余 <br/> 例如下面这个next数组:
<table><thead><th align="center">模式串</th><th align="center">A</th><th align="center">A</th><th align="center">A</th><th align="center">A</th><th align="center">A</th><th align="center">B</th>
</thead><tbody><td align="center">j</td><td align="center">1</td><td align="center">2</td><td align="center">3</td><td align="center">4</td><td align="center">5</td><td align="center">6</td>
<td align="center">next[j]</td><td align="center">0</td><td align="center">1</td><td align="center">2</td><td align="center">3</td><td align="center">4</td><td align="center">5</td>
</tbody></table>
当j = 5时，发生不匹配时，因next[5] = 4，则需将j回溯4进行比较，而next[4]=3，则需将j回溯到3进行比较。。。j需要一次回溯到5、4、3、2、1的位置上，我们可以改进一下next数组，直接跳过位置1~4的回溯，定义改进后的数组为nextval[ j ]。


代码实现步骤：

```
//k=next[j]
//1.当j=1时，和next数组一样，将nextval[1]=0;
//2.当pj=pk时，nextval[j]=nextval[k];
//3.pj!=pk时，nextval[j]=k;
//第二步是算法改进的关键

//这是next数组，放在一起比较
//t=next[j]
//这一点是KMP的核心，仔细琢磨
if(pj=pt)next[j+1]=t+1;
else t=next[t];

//于是可以改进为
//匹配成功
++i;++j;
if(substr.ch[i]!=substr.ch[j])nextval[i]=j;
else nextval[i]=nextval[j];
//匹配失败,直接跳转到nextval[j]
j=nextval[j];
```

nextval数组函数：

```
void getenextval(Str substr, int nextval[])
{
    int i=1,j=0;
    nextval[1]=0;
    while(i&lt;substr.length)
    {
        if(j==0||substr.ch[i]=substr.ch[j])
        {
            ++i;++j;
            if(substr.ch[i]!=substr.ch[j]) nextval[i]=j;
            else nextval[i]=nextval[j];
        }
        else j=nextval[j];
    }
}
```

# 四、最完整的KMP算法实现

```
typedef struct
{
    char *ch;
    int length;
}Str;

void getenextval(Str substr, int nextval[])
{
    int i=1,j=0;
    nextval[1]=0;
    while(i&lt;substr.length)
    {
        if(j==0||substr.ch[i]=substr.ch[j])
        {
            ++i;++j;
            if(substr.ch[i]!=substr.ch[j]) nextval[i]=j;
            else nextval[i]=nextval[j];
        }
        else j=nextval[j];
    }
}

int KMP(Str str, Str substr, int nextval[])
{
    int i=1,j=1;
    while(i&lt;=str.length&amp;&amp;j&lt;=str.length)
    {
        if(j==0||str.ch[i]==substr.ch[j])++i,++j;
        else j=nextval[j];
    }
    if(j&gt;substr.length)return i-substr.length;
    else return 0;
}
```
