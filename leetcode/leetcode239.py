class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        if len(nums) == 0:
            return
        if k > len(nums):
            return
        if k == len(nums):
            res.append(max(nums))
            return res
        if k == 1:
            return nums
        temp = nums[:k]
        res.append(max(temp))
        index = 0
        for i in range(k, len(nums)):
            temp[index] = nums[i]
            maxValue = max(temp)
            res.append(maxValue)
            index += 1
            if index > k - 1:
                index = 0
        return res
s=Solution()
# nums =[-7,-8,7,5,7,1,6,0]
nums =[1,3,-1,-3,5,3,6,7]
res=s.maxSlidingWindow(nums,3)
print(res)

