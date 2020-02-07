# 公式C(n,2n)/(n+1)
class Solution:
    def numTrees(self, n: int) -> int:
        if n==1:
            return 1
        Csum=1
        for i in range(n+1,2*n+1):
            Csum*=i
        Cs=self.factorial(n)
        print(Cs)
        print(Csum)
        print(Csum//Cs)
        return (Csum//Cs)//(n+1)


    def factorial(self,n):
        if n==1:
            return 1
        return n*(self.factorial(n-1))

if __name__ == '__main__':
    s=Solution()
    res=s.numTrees(3)
    print(res)