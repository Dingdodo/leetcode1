from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle :
            return
        # 思想：从低向上
        m=len(triangle)
        dp=[[0]*m for _ in range(m)]

        for i in range(m-1,-1,-1):
            for j in range(len(triangle[i])):
                if i==m-1:
                    dp[i][j]=triangle[i][j]
                else:
                    dp[i][j]=min(dp[i+1][j],dp[i+1][j+1])+triangle[i][j]

        return dp[0][0]

if __name__ == '__main__':
    s=Solution()
    nums=[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
   ]
    res=s.minimumTotal(nums)
    print(res)


