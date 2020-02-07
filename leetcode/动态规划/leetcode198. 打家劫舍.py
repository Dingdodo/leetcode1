from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
       if not nums:
           return 0
       n=len(nums)
       pre1,pre2=0,0
       for i in range(n):
           cur=max(pre1+nums[i],pre2)
           pre1=pre2
           pre2=cur
       return pre2

    # 方法2
    def rob2(self, nums: List[int]) -> int:
        # nums=[2,1,1,2,3]
        # 之前的最大值 和当前的最大值比较 max(nums[i]+pre_max.cur_max)
        last_max, cur_max = 0, 0
        # 公式 dp[i]=max(dp[i-2]+num,dp[i-1])
        for i in nums:
            tmp = cur_max
            cur_max = max(last_max + i, tmp)
            last_max = tmp
        return cur_max
    






if __name__ == '__main__':
    s=Solution()
    nums=[2,1,1,2,3]
    res=s.rob2(nums)
    print(res)