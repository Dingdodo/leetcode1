from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n=len(pairs)
        if not pairs or n==0:
            return 0
        dp=[1]*n
        for i in range(n):
            for j in range(i):
                if pairs[j][1]<pairs[i][0]:
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)

if __name__ == '__main__':
    nums=[[1,2], [2,3], [3,4]]
    s=Solution()
    res=s.findLongestChain(nums)
    print(res)

