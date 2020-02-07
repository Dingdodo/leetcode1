import math
class Solution:
     def numSquares(self, n: int) -> int:
         squareN=[i**2  for i in range (1,int(math.sqrt(n))+1)]
         queue=[n]
         step=0
         visited=[]
         while queue:
             size =len(queue)
             print(size)
             print(queue)
             step+=1
             for _ in range(size):
                 target=queue.pop(0)
                 for num in squareN:
                     diff=target-num
                     if diff==0:
                         return step
                     if diff not in visited:
                         visited.append(diff)
                         queue.append(diff)

         return step

if __name__=="__main__":
    s=Solution()
    res=s.numSquares(13)
    print(res)

