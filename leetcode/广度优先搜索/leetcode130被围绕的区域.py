from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board)==0:
            return []

        return self.bfs(board)



    def bfs(self,board):
        m,n=len(board),len(board[0])
        queue=[]

        #第一行和最后一行的O 坐标入栈
        for i in range(n):
            if board[0][i]=="O":
                board[0][i] = "-"
                queue.append((0,i))
            if board[m-1][i] == "O":
                board[m-1][i] = "-"
                queue.append((m-1, i))
        # 第一列和最后一列的O 坐标入栈
        for j in range(m):
            if board[j][0]=="O":
                board[j][0] = "-"
                queue.append((j,0))
            if board[j][n-1]=="O":
                board[j][n-1] = "-"
                queue.append((j,n-1))
        print(board)
        print(queue)
        while queue:
              top=queue.pop(0)
              x,y=top

              #上下左右添加
              if x - 1 > 0 and board[x - 1][y] == "O":
                  board[x - 1][y] = "-"
                  queue.append((x - 1, y))
              if x + 1 < len(board) and board[x + 1][y] == "O":
                  board[x + 1][y] = "-"
                  queue.append((x + 1, y))
              if y - 1 > 0 and board[x][y - 1] == "O":
                  board[x][y - 1] = "-"
                  queue.append((x, y - 1))
              if y + 1 < len(board[0]) and board[x][y + 1] == "O":
                  board[x][y + 1] = "-"
                  queue.append((x, y + 1))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "-":
                    board[i][j] = "O"
        return board



if __name__=="__main__":
    s=Solution()
    board=[["O","O","O"],["O","X","O"],["O","O","O"]]
    res=s.solve(board)
    print(res)