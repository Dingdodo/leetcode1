from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return []

    # 最优解法（使用字典）返回的是下标
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums)==0:
            return[]
        n=len(nums)
        # 用于登记
        res={}
        for i in range(n):
            temp=target-nums[i]
            if temp in res.keys():
                return [res[temp],i]
            else:
                res[nums[i]]=i
        return []
    
if __name__ == '__main__':
    s=Solution()
    nums=[3, 2, 4]
    ans=s.twoSum1(nums,6)
    print(ans)
