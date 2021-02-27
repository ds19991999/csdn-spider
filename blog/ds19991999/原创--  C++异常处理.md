# 原创
：  C++异常处理

# C++异常处理

# 一、C++语言异常处理的实现

## 1.三个保留字

```
//try:可能发生异常的程序代码
//throw:抛出异常
//catch:捕获异常，进行异常处理

try
{
    //try语句块
}
catch(异常类型1 参数1)
{
    //针对类型1的异常处理
}
//throw语句在try语句块内

//当异常发生，系统找不到与该错误类型相匹配的错误处理模块，则函数
//terminate()将被自动调用，默认功能是调用abort()终止程序执行
//错误处理函数set_terminate()函数来指定
# include &lt;iosteam&gt;
using namesapce
void aa()
{
    cout&lt;&lt;"这是由用户指定的错误处理函数"&lt;&lt;endl;
    exit(-1);
}
void main()
{
    set_terminate(aa);//aa代替默认的abort()函数
    try
    {
        throw"error";
    }
    catch(int){}
}
```

## 2.实例

```
//test1
# include &lt;iosteam&gt;
double divide(duoble,double);
void main()
{
    double f1 = 0.0, f2 = 0.0;
    try
    {
        cout&lt;&lt;"f1/f2="&lt;&lt;divide(f1,f2)&lt;&lt;"\n";
    }
    catch(double)
    {
        cout&lt;&lt;"被0除"&lt;&lt;"\n";
    }
}
double divide(double x, double y)
{
    if(y==0)throw 0.0;//抛出异常
    return x/y;
}

//test2
# include &lt;iosteam&gt;
using namespace std;
void detail(int k);
{
    cout&lt;&lt;"Start of detail function.\n";
    if(k==0) throw 123;
    cout&lt;&lt;"End of detail function.\n"
}
void compute(int i)
{
    cout&lt;&lt;"Start of compute function.\n";
    detail(i);
    cout&lt;&lt;"End of compute function.\n";
}
int main()
{
    int x;
    cout&lt;&lt;"Enter x(0 will throw an exception):";
    cin&gt;&gt;x;
    try
    {
        compute(x);
    }
    catch(int i)
    {
        cout&lt;&lt;"Exception:"&lt;&lt;i&lt;&lt;endl;
    }
    cout&lt;&lt;"The end.\n";
    return 0;
}

//test3
# include&lt;iosteam&gt;
using namespace std;
void main()
{
    int i;
    char ch;
    cout&lt;&lt;"请输入一个整数和一个字符\n";
    //如果输入为0！则只会抛出0异常，不会抛出！异常
    try
    {
        cin&gt;&gt;i&gt;&gt;ch;
        if(i==0)throw 0;
        if(ch=='!')throw '!';
    }
    catch(int)
    {
        cout&lt;&lt;"输入为0\n";
    }
    catch(char)
    {
        cout&lt;&lt;"输入字符！"&lt;&lt;endl;
    }
    cout&lt;&lt;"程序结束"&lt;&lt;endl;
}

//test4
# include &lt;iosteam&gt;
using namespace std;
class OutOfBounds
{
public:
    OutOfBounds(int a)
    {
        i=a;
    }
    int indexValue()
    {
        return i;
    }
private:
    int i;
};

class Array
{
public:
    int &amp;operator[](int i)
    {
        if(i&lt;0||i&gt;=10)
            throw OutOfBounds(i);
        return a[i];
    }
private:
    int a[10];
};
void main()
{
    Array a;
    try
    {
        a[3]=30;
        cout&lt;&lt;"a[1000]"&lt;&lt;a[1000]&lt;&lt;endl;
    }
    catch(OutOfBounds error)//捕获异常类
    {
        cout&lt;&lt;"Subscript value"&lt;&lt;error.indexValue()
        cout&lt;&lt;"Out of bounds.\n";
    }
    return;
}
```

# 二、重新抛出异常和异常规范

## 1.重新抛出异常

```
//当catch语句捕获异常后，不能完全处理异常
//catch语句块可以重新抛出异常，交给更高级函数进行处理
# include &lt;iosteam&gt;
using namespace std;
void h()
{
    throw 0;
}
void g()
{
    try
    {
        h();
    }
    catch
    {
        cout&lt;&lt;"Catch in a\n";
        throw;
    }
}
int main()
{
    try
    {
        g();
    }
    catch(int)
    {
        cout&lt;&lt;"Catch in main\n";
    }
    return 0;
}
```

## 2.异常规范

```
//如果程序运行时，函数抛出了一个没有被列在它的异常规范中的异常时
//系统调用C++标准库中定义的函数unexcepted(),而unexception()
//调用terminate()终止整个程序的运行
void f() throw(X,Y)
{
    ...
}
//函数f只能抛出X、Y异常,throw(X,Y)称为异常规范
//如果写成throw(),则表示不会抛出异常
```

# 三、C++标准库中的异常类

```
//C++异常层次根类为exception类，exception类中的虚函数what()
//返回一个C语言风格的字符串，为异常提供文本描述

//逻辑异常
length_error        //长度异常
domain_error        //时域异常
out_of_range_error  //越界异常
invalid_argument    //参数异常

//运行异常
range_error         //范围错误
overflow_error      //溢出（上溢）异常
underflow_error     //溢出（下溢）

//test:exception 和logic_error类的使用方法
# include&lt;exception&gt;
# include&lt;iosteam&gt;
using namesapce std;
void main()
{
    try
    {
        exception theError;
        throw(theError);
    }
    catch(const exception &amp;theError) //捕捉标准C++异常类的对象
    {
        cout&lt;&lt;theError.what()&lt;&lt;endl;  //用what()成员函数显示出错的原因
    }
    try
    {
        logic_error theLogicError("Logic Error!");
        throw(theLogicError);
    }
    catch(const exception theLogicError)
    {
        cout&lt;&lt;theLogicError.what()&lt;&lt;endl;
    }
}

//运行结果
Unknown exception
Logic Error
```
