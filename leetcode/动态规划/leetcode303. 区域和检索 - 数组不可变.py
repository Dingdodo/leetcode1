from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        n=len(nums)
        if not nums or n<0:
            return
        self.dp=[0]*(n+1)
        self.dp[1]=nums[0]
        for i in range(2,n+1):
            self.dp[i]=self.dp[i-1]+nums[i-1]

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j+1]-self.dp[i]

if __name__ == '__main__':
    nums = [-2, 0, 3, -5, 2, -1]
    n=NumArray(nums)
    res=n.sumRange(0,4)
    print(res)


