class Solution:
    def isHappy(self, n: int) -> bool:
        slow=n
        fast=n
        while True:
            slow = self.SquareSum(slow)
            fast = self.SquareSum(fast)
            fast = self.SquareSum(fast)
            if slow==fast:

                break
        return slow==1


    def SquareSum(self,m:int):

        sum1=0
        while m:
            num=m%10
            sum1+=num*num
            m=m//10
        return sum1


if __name__ == '__main__':
    s=Solution()
    print(s.isHappy(19456))