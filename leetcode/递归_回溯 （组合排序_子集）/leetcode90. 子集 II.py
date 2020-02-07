from typing import List


class Solution:
    def __init__(self):
        self.res=None

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        # 先排序 重点
        nums.sort()
        res=[]
        n=len(nums)
        def helper(i,temp):
            res.append(temp)
            for j in range(i,n):
                # 同一个父节点的的子节点必须是不同的值
                # 剪枝
                if j>i and nums[j-1]==nums[j]:
                    continue
                helper(j+1,temp+[nums[j]])
        helper(0,[])
        return res
if __name__ == '__main__':
   s=Solution()
   nums=[1,2,2]
   res=s.subsetsWithDup(nums)
   print(res)











