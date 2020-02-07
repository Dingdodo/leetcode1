class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n=len(word1)
        m=len(word2)
        def helper(i,j):
            if i==-1:#字符串1为空
                return j+1 #返回字符串的长度
            if j==-1:
                return i+1
            if word1[i]==word2[j]:
                return helper(i-1,j-1)
            else:
               return min(helper(i,j-1)+1, #插入
                helper(i-1,j)+1, #删除
                helper(i-1,j-1)+1 #替换
                          )
        return helper(n-1,m-1)
    # 如果 i 走完 s1 时 j 还没走完了 s2，那就只能用插入操作把 s2 剩下的字符全部插入 s1。
    # 等会会看到，这两种情况就是算法的 base case

    # 方法2 用动态规划  方法一很多重复的路径
    def minDistanceDP(self, word1: str, word2: str) -> int:

        m=len(word1)
        n=len(word2)
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            dp[i][0]=i
        for j in range(1,n+1):
            dp[0][j]=j

        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+1)
        return dp[m][n]














