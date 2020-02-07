from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        if not nums or n==0:
            return 0
        dp=[0]*n
        for i in range(n):
            max_value=1
            for j in range(i):
                if nums[i]>nums[j]:
                   max_value=max(max_value,dp[j]+1)
                dp[i]=max_value
        return max(dp)

if __name__ == '__main__':
    s=Solution()
    nums=[10,9,2,5,3,7,101,18]
    res=s.lengthOfLIS(nums)
    print(res)












