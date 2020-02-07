from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length=len(nums)
        i=0
        while i<length:
            if nums[i]<=length and nums[i]>0 and nums[i]!=nums[nums[i]-1]:
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
            else:
                i+=1
        print(nums)
        for i in range(1, len(nums) + 1):
            if i != nums[i - 1]:
                return i
        return len(nums)




if __name__ == '__main__':
    nums=[2,3,2,1,-2,4]
    s=Solution()

    res=s.firstMissingPositive(nums)
    print(res)