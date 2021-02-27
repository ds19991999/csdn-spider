# 原创
：  03-用Jupyter编写数学公式

# 03-用Jupyter编写数学公式

# 用jupyter编写数学公式

# Contents

## 两种数学模式

直接切入正题，毕竟我是在用Jupyter，不是LaTex。。。

```
$P(A \mid B) = \frac{ P(B \mid A) P(A) }{ P(B) }$

```


    
     
      
       
        P
       
       
        (
       
       
        A
       
       
        ∣
       
       
        B
       
       
        )
       
       
        =
       
       
        
         
          P
         
         
          (
         
         
          B
         
         
          ∣
         
         
          A
         
         
          )
         
         
          P
         
         
          (
         
         
          A
         
         
          )
         
        
        
         
          P
         
         
          (
         
         
          B
         
         
          )
         
        
       
      
      
       P(A \mid B) = \frac{ P(B \mid A) P(A) }{ P(B) }
      
     
    P(A∣B)=P(B)P(B∣A)P(A)​

```
贝叶斯公式：$$P(A \mid B) = \frac{ P(B \mid A) P(A) }{ P(B) }$$

```

贝叶斯公式：
     
      
       
        
         P
        
        
         (
        
        
         A
        
        
         ∣
        
        
         B
        
        
         )
        
        
         =
        
        
         
          
           P
          
          
           (
          
          
           B
          
          
           ∣
          
          
           A
          
          
           )
          
          
           P
          
          
           (
          
          
           A
          
          
           )
          
         
         
          
           P
          
          
           (
          
          
           B
          
          
           )
          
         
        
       
       
        P(A \mid B) = \frac{ P(B \mid A) P(A) }{ P(B) }
       
      
     P(A∣B)=P(B)P(B∣A)P(A)​

## 空格

```
$$a\quad\a$$

```

KaTeX parse error: Expected 'EOF', got '\a' at position 7: a\quad\̲a̲

注意这个空格很奇葩，后面非要紧跟字符，否则没有效果，<s>另外，上一篇文章md是自动加空格的，写错了。</s>

在LaTeX中，符号之间的空格会被自动移除，通过 `\`, 或 `\:`或 `\;`添加空格，其空格宽度分别为从小到大。

`$$\intf(x) \; dx$$`


     
      
       
        
         ∫
        
        
         f
        
        
         (
        
        
         x
        
        
         )
        &amp;ThickSpace;
        
         d
        
        
         x
        
       
       
        \int f(x) \; dx
       
      
     ∫f(x)dx

## 上标和下标

`$$x^2$$`


     
      
       
        
         
          x
         
         
          2
         
        
       
       
        x^2
       
      
     x2

`$$e^2x$$`


     
      
       
        
         
          e
         
         
          2
         
        
        
         x
        
       
       
        e^2x
       
      
     e2x

`$$e^{2x}$$`


     
      
       
        
         
          e
         
         
          
           2
          
          
           x
          
         
        
       
       
        e^{2x}
       
      
     e2x<br/> `$$x_i$$`<br/> 
     
      
       
        
         
          x
         
         
          i
         
        
       
       
        x_i
       
      
     xi​<br/> `$$_{10}C_5$$`<br/> 
     
      
       
        
         
         
          10
         
        
        
         
          C
         
         
          5
         
        
       
       
        _{10}C_5
       
      
     10​C5​<br/> `$$\underset{k}{argmax}$$`<br/> 
     
      
       
        
         
          
           a
          
          
           r
          
          
           g
          
          
           m
          
          
           a
          
          
           x
          
         
         
          k
         
        
       
       
        \underset{k}{argmax}
       
      
     kargmax​

## 命令

特定的符号和形式通过命令进行编写，每一个命令以反斜杠开始，一个命令名紧随其后。比如说，创建一个平方根的表达式 `$ \sqrt{2\pi} $$` 显示为


     
      
       
        
         
          
           2
          
          
           π
          
         
        
       
       
         \sqrt{2\pi} 
       
      
     2π
​<br/> `$$\frac{a}{b}$$`<br/> 
     
      
       
        
         
          a
         
         
          b
         
        
       
       
        \frac{a}{b}
       
      
     ba​

## 符号

`$$\alpha, \beta, \gamma$$`<br/> 
     
      
       
        
         α
        
        
         ,
        
        
         β
        
        
         ,
        
        
         γ
        
       
       
        \alpha, \beta, \gamma
       
      
     α,β,γ<br/> `$$\Phi, \Lambda, \Gamma$$`<br/> 
     
      
       
        
         Φ
        
        
         ,
        
        
         Λ
        
        
         ,
        
        
         Γ
        
       
       
        \Phi, \Lambda, \Gamma
       
      
     Φ,Λ,Γ<br/> `$$\times, \pm, \cup, \oplus$$`<br/> 
     
      
       
        
         ×
        
        
         ,
        
        
         ±
        
        
         ,
        
        
         ∪
        
        
         ,
        
        
         ⊕
        
       
       
        \times, \pm, \cup, \oplus
       
      
     ×,±,∪,⊕<br/> `$$\sin, \cosh, \arctan$$`<br/> 
     
      
       
        
         sin
        
        
         ⁡
        
        
         ,
        
        
         cosh
        
        
         ⁡
        
        
         ,
        
        
         arctan
        
        
         ⁡
        
       
       
        \sin, \cosh, \arctan
       
      
     sin,cosh,arctan<br/> `$$\leq, \geq, \approx, \neq$$`<br/> 
     
      
       
        
         ≤
        
        
         ,
        
        
         ≥
        
        
         ,
        
        
         ≈
        
        
         ,
        
        
         ≠
        
       
       
        \leq, \geq, \approx, \neq
       
      
     ≤,≥,≈,̸​=<br/> `$$\cdots, \ldots, \ddots$$`<br/> 
     
      
       
        
         ⋯
        &amp;ThinSpace;
        
         ,
        
        
         …
        
        
         ,
        
        
         ⋱
        
       
       
        \cdots, \ldots, \ddots
       
      
     ⋯,…,⋱<br/> `$$\infty, \nabla, \partial $$`<br/> 
     
      
       
        
         ∞
        
        
         ,
        
        
         ∇
        
        
         ,
        
        
         ∂
        
       
       
        \infty, \nabla, \partial 
       
      
     ∞,∇,∂

## 头标

`$$\hat x$$`<br/> 
     
      
       
        
         
          x
         
         
          ^
         
        
       
       
        \hat x
       
      
     x^<br/> `$$\widehat{abs}$$`<br/> 
     
      
       
        
         
          
           a
          
          
           b
          
          
           s
          
         
         
          ^
         
        
       
       
        \widehat{abs}
       
      
     abs
<br/> `$$\bar x $$`<br/> 
     
      
       
        
         
          x
         
         
          ˉ
         
        
       
       
        \bar x 
       
      
     xˉ<br/> `$$\overline{abs}$$`<br/> 
     
      
       
        
         
          
           a
          
          
           b
          
          
           s
          
         
         
          ‾
         
        
       
       
        \overline{abs}
       
      
     abs<br/> `$$\dot x\quad\ddot x $$`<br/> 
     
      
       
        
         
          x
         
         
          ˙
         
        
        
        
         
          x
         
         
          ¨
         
        
       
       
        \dot x\quad\ddot x 
       
      
     x˙x¨<br/> `$$\vec{x}, \overrightarrow{AB}$$`<br/> 
     
      
       
        
         
          x
         
         
          ⃗
         
        
        
         ,
        
        
         
          
           A
          
          
           B
          
         
         
          →
         
        
       
       
        \vec{x}, \overrightarrow{AB}
       
      
     x
,AB


## 括号

`$$z=(\frac{dx}{dy})^{1/3}$$`<br/> 
     
      
       
        
         z
        
        
         =
        
        
         (
        
        
         
          
           d
          
          
           x
          
         
         
          
           d
          
          
           y
          
         
        
        
         
          )
         
         
          
           1
          
          
           /
          
          
           3
          
         
        
       
       
        z=(\frac{dx}{dy})^{1/3}
       
      
     z=(dydx​)1/3<br/> `$$z=\left(\frac{dx}{dy}\right)^{1/3}$$`<br/> 
     
      
       
        
         z
        
        
         =
        
        
         
          
           (
          
          
           
            
             d
            
            
             x
            
           
           
            
             d
            
            
             y
            
           
          
          
           )
          
         
         
          
           1
          
          
           /
          
          
           3
          
         
        
       
       
        z=\left(\frac{dx}{dy}\right)^{1/3}
       
      
     z=(dydx​)1/3<br/> `$$ {\langle} {\phi} \mid {\psi} {\rangle} $$`<br/> 
     
      
       
        
         ⟨
        
        
         ϕ
        
        
         ∣
        
        
         ψ
        
        
         ⟩
        
       
       
         {\langle} {\phi} \mid {\psi} {\rangle} 
       
      
     ⟨ϕ∣ψ⟩<br/> `$$ {\langle} {\phi} \vert {\psi} {\rangle} $$`<br/> 
     
      
       
        
         ⟨
        
        
         ϕ
        
        
         ∣
        
        
         ψ
        
        
         ⟩
        
       
       
         {\langle} {\phi} \vert {\psi} {\rangle} 
       
      
     ⟨ϕ∣ψ⟩<br/> `$$\left[\begin{matrix}a &amp; b \cr c &amp; d\end{matrix}\right]$$`<br/> 
     
      
       
        
         [
        
        
         
          
           
            
             a
            
           
          
          
           
            
             b
            
           
          
         
         
          
           
            
             c
            
           
          
          
           
            
             d
            
           
          
         
        
        
         ]
        
       
       
        \left[\begin{matrix}a &amp;amp; b \cr c &amp;amp; d\end{matrix}\right]
       
      
     [ac​bd​]<br/> `$$\left\lgroup\begin{matrix}a &amp; b \cr c &amp; d\end{matrix}\right\rgroup$$`<br/> 
     
      
       
        
         ⟮
        
        
         
          
           
            
             a
            
           
          
          
           
            
             b
            
           
          
         
         
          
           
            
             c
            
           
          
          
           
            
             d
            
           
          
         
        
        
         ⟯
        
       
       
        \left\lgroup\begin{matrix}a &amp;amp; b \cr c &amp;amp; d\end{matrix}\right\rgroup
       
      
     ⎩⎪⎪⎧​ac​bd​⎭⎪⎪⎫​

## 字体及其选项

```
<code># 非斜体罗马文本
# 使用 \textrm{abcdefghijklmn123456}
# 或者 \rm{abcdefghijklmn123456}
</code>
```


     
      
       
        
         abcdefghijklmn123456
        
       
       
        \textrm{abcdefghijklmn123456}
       
      
     abcdefghijklmn123456

```
<code># 斜体字母 \mathit{abcdefghijklmn123456} 
</code>
```


     
      
       
        
         a
        
        
         b
        
        
         c
        
        
         d
        
        
         e
        
        
         f
        
        
         g
        
        
         h
        
        
         i
        
        
         j
        
        
         k
        
        
         l
        
        
         m
        
        
         n
        
        
         123456
        
       
       
        \mathit{abcdefghijklmn123456}
       
      
     abcdefghijklmn123456

```
<code># Boldsymbol 字体加粗 \boldsymbol{A\cdot x}=\lambda\cdot v
</code>
```


     
      
       
        
         
          A
         
         
          ⋅
         
         
          x
         
        
        
         =
        
        
         λ
        
        
         ⋅
        
        
         v
        
       
       
        \boldsymbol{A\cdot x}=\lambda\cdot v
       
      
     A⋅x=λ⋅v

## 转义字符’’

## 等式对齐

通过 \ 断开两个或多个等式，可实现等式中部对齐，例如：

```
$$
a_1=b_1+c_1 \\
a_2=b_2+c_2+d_2 \\
a_3=b_3+c_3
$$

```


     
      
       
        
         
          a
         
         
          1
         
        
        
         =
        
        
         
          b
         
         
          1
         
        
        
         +
        
        
         
          c
         
         
          1
         
        
        
        
         
          a
         
         
          2
         
        
        
         =
        
        
         
          b
         
         
          2
         
        
        
         +
        
        
         
          c
         
         
          2
         
        
        
         +
        
        
         
          d
         
         
          2
         
        
        
        
         
          a
         
         
          3
         
        
        
         =
        
        
         
          b
         
         
          3
         
        
        
         +
        
        
         
          c
         
         
          3
         
        
       
       
         a_1=b_1+c_1 \\ a_2=b_2+c_2+d_2 \\ a_3=b_3+c_3 
       
      
     a1​=b1​+c1​a2​=b2​+c2​+d2​a3​=b3​+c3​<br/> 左对齐：

```
$$\begin{aligned}
a_1&amp;=b_1+c_1 \\
a_2&amp;=b_2+c_2+d_2 \\
a_3&amp;=b_3+c_3
\end{aligned}$$

```


     
      
       
        
         
          
           
            
             a
            
            
             1
            
           
          
         
         
          
           
            
            
             =
            
            
             
              b
             
             
              1
             
            
            
             +
            
            
             
              c
             
             
              1
             
            
           
          
         
        
        
         
          
           
            
             a
            
            
             2
            
           
          
         
         
          
           
            
            
             =
            
            
             
              b
             
             
              2
             
            
            
             +
            
            
             
              c
             
             
              2
             
            
            
             +
            
            
             
              d
             
             
              2
             
            
           
          
         
        
        
         
          
           
            
             a
            
            
             3
            
           
          
         
         
          
           
            
            
             =
            
            
             
              b
             
             
              3
             
            
            
             +
            
            
             
              c
             
             
              3
             
            
           
          
         
        
       
       
        \begin{aligned} a_1&amp;amp;=b_1+c_1 \\ a_2&amp;amp;=b_2+c_2+d_2 \\ a_3&amp;amp;=b_3+c_3 \end{aligned}
       
      
     a1​a2​a3​​=b1​+c1​=b2​+c2​+d2​=b3​+c3​​

## 分段函数

```
$$
sign(x)=
\begin{cases}
1,&amp;x&gt;0 \\ 
0,&amp;x=0 \\
-1,&amp;x&lt;0
\end{cases}
$$

```


     
      
       
        
         s
        
        
         i
        
        
         g
        
        
         n
        
        
         (
        
        
         x
        
        
         )
        
        
         =
        
        
         
          {
         
         
          
           
            
             
              
               1
              
              
               ,
              
             
            
           
           
            
             
              
               x
              
              
               &amp;gt;
              
              
               0
              
             
            
           
          
          
           
            
             
              
               0
              
              
               ,
              
             
            
           
           
            
             
              
               x
              
              
               =
              
              
               0
              
             
            
           
          
          
           
            
             
              
               −
              
              
               1
              
              
               ,
              
             
            
           
           
            
             
              
               x
              
              
               &amp;lt;
              
              
               0
              
             
            
           
          
         
        
       
       
         sign(x)= \begin{cases} 1,&amp;amp;x&amp;gt;0 \\ 0,&amp;amp;x=0 \\ -1,&amp;amp;x&amp;lt;0 \end{cases} 
       
      
     sign(x)=⎩⎪⎨⎪⎧​1,0,−1,​x&gt;0x=0x&lt;0​

`\\ 等价于 \cr，表示换行到新的 case。`

## 一点总结

`$$\sqrt[3]{a}$$`<br/> 
     
      
       
        
         
          a
         
         
          3
         
        
       
       
        \sqrt[3]{a}
       
      
     3a
​<br/> `$$\overline{m+n}$$`<br/> 
     
      
       
        
         
          
           m
          
          
           +
          
          
           n
          
         
         
          ‾
         
        
       
       
        \overline{m+n}
       
      
     m+n​<br/> `$$\underline {m+n}$$`<br/> 
     
      
       
        
         
          
           m
          
          
           +
          
          
           n
          
         
         
          ‾
         
        
       
       
        \underline {m+n}
       
      
     m+n​

不知道为啥这个下划线需要加空格，否则报错。。。关于md和LaTex对于空格方面都是忽略，不同的是md会保留一个空格。

所以以后书写数学公式关键命令及语法前面还是要加空格，正如md标准语法中，每一种格式的结束都需要空一行，表示此语法格式结束，虽然有些md编辑器会容下这些细小的错误，但为保证统一，我们还是使用标准格式比较好。<br/> `$$\underbrace{a+b+\cdots+j}_{10}$$`<br/> 
     
      
       
        
         
          
           
            a
           
           
            +
           
           
            b
           
           
            +
           
           
            ⋯
           
           
            +
           
           
            j
           
          
          
           ⎵
          
         
         
          10
         
        
       
       
        \underbrace{a+b+\cdots+j}_{10}
       
      
     10


a+b+⋯+j​​<br/> `$$\overbrace{a+b+\cdots+j}^{10}$$`<br/> 
     
      
       
        
         
          
           
            a
           
           
            +
           
           
            b
           
           
            +
           
           
            ⋯
           
           
            +
           
           
            j
           
          
          
           ⏞
          
         
         
          10
         
        
       
       
        \overbrace{a+b+\cdots+j}^{10}
       
      
     a+b+⋯+j


​10​<br/> `$$\vec{AB}$$`<br/> 
     
      
       
        
         
          
           A
          
          
           B
          
         
         
          ⃗
         
        
       
       
        \vec{AB}
       
      
     AB
<br/> `$$\overrightarrow{AB}$$`<br/> 
     
      
       
        
         
          
           A
          
          
           B
          
         
         
          →
         
        
       
       
        \overrightarrow{AB}
       
      
     AB
<br/> `$$\overleftarrow {AB}$$`<br/> 
     
      
       
        
         
          
           A
          
          
           B
          
         
         
          ←
         
        
       
       
        \overleftarrow {AB}
       
      
     AB
<br/> `$$\frac{-b\pm\sqrt{b^2-4ac}}{2a}$$`<br/> 
     
      
       
        
         
          
           −
          
          
           b
          
          
           ±
          
          
           
            
             
              b
             
             
              2
             
            
            
             −
            
            
             4
            
            
             a
            
            
             c
            
           
          
         
         
          
           2
          
          
           a
          
         
        
       
       
        \frac{-b\pm\sqrt{b^2-4ac}}{2a}
       
      
     2a−b±b2−4ac
​​<br/> `$$\int_{0}^{\pi}{\tan x}$$`<br/> 
     
      
       
        
         
          ∫
         
         
          0
         
         
          π
         
        
        
         
          tan
         
         
          ⁡
         
         
          x
         
        
       
       
        \int_{0}^{\pi}{\tan x}
       
      
     ∫0π​tanx<br/> `$$\sum_{i=0}^{n}{i}$$`<br/> 
     
      
       
        
         
          ∑
         
         
          
           i
          
          
           =
          
          
           0
          
         
         
          n
         
        
        
         i
        
       
       
        \sum_{i=0}^{n}{i}
       
      
     i=0∑n​i<br/> `$$\prod_{i=1}^{9}{i}$$`<br/> 
     
      
       
        
         
          ∏
         
         
          
           i
          
          
           =
          
          
           1
          
         
         
          9
         
        
        
         i
        
       
       
        \prod_{i=1}^{9}{i}
       
      
     i=1∏9​i

## 附录1：数学符号表

> 
要经常查看


## 附录2：参考书籍
