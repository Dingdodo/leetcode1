import copy
from typing import List


class Solution:
    def __init__(self):
        self.res = None
    def subsets(self, nums: List[int]) -> List[List[int]]:

          item=[]
          self.res=[]
          self.res.append(item)
          self.generate(0, nums, item)
          return self.res

    def generate(self,i,nums,item):
        if i>=len(nums):
            return

        item.append(nums[i])
        # 深拷贝浅拷贝问题
        ta = []
        ta.extend(item)
        # a=copy.deepcopy(item)#对象拷贝，深拷贝 缺点费时
        self.res.append(ta)
        self.generate(i+1,nums,item)
        item.pop()
        self.generate(i+1,nums,item)
    # 方法2 位运算 & 来
    def subsets1(self, nums: List[int]) -> List[List[int]]:
        res=[]
        all_m=1<<len(nums)
        for i in range(all_m):
            temp=[]
            for j in range(len(nums)):
               if i &(1<<j):
                    temp.append(nums[j])
            res.append(temp)
        return res
    #方法3
    def subsets2(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                helper(j + 1,tmp + [nums[j]] )

        helper(0, [])
        return res









if __name__ == '__main__':
    s=Solution()
    nums=[1,2,3]
    # res=s.subsets(nums)
    # print(res)
    #
    # result=s.subsets1(nums)
    # print(result)

    res=s.subsets2(nums)
    print(res)