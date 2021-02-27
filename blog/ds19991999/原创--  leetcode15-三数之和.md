# 原创
：  leetcode15-三数之和

# leetcode15-三数之和

> 
题目详见：[https://leetcode-cn.com/problems/3sum/description/](https://leetcode-cn.com/problems/3sum/description/)


> 
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。


注意：答案中不可以包含重复的三元组。

```
例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

```

这道题我遇到好几次了，B站后台开发工程师笔试题就考了这个。今天就来总结一下解决方案。<br/> 这道题并不难，正常人的第一反应肯定是三个循环，再简单不过了，可是时间复杂度是不是有点大。。。提交也不让通过是吧。<br/> 首先写好边界条件，数组小于三个元素就不满足条件：

```
result = []
nums_len = len(nums)
if nums_len &lt; 3:
	return result

```

注意我们用的是Python语言，所以可以直接**先用内建函数`sort()`排序**，**方便操作。然后可以用一个for循环，两个指针遍历**，时间复杂度也就是
    
     
      
       
        o
       
       
        (
       
       
        
         n
        
        
         2
        
       
       
        )
       
      
      
       o(n^2)
      
     
    o(n2)，与之前的三循环减小了不少。了解了这些差不多就可以实现代码了。

```
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = list()
        nums_len = len(nums)
        if nums_len &lt; 3:
            return result
        l, r, dif = 0, 0, 0
        nums.sort()
        for i in range(nums_len - 2):
            if nums[i] &gt; 0: 
                break
            if i &gt; 0 and nums[i - 1] == nums[i]:
                continue

            l = i + 1
            r = nums_len - 1
            dif = -nums[i]
            while l &lt; r:
                if nums[l] + nums[r] == dif:
                    result.append([nums[l], nums[r], nums[i]])
                    # 这两个while完全可以不要
                    while l &lt; r and nums[l] == nums[l + 1]:
                        l += 1
                    while l &lt; r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] &lt; dif:
                    l += 1
                else:
                    r -= 1
        
        return result

```

另外，leetcode16题也是差不多这个意思：

> 
例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).


思路一模一样，一个for，加上两个指针，时间复杂度为
    
     
      
       
        O
       
       
        (
       
       
        
         n
        
        
         2
        
       
       
        )
       
      
      
       O(n^2)
      
     
    O(n2)

```
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
#         n = len(nums)
#         if n&lt;3:return None
#         res = sum(nums[0:3])
#         diff = abs(res - target)
        
#         for i in range(0,n-2):
#             for j in range(i+1,n-1):
#                 for k in range(j+1,n):
#                     tmp = nums[i]+nums[j]+nums[k]
#                     if diff &gt; abs(tmp - target):
#                         diff = abs(tmp - target)
#                         res = tmp
#         return res               
        n = len(nums)
        if n&lt;3:return None
        nums.sort()
        res = sum(nums[0:3])
        diff = abs(res - target)
        
        for i in xrange(len(nums)-2):
            low = i+1
            high = len(nums)-1
            while low&lt;high:
                tmp = nums[i]+nums[low]+nums[high]
                if abs(res-target) &gt; abs(tmp-target):res = tmp
                elif target &lt; tmp: high -= 1
                else: low += 1
        return res

```
