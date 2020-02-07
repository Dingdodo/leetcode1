from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums or len(nums)<=0:
            return
        n=len(nums)
        thisSum=0
        maxSum=nums[0]
        for i in range(1,n):
            if thisSum>0:
                thisSum+=nums[i]
            else:
                thisSum=nums[i]
            if thisSum>maxSum:
                maxSum=thisSum
        return maxSum
    # 方法2，Kadane算法
    def maxSubArray2(self, nums: List[int]) -> int:
        n=len(nums)
        if not nums or n<0:
            return
        thisSum=maxSum=nums[0]
        for i in range(n):
            thisSum=max(nums[i],nums[i]+thisSum)
            maxSum=max(thisSum,maxSum)
        return maxSum

if __name__ == '__main__':
    nums=[-2,1,-3,4,-1,2,1,-5,4]
    s=Solution()
    maxSum=s.maxSubArray2(nums)
    print(maxSum)