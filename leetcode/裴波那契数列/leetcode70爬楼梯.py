class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        dp=[0]*(n+1)

        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        print(dp)
        return dp[n]

    def climbStairs1(self, n: int) -> int:
        Fn = 1 / math.sqrt(5)(((1 + math.sqrt(5)) / 2) ** n - ((1 - math.sqrt(5)) / 2) ** n)
        return Fn

    def climbStairs2(self, n: int) -> int:
        a, b = 0, 1

        for _ in range(n):
            a, b = b, a + b

        return b
if __name__ == '__main__':
    s=Solution()
    res=s.climbStairs(3)
    print(res)
    import math