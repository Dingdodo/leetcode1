from typing import List


class NumArray:
    # 方法超时
    def __init__(self, nums: List[int]):
        n=len(nums)
        if not nums or n<0:
            return

        self.dp=[0]*(n+1)
        self.dp[1]= nums[0]
        for i in range(2,n+1):
            self.dp[i]=self.dp[i-1]+ nums[i-1]

    def update(self, i: int, val: int) -> None:
        if i < 0 or i > self.n + 1:
            return
        self.nums[i] = val
        self.dp[i + 1] = self.dp[i] + val
        for j in range(i + 2, self.n + 1):
            self.dp[j] = self.dp[j - 1] + self.nums[j - 1]

def sumRange(self, i: int, j: int) -> int:
       return self.dp[j+1]-self.dp[i]
