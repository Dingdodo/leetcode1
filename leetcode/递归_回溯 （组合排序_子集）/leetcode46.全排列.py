from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums :
            return
        res=[]
        n=len(nums)
        # 访问过就标记
        visted=[0]*n
        def helper(temp,length):
            if length==n:
                res.append(temp)
                return
            for j in range(0,n):
                if visted[j]:
                    continue
                visted[j]=1
                helper(temp+[nums[j]],length+1)
                # 清除标记
                visted[j]=0
        helper([],0)
        return res
    # 方法2
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def backward(nums, temp):
            if not nums:
                res.append(temp)
                return
            for i in range(len(nums)):
                backward(nums[:i] + nums[i + 1:], temp + [nums[i]])

        backward(nums, [])
        return res
if __name__ == '__main__':
    s=Solution()
    nums=['a','b','c']
    res=s.permute(nums)
    print(res)
    num=[3]
    print(num[:0]+num[1:])
