from typing import List


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        最简单的方法应该是求和，然后和1到n项的数列和对比，相差的数就是缺的这个数
        """
        res=0
        nums.sort()
        for i in range(len(nums)):
            if nums[i]!=i:
                return i
        return nums[-1]+1

    def missingNumber1(self, nums: List[int]) -> int:
        if not nums or len(nums)<0:
            return
        for i in range (len(nums)):
            if nums[i]<0 or nums[i]>len(nums):
                return
        for i in range(len(nums)):
            while i!=nums[i] and nums[i]<len(nums):
                nums[nums[i]],nums[i]=nums[i],nums[nums[i]]
        print(nums)
        for i in range(len(nums)):
            if i!=nums[i]:
                return i
        return len(nums)



if __name__ == '__main__':

    s=Solution()
    nums=[0]
    nums1= [0]
    # res=s.missingNumber(nums)
    ans=s.missingNumber1(nums1)
    print(ans)
