class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        if not s or n==0:
            return 0
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=0 if s[0]=='0'else 1
        for i in range(2,n+1):
            one=int(s[i-1:i])
            if one!=0:
                dp[i]+=dp[i-1]
            if s[i-2]=='0':
                continue
            two=int(s[i-2:i])
            if two<=26:
                dp[i]+=dp[i-2]
        return dp[n]

    # 方法2
    def numDecodings2(self, s: str) -> int:
        size = len(s)
        if size <= 0:
            return 0
        dp = [0 for _ in range(size + 1)]
        dp[0] = 1

        for i in range(1, size + 1):
            if '1' <= s[i - 1] <= '9':
                dp[i] += dp[i - 1]
            if i > 1 and '10' <= s[i - 2:i] <= '26':
                dp[i] += dp[i - 2]
        return dp[size]
if __name__ == '__main__':
    s1="123"
    s=Solution()
    ans=s.numDecodings(s1)
    print(ans)