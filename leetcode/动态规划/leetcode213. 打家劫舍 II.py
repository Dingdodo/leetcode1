from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n=len(nums)
        if n==1:
            return nums[0]

        def helper(nums:List[int],first:int,last:int):
            pre_max,cur_max=0,0
            for i in range(first,last):
                temp=cur_max
                cur_max=max(pre_max+nums[i],cur_max)
                pre_max=temp
            return cur_max
        return max(helper(nums,0,n-1),helper(nums,1,n))

if __name__ == '__main__':
    nums=[1,2,3,1]
    s=Solution()
    res=s.rob(nums)
    print(res)