from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        found=False
        if  matrix and len(matrix)>0 and len(matrix[0])>0:

            row=0
            columns=len(matrix[0])
            column=columns-1
            rows=len(matrix)
            while row<rows and column>=0:
                print(matrix[row][column])
                if matrix[row][column]==target:
                    found=True
                    break
                elif matrix[row][column]>target:
                    column-=1
                else:
                    row+=1
        return found


if __name__ == '__main__':
    matrix = [[1, 3, 5, 7],
              [10, 11, 16, 20],
              [23, 30, 34, 50]]
    s=Solution()
    res= s.searchMatrix(matrix,13)
    print(res)