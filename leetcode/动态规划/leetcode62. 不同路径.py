from typing import List


class Solution:
    # res=[]
    def uniquePaths(self, m: int, n: int) -> int:
        # if (n<0 or m<0):
        #     return 0
        # grid=[[1]*n for _ in range(m)]
        #
        # def helper(grid,i,j,temp):
        #     if i<0 or i>m-1 or j<0 or j>n-1:
        #         return
        #     if i==m-1 and j==n-1:
        #         self.res.append(temp)
        #
        #     helper(grid,i+1,j,temp+[grid[i][j]])
        #     helper(grid,i,j+1,temp+[grid[i][j]])
        # helper(grid,0,0,[])
        # return len(self.res)
        if m<0 or n<0:
            return 0
        dp=[[0]*n for _ in range(m)]
        print(dp)
        for i in range(m):
            dp[i][0]=1
        for j in range(n):
            dp[0][j]=1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]



if __name__ == '__main__':
    s=Solution()
    res=s.uniquePaths(3,2)
    print(res)