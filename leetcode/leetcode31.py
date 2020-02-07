class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)<2:
            return
        i=len(nums)-1
        while i>0 and nums[i]<=nums[i-1]:
            i-=1
        a,b=i,len(nums)-1
        while a<b:
            nums[a],nums[b]=nums[b],nums[a]
            a+=1
            b-=1
        j = i - 1
        for k in range(i, len(nums)):
            if nums[k] > nums[j]:
                nums[j], nums[k] = nums[k], nums[j]
                break
