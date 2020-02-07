class Solution:
    def integerBreak(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[1]=1
        dp[2]=1
        for i in range(2,n+1):
            for j in range(1,i):
                print(j*dp[i-j],j*(i-j))
                # dp[i]=max(dp[i],max(j*dp[i-j],j*(i-j)))
                dp[i] = max(dp[i], max(dp[j], j) * (i - j))
                print("i=",i,dp[i])
        return dp[n]
    # 递归暴力法
    def integerBreak2(self, n: int) -> int:
        if n==2:
            return 1
        res=-1
        for i in range(1,n):
            res=max(res,max(i*(n-i),i*self.integerBreak2(n-i)))
        return res
    # 方法3
    def integerBreak3(self, n: int) -> int:
        if n==2:
            return 1
        a,b=n//3,n%3
        if b==0:return 3**a
        if b==1:return  3**(a-1)*4
        return 3**a *2


if __name__ == '__main__':
    n=10
    s=Solution()
    res=s.integerBreak3(n)
    print(res)
