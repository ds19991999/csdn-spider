# 原创
：  C++实现随机产生一个二维数组

# C++实现随机产生一个二维数组

```
#include &lt;iostream&gt;   
#include &lt;stdlib.h&gt;   
#include &lt;time.h&gt;  
using namespace std;

int main() {
	int n, m;                                   //行数n和列数m
	cin &gt;&gt; n &gt;&gt; m;
	srand((unsigned)time(NULL));

	for (int i = 0; i &lt; n; i++) 
	{
		for (int i = 0; i&lt; m; i++) 
		{
			cout &lt;&lt; (rand() % 900) + 100 &lt;&lt; " ";
			//要取得[a,b)的随机整数，使用(rand() % (b-a))+ a;   
			//要取得[a,b]的随机整数，使用(rand() % (b-a+1))+ a;   
			//要取得(a,b]的随机整数，使用(rand() % (b-a))+ a + 1;   
		}
		cout &lt;&lt; endl;
	}
	return 0;
}
```
