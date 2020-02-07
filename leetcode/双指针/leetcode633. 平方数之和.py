import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i=0
        j= int(c**0.5)
        while i<=j:
            target=i*i+j*j
            if target==c:
                return True
            elif target>c:
                j-=1
            else:
                i+=1
        return False
if __name__ == '__main__':
    s=Solution()
    print(s.judgeSquareSum(3))
