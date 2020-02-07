import sys
sys.setrecursionlimit(9000000)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            flag=1
            n=-n

        res=1
        while n:
            if n&1:#n=偶数:0，n=奇数:1
                res*=x
            x*=x
            n>>=1
        if flag==1:
            return 1/res
        return res
    def powWithexponent(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n==1:
            return x

        result=self.powWithexponent(x,n>>1)
        result*=result
        if n&1==1:
            result*=x
        return result
    # 方法2
    def pow1(self, x: float, n: int) -> float:
        res=1
        while n:
            if n&1:
                res*=x
            x*=x
            n>>=1






if __name__ == '__main__':
    for i in range(10):
        print(i,"=",i&1)
    s=Solution()
    res=s.myPow(2,-3)
    print(res)

    print(s.pow1(2,3))