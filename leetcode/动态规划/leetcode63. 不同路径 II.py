from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 遇到障碍后返回dp=0 就可以了
        if not obstacleGrid:
            return 0
        # 行数
        m=len(obstacleGrid)
        # 列数
        n=len(obstacleGrid[0])
        dp=[[0]*n for _ in range(m)]

        for i in range(m):
            if obstacleGrid[i][0]==1:
                dp[i][0]=0
                break
            else:
                dp[i][0]=1
        print(dp)
        for j in range(n):
            if obstacleGrid[0][j]==1:
                dp[0][j]=0
                break
            else:
                dp[0][j]=1
        print(dp)
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        print(dp)
        return dp[m-1][n-1]

if __name__ == '__main__':
    s=Solution()
    nums=[[0,0,0],
          [1,1,0],
          [1,0,0]]
    res=s.uniquePathsWithObstacles(nums)
    print(res)