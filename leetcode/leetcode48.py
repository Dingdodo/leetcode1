from typing import List
import numpy as np

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        from typing import List
        import numpy as np
        res=[]
        matrix = np.array(matrix).T
        matrix= np.fliplr(matrix)
        return matrix




if __name__ =="__main__":
    matrix =[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
  ]
    # matrix=np.array(matrix).T
    # matrix=np.fliplr(matrix)
    # print(matrix)
    matrix1=[
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]


    s=Solution()
    res=s.rotate(matrix)
    print(res)