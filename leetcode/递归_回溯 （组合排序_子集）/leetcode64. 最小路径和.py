from typing import List


class Solution:
    res=[]
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return
        # 行数   # 列数
        m,n =len(grid),len(grid[0])
        def helper(grid,temp,i,j):

            if i==m-1 and j==n-1:
                self.res.append(temp)
            if i<0 or i>n-1 or i>m-1 or (j<0 or j>n-1 or j>m-1):
                return
            helper(grid,temp+[grid[i][j]],i+1,j)
            helper(grid,temp+[grid[i][j]],i,j+1)
        helper(grid,[],0,0)
        temp=1110000

        for list1 in self.res:
            if sum(list1)<temp:
                temp=sum(list1)
        return temp+grid[m-1][n-1]
















if __name__ == '__main__':
    s=Solution()

    grid=[[0,1],[1,0]]
    res=s.minPathSum(grid)
    print(res)