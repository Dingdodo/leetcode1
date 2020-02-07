from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums or len(nums)<=0:
            return
        for i in range(len(nums)):
            if nums[i]<1 or nums[i]>len(nums):
                return
        for i in range(len(nums)):
            while i!=nums[i]:
                if nums[i]==nums[nums[i]-1]:
                    break
                else:
                    nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
        for i in range(len(nums)):
            if i+1!=nums[i]:
                return nums[i]
        return

if __name__ == '__main__':
    s=Solution()
    nums=[3,1,3,4,2]
    res=s.findDuplicate(nums)
    print(res)