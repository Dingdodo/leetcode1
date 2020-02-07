class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row=[]
        col=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                   row.append(i)
                   col.append(j)
        for i,j in zip(row,col):
            print(i,j)
            matrix[i]=[0]*len(matrix[0])
            for k in range(len(matrix)):
                matrix[k][j] = 0
        return matrix

matrix=[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
s=Solution()
print(s.setZeroes(matrix))

import pandas as pd
newfile=pd.read_csv("new.csv",sep='\t',encoding="gbk")
print(newfile)