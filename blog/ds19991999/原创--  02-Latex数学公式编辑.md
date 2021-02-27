# 原创
：  02-Latex数学公式编辑

# 02-Latex数学公式编辑

# 数学公式编辑

> 
对于Python程序员，需要一些数学公式的编辑，所以对于LaTex的学习只需要掌握数学公式的编辑已经足够，关于文档编排感兴趣可以深究，但感觉没必要.


# Contents

## 数学模式

```
<code># `$ ... $` 可以插入行内公式
# `\[ ... \]` 可以插入行间公式
# 对行间公式编号：`equation环境`
</code>
```

```
\begin{equation}
...
\end{equation}

```


     
      
       
        
         .
        
        
         .
        
        
         .
        
       
       
        ...
       
      
     ...

编号已经自动显示出来了，不过一般这个环境可以不使用，后面会介绍.

## 上下标`^` `_`

```
\[ x_1+x_2=-b/a. \]
\begin{equation}
E=mc^2.
\end{equation}

```


     
      
       
        
         
          x
         
         
          1
         
        
        
         +
        
        
         
          x
         
         
          2
         
        
        
         =
        
        
         −
        
        
         b
        
        
         /
        
        
         a
        
        
         .
        
       
       
        x_1+x_2=-b/a.
       
      
     x1​+x2​=−b/a.<br/> 
     
      
       
        
         E
        
        
         =
        
        
         m
        
        
         
          c
         
         
          2
         
        
        
         .
        
       
       
        E=mc^2.
       
      
     E=mc2.

貌似这个equation环境是全局的…好吧，markdown已经帮我们实现了一切，我们只需要会用就行.

**它默认只作用于之后的一个字符，如果想对连续的几个字符起作用，请将这些字符用花括号 {} 括起来，例如：**

```
\[ z = r\cdot e^{2\pi i}. \]

```


     
      
       
        
         z
        
        
         =
        
        
         r
        
        
         ⋅
        
        
         
          e
         
         
          
           2
          
          
           π
          
          
           i
          
         
        
        
         .
        
       
       
         z = r\cdot e^{2\pi i}. 
       
      
     z=r⋅e2πi.

## 根式与分式

根式用 `\sqrt{·}` 来表示，分式用`\frac{·}{·}` 来表示（第一个参数为分子，第二个为分母）

```
$\sqrt{x}$, $\frac{1}{2}$.
\[ \sqrt{x}, \]
\[ \frac{1}{2}. \]

```


    
     
      
       
        
         x
        
       
      
      
       \sqrt{x}
      
     
    x
​, 
    
     
      
       
        
         1
        
        
         2
        
       
      
      
       \frac{1}{2}
      
     
    21​.<br/> 
     
      
       
        
         
          x
         
        
        
         ,
        
       
       
         \sqrt{x}, 
       
      
     x
​,<br/> 
     
      
       
        
         
          1
         
         
          2
         
        
        
         .
        
       
       
        \frac{1}{2}. 
       
      
     21​.

## 运算符

```
\[ \pm\; \times \; \div\; \cdot\; \cap\; \cup\;
\geq\; \leq\; \neq\; \approx \; \equiv \]

```


     
      
       
        
         ±
        
        
         ,
        
        
         ×
        
        
         ,
        
        
         ÷
        
        
         ,
        
        
         ⋅
        
        
         ,
        
        
         ∩
        
        
         ,
        
        
         ∪
        
        
         ,
        
        
         ≥
        
        
         ,
        
        
         ≤
        
        
         ,
        
        
         ≠
        
        
         ,
        
        
         ≈
        
        
         ,
        
        
         ≡
        
       
       
        \pm, \times, \div, \cdot, \cap, \cup,\geq, \leq, \neq, \approx, \equiv 
       
      
     ±,×,÷,⋅,∩,∪,≥,≤,̸​=,≈,≡

```
\[\sum, \quad, \prod, \lim, \int \]

```


     
      
       
        
         ∑
        
        
         ,
        
        
        
         ,
        
        
         ∏
        
        
         ,
        
        
         lim
        
        
         ⁡
        
        
         ,
        
        
         ∫
        
       
       
        \sum, \quad, \prod, \lim, \int 
       
      
     ∑,,∏,lim,∫

```
$ \sum_{i=1}^n i\quad\prod_{i=1}^n $  和  $ \sum\limits _{i=1}^n i\quad\prod\limits _{i=1}^n $
\[ \lim_{x\to0}x^2\int_a^b x^2 dx \]
\[ \lim\nolimits _{x\to0}x^2\int\nolimits_a^b x^2 dx \]

```

$ \sum_{i=1}^n i\quad\prod_{i=1}^n $ 和 $ \sum\limits _{i=1}^n i\quad\prod\limits _{i=1}^n $<br/> 
     
      
       
        
         
          lim
         
         
          ⁡
         
         
          
           x
          
          
           →
          
          
           0
          
         
        
        
         
          x
         
         
          2
         
        
        
         
          ∫
         
         
          a
         
         
          b
         
        
        
         
          x
         
         
          2
         
        
        
         d
        
        
         x
        
       
       
         \lim_{x\to0}x^2\int_a^b x^2 dx 
       
      
     x→0lim​x2∫ab​x2dx<br/> 
     
      
       
        
         
          lim
         
         
          ⁡
         
         
          
           x
          
          
           →
          
          
           0
          
         
        
        
         
          x
         
         
          2
         
        
        
         
          ∫
         
         
          a
         
         
          b
         
        
        
         
          x
         
         
          2
         
        
        
         d
        
        
         x
        
       
       
         \lim\nolimits _{x\to0}x^2\int\nolimits_a^b x^2 dx 
       
      
     limx→0​x2∫ab​x2dx

[ \iint\quad\iiint\quad\iiiint\quad\idotsint ]

KaTeX parse error: Expected 'EOF', got '\iiiint' at position 23: …quad\iiint\quad\̲i̲i̲i̲i̲n̲t̲\quad\idotsint 

~~这里又发现markdown已经帮我们把空格加上去了.~~好吧，是我搞错了。。。

## 定界符括号等

```
(x)  \[ \Biggl(\biggl(\Bigl(\bigl((x)\bigr)\Bigr)\biggr)\Biggr) \]
[x] \[ \Biggl[\biggl[\Bigl[\bigl[[x]\bigr]\Bigr]\biggr]\Biggr] \]
{x} \[ \Biggl \{\biggl \{\Bigl \{\bigl \{\{x\}\bigr \}\Bigr \}\biggr \}\Biggr\} \]
&lt;x\&gt; \[ \Biggl\langle\biggl\langle\Bigl\langle\bigl\langle\langle x
    \rangle\bigr\rangle\Bigr\rangle\biggr\rangle\Biggr\rangle \]
[x] \[ \Biggl\lvert\biggl\lvert\Bigl\lvert\bigl\lvert\lvert x
\rvert\bigr\rvert\Bigr\rvert\biggr\rvert\Biggr\rvert \]
||x||\[ \Biggl\lVert\biggl\lVert\Bigl\lVert\bigl\lVert\lVert x
\rVert\bigr\rVert\Bigr\rVert\biggr\rVert\Biggr\rVert \]

```

(x) 
     
      
       
        
         (
        
        
         (
        
        
         (
        
        
         (
        
        
         (
        
        
         x
        
        
         )
        
        
         )
        
        
         )
        
        
         )
        
        
         )
        
       
       
        \Biggl(\biggl(\Bigl(\bigl((x)\bigr)\Bigr)\biggr)\Biggr)
       
      
     (((((x)))))<br/> [x] 
     
      
       
        
         [
        
        
         [
        
        
         [
        
        
         [
        
        
         [
        
        
         x
        
        
         ]
        
        
         ]
        
        
         ]
        
        
         ]
        
        
         ]
        
       
       
        \Biggl[\biggl[\Bigl[\bigl[[x]\bigr]\Bigr]\biggr]\Biggr]
       
      
     [[[[[x]]]]]<br/> {x} 
     
      
       
        
         {
        
        
         {
        
        
         {
        
        
         {
        
        
         {
        
        
         x
        
        
         }
        
        
         }
        
        
         }
        
        
         }
        
        
         }
        
       
       
        \Biggl \{\biggl \{\Bigl \{\bigl \{\{x\}\bigr \}\Bigr \}\biggr \}\Biggr\}
       
      
     {{{{{x}}}}}<br/> &lt;x&gt; 
     
      
       
        
         ⟨
        
        
         ⟨
        
        
         ⟨
        
        
         ⟨
        
        
         ⟨
        
        
         x
        
        
         ⟩
        
        
         ⟩
        
        
         ⟩
        
        
         ⟩
        
        
         ⟩
        
       
       
         \Biggl\langle\biggl\langle\Bigl\langle\bigl\langle\langle x \rangle\bigr\rangle\Bigr\rangle\biggr\rangle\Biggr\rangle 
       
      
     ⟨⟨⟨⟨⟨x⟩⟩⟩⟩⟩<br/> |x| 
     
      
       
        
         ∣
        
        
         ∣
        
        
         ∣
        
        
         ∣
        
        
         ∣
        
        
         x
        
        
         ∣
        
        
         ∣
        
        
         ∣
        
        
         ∣
        
        
         ∣
        
       
       
        \Biggl\lvert\biggl\lvert\Bigl\lvert\bigl\lvert\lvert x \rvert\bigr\rvert\Bigr\rvert\biggr\rvert\Biggr\rvert 
       
      
     ∣∣∣∣∣​∣∣∣∣​∣∣∣​∣∣​∣x∣∣∣​∣∣∣​∣∣∣∣​∣∣∣∣∣​<br/> ||x||
     
      
       
        
         ∥
        
        
         ∥
        
        
         ∥
        
        
         ∥
        
        
         ∥
        
        
         x
        
        
         ∥
        
        
         ∥
        
        
         ∥
        
        
         ∥
        
        
         ∥
        
       
       
         \Biggl\lVert\biggl\lVert\Bigl\lVert\bigl\lVert\lVert x \rVert\bigr\rVert\Bigr\rVert\biggr\rVert\Biggr\rVert 
       
      
     ∥∥∥∥∥​∥∥∥∥​∥∥∥​∥∥​∥x∥∥∥​∥∥∥​∥∥∥∥​∥∥∥∥∥​

## 省略号

```
\[ x_1,x_2,\dots ,x_n\quad1,2,\cdots ,n\quad\vdots\quad\ddots \]

```


     
      
       
        
         
          x
         
         
          1
         
        
        
         ,
        
        
         
          x
         
         
          2
         
        
        
         ,
        
        
         …
        
        
         ,
        
        
         
          x
         
         
          n
         
        
        
        
         1
        
        
         ,
        
        
         2
        
        
         ,
        
        
         ⋯
        &amp;ThinSpace;
        
         ,
        
        
         n
        
        
        
         ⋮
        
        
        
        
         ⋱
        
       
       
        x_1,x_2,\dots ,x_n\quad1,2,\cdots ,n\quad\vdots\quad\ddots 
       
      
     x1​,x2​,…,xn​1,2,⋯,n⋮⋱

## 矩阵

```
\[ \begin{pmatrix} a&amp;b\\c&amp;d \end{pmatrix} \quad 
\begin{bmatrix} a&amp;b\\c&amp;d \end{bmatrix} \quad 
\begin{Bmatrix} a&amp;b\\c&amp;d \end{Bmatrix} \quad 
\begin{vmatrix} a&amp;b\\c&amp;d \end{vmatrix} \quad 
\begin{Vmatrix} a&amp;b\\c&amp;d \end{Vmatrix} \]

```


     
      
       
        
         
          (
         
         
          
           
            
             
              a
             
            
           
           
            
             
              b
             
            
           
          
          
           
            
             
              c
             
            
           
           
            
             
              d
             
            
           
          
         
         
          )
         
        
        
       
       
         \begin{pmatrix} a&amp;amp;b\\c&amp;amp;d \end{pmatrix} \quad 
       
      
     (ac​bd​)<br/> 
     
      
       
        
         
          [
         
         
          
           
            
             
              a
             
            
           
           
            
             
              b
             
            
           
          
          
           
            
             
              c
             
            
           
           
            
             
              d
             
            
           
          
         
         
          ]
         
        
        
       
       
         \begin{bmatrix} a&amp;amp;b\\c&amp;amp;d \end{bmatrix} \quad 
       
      
     [ac​bd​]<br/> 
     
      
       
        
         
          {
         
         
          
           
            
             
              a
             
            
           
           
            
             
              b
             
            
           
          
          
           
            
             
              c
             
            
           
           
            
             
              d
             
            
           
          
         
         
          }
         
        
        
       
       
         \begin{Bmatrix} a&amp;amp;b\\c&amp;amp;d \end{Bmatrix} \quad 
       
      
     {ac​bd​}<br/> 
     
      
       
        
         
          ∣
         
         
          
           
            
             
              a
             
            
           
           
            
             
              b
             
            
           
          
          
           
            
             
              c
             
            
           
           
            
             
              d
             
            
           
          
         
         
          ∣
         
        
        
       
       
         \begin{vmatrix} a&amp;amp;b\\c&amp;amp;d \end{vmatrix} \quad 
       
      
     ∣∣∣∣​ac​bd​∣∣∣∣​<br/> 
     
      
       
        
         ∥
        
        
         
          
           
            
             a
            
           
          
          
           
            
             b
            
           
          
         
         
          
           
            
             c
            
           
          
          
           
            
             d
            
           
          
         
        
        
         ∥
        
       
       
         \begin{Vmatrix} a&amp;amp;b\\c&amp;amp;d \end{Vmatrix} 
       
      
     ∥∥∥∥​ac​bd​∥∥∥∥​

使用 smallmatrix 环境，可以生成行内公式的小矩阵。

```
Marry has a little matrix $ ( \begin{smallmatrix} a&amp;b\\c&amp;d \end{smallmatrix} ) $.

Marry has a little matrix $ | \begin{smallmatrix} a&amp;b\\c&amp;d \end{smallmatrix} | $.

```

Marry has a little matrix $ ( \begin{smallmatrix} a&amp;b\c&amp;d \end{smallmatrix} ) $.

Marry has a little matrix $ | \begin{smallmatrix} a&amp;b\c&amp;d \end{smallmatrix} | $.

## 多行公式

有的公式特别长，我们需要手动为他们换行；有几个公式是一组，我们需要将他们放在一起；还有些类似分段函数，我们需要给它加上一个左边的花括号。

### 长公式

不对齐：

```
\begin{multline}
x = a+b+c+{} \\
d+e+f+g
\end{multline}

```

如果不需要编号，可以使用 multline* 环境代替。

对齐：

```
\[\begin{aligned}
x ={}&amp; a+b+c+{} \\
&amp;d+e+f+g
\end{aligned}\]

```

一行显示居中对齐：

```
\[\begin{aligned}
x =a+b+c+
d+e+f+g
\end{aligned}\]

```

一行显示居中对齐：<br/> 
     
      
       
        
         x
        
        
         =
        
        
         a
        
        
         +
        
        
         b
        
        
         +
        
        
         c
        
        
         +
        
        
         d
        
        
         +
        
        
         e
        
        
         +
        
        
         f
        
        
         +
        
        
         g
        
       
       
         x =a+b+c+d+e+f+g 
       
      
     x=a+b+c+d+e+f+g

### 公式组

无需对齐的公式组可以使用 gather 环境，需要对齐的公式组可以使用 align 环境。他们都带有编号，如果不需要编号可以使用带`*`的版本。

```
\begin{gather}
a = b+c+d \\
x = y+z
\end{gather}

\begin{align}
a &amp;= b+c+d \\
x &amp;= y+z
\end{align}

```

### 分段函数

分段函数可以用cases次环境来实现，它必须包含在数学环境之内。

```
\[ y= \begin{cases}
-x,\quad x\leq 0 \\
x,\quad x&gt;0
\end{cases} \]

```

这里，LaTex和md的空格都不起作用了…

## 插入图片和表格

这里由于md本身已经支持了图片和和表格，所以关于LaTex本身的图片和表格就无须了解，要知道md支持LaTex数学公式，这个文档就是纯md写的.

看一下图片显示。。。

```
\begin{figure}[htbp]
\centering
\includegraphics{a.jpg}
\caption{有图有真相}
\label{fig:myphoto}
\end{figure}

```

“htbp” 选项用来指定插图的理想位置，这几个字母分别代表here, top, bottom, float page，也就是就这里、页顶、页尾、浮动页(专门放浮动体的单独页面) 。\centering 用来使插图居中；\caption 命令设置插图标题，LaTeX 会自动给浮动体的标题加上编号。注意 \label 应该放在标题命令之后。

## 一点背景

### TeX - LaTeX

TeX 是高德纳（Donald Ervin Knuth，1938年1月10日 –）教授愤世嫉俗（大雾；追求完美）做出来的排版引擎，同时也是该引擎使用的标记语言（Markup Lang）的名称。这里所谓的引擎，是指能够实现断行、分页等操作的程序（请注意这并不是定义）；这里的标记语言，是指一种将控制命令和文本结合起来的格式，它的主体是其中的文本而控制命令则实现一些特殊效果（同样请注意这并不是定义）。

而 LaTeX 则是 L. Lamport （1941年2月7日 – ） 教授开发的基于 TeX 的排版系统。实际上 LaTeX 利用 TeX 的控制命令，定义了许多新的控制命令并封装成一个可执行文件。这个可执行文件会去解释 LaTeX 新定义的命令成为 TeX 的控制命令，并最终交由 TeX 引擎进行排版。

所以：

### pdfTeX - pdfLaTeX

pdfTeX 直接输出 pdf 格式文档，而 TeX 引擎则输出 dvi 格式的文档。

pdfLaTeX 这个程序的主要工作依旧是将 LaTeX 格式的文档进行解释，不过此次是将解释之后的结果交付给 pdfTeX 引擎处理。

更多LaTex知识请看[LaTeX 入门文档](https://liam0205.me/2014/09/08/latex-introduction/)。

### 总结

TeX - pdfTeX - XeTeX - LuaTeX 都是排版引擎，按照先进程度递增（LuaTeX 尚未完善）。

LaTeX 是一种格式，基于 TeX 格式定义了很多更方便使用的控制命令。上述四个引擎都有对应的程序将 LaTeX 格式解释成引擎能处理的内容。

CTeX, MiKTeX, TeX Live 都是 TeX 的发行，他们是许许多多东西的集合。
