from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islanNums=0
        m=len(grid)
        n=len(grid[0])
        for i in range (m):
            for j in range(n):
                if grid[i][j]=="1":
                   self.bfs(grid,i,j)
                   islanNums+=1

        return islanNums

    def bfs(self,grid,i,j):
        if (i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1'):
            return
        grid[i][j] = '2'
        self.bfs(grid, i + 1, j)
        self.bfs(grid, i - 1, j)
        self.bfs(grid, i, j + 1)
        self.bfs(grid, i, j - 1)

if __name__=="__main__":
    s=Solution()

    grid=[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    print(s.numIslands(grid))