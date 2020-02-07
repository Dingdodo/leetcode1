from typing import List
import numpy as np


class Solution:
    # def getMaximumGold(self, grid: List[List[int]]) -> int:

        def initMaze(self):

            grid = [[0,0,0,0,0],[0,0, 6,0,0], [0,5, 8, 7,0], [0,0, 9,0, 0],[0,0,0,0,0]]
            return grid
        def direction_set(self,data):
            data=np.array(data)

            # 找到data中未被走过的地方，并同时记录该地方能够走的地方
            sum_i, sum_j = np.where(data > 0)  # 获取数组中大于0 的 下标 x一列数组 y一列数组
            print(sum_i)
            print(sum_j)
            dir_set = {}

            for i, j in zip(sum_i, sum_j):
                key = str(i) + str(j)
                for wi, wj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    if data[i + wi][j + wj] > 0:  # 向下走
                        if key in dir_set:
                            dir_set[key] += [str(i + wi) + str(j + wj)]
                        else:
                            dir_set[key] = [str(i + wi) + str(j + wj)]
            return dir_set

            # 广度优先搜索 分层 返回分层信息
        def dfs(self,grid,x:int,y:int,count:int):
            print()





if __name__=="__main__":
   s=Solution()
   data=s.initMaze()
   dir_set=s.direction_set(data)
   print(dir_set)