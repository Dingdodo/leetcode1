#给定正整数 n，
# 找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。
# 你需要让组成和的完全平方数的个数最少。
import math
class Solution(object):

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = []  # 保存1-n的平方数 1 ,4,9,.....
        for i in range(1,n+1):
            if math.sqrt(i)%1.0==0:
                  res.append(i)
            return res

    def numSquares1(self, n: int) -> int:

        squareN = [i ** 2 for i in range(1, int(math.sqrt(n)) + 1)]

        queue = [n]
        step = 0
        visited = set()
        while queue:
            size = len(queue)
            step += 1
            for _ in range(size):
                target = queue.pop(0)
                for num in squareN:
                    diff = target - num
                    if diff == 0:
                        return step
                    if diff not in visited:
                        visited.add(diff)
                        queue.append(diff)
                        print(queue)

        return step
    # 方法3
    def numSquares3(self, n: int) -> int:

        squareList=[i**2 for i in range(int(n**0.5)+1)]
        print(squareList)
        dp=[i for i in range(n+2)]
        for i in range(1,n+1):
            for number in squareList:
                if i<number:
                    break
                dp[i]=min(dp[i],dp[i-number]+1)
        return dp[n]

if __name__ == '__main__':
    s=Solution()
    res=s.numSquares3(14)
    print(res)
    min_val = float("inf")
    print(min_val)
    pre = -float("inf")
