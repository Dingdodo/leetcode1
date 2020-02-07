class Solution:
    def mySqrt(self, x: int) -> int:
        # x=10 :则0，1，2，3，4，...10
        left=0
        # 取中位数右边的一位
        right=x//2+1
        # 不能取<=,因为题目类似 3平方=9<10,4平方>10,取3
        # 如果取=号，会死循环，因为left=mid,而不是left=mid+1
        while left<right:
         #必须取中位数右边的一位做mid
           mid=(left+right+1)>>1
           square=mid*mid
           if square>x:
              right=mid-1
           else:
               # 很重要，不能mid-1,因为介于3和4之间时取3不是取4
               left=mid
        return left
    # 牛顿迭代法
    def mySqrt1(self, x: int) -> int:
        if x<2:
            return x
        # 起始的时候为1，随机的
        cur=4
        while 1:
            pre=cur
            cur=(cur+x/cur)/2
            if abs(cur-pre)<1e-6:
                return int(cur)



if __name__ == '__main__':
    s=Solution()
    x=10
    index=s.mySqrt(x)
    print(index)
    res=s.mySqrt1(x)
    print(res)
