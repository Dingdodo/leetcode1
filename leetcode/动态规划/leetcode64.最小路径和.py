from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m,n=len(grid),len(grid[0])
        dp=[[0] * n for _ in range(m)]
        # 指定赋值会出错
        # dp=[[0]*(n)]*(m)
        dp[0][0]=grid[0][0]
        # 第0列
        for i in range(1,m):
            dp[i][0]=dp[i-1][0]+grid[i][0]
        #第0行
        for j in range(1,n):
            dp[0][j]=dp[0][j-1]+grid[0][j]
        print(dp)
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        print(dp)
        return dp[m-1][n-1]


if __name__ == '__main__':
    s=Solution()
    grid=  [[1,3,1],
            [1,5,1],
            [4,2,1]]
    res=s.minPathSum(grid)
    print(res)