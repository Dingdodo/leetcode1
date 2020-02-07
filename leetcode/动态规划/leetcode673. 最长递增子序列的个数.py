from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
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
        print(dp)
        map_list={}
        for num in dp:
            if num in map_list:
                map_list[num]+=1
            else:
                map_list[num]=1
        return max(list(map_list.values()))
if __name__ == '__main__':
    s=Solution()
    nums=[1,2,4,3,5,4,7,2]
    ans=s.findNumberOfLIS(nums)
    print(ans)