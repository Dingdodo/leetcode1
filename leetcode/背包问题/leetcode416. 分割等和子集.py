from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumNums=0
        for num in nums:
            sumNums+=num
        if sumNums%2!=0:
            return False
        W=sumNums//2 #背包的承受重量
        dp=[False]*(W+1)
        dp[0]=True
        for num in nums:
            for i in range(W,num-1,-1):
                dp[i]=dp[i] or dp[i-num]
        print(dp)
        return dp[W]
if __name__ == '__main__':
    s=Solution()
    nums=[1, 5, 11, 5]
    res=s.canPartition(nums)
    print(res)
