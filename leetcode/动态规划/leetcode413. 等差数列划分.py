from typing import List


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        n=len(A)
        if not A or n==0:
            return 0
        dp=[0]*n
        for i in range(2,n):
            if A[i]-A[i-1]==A[i-1]-A[i-2]:
                dp[i]=dp[i-1]+1
        totel=0
        for num in dp:
            print(num)
            totel+=num
        return totel
if __name__ == '__main__':
    A=[1,2,3,4,7,8,9]
    s=Solution()
    totel=s.numberOfArithmeticSlices(A)
    print(totel)