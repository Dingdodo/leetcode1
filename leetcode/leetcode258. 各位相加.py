class Solution:
    def addDigits(self, num: int) -> int:
        # return (num-1)%9+1
        # 1.9的倍数返回9
        # 2.小于9 直接返回
        # 3,其他直接返回余9
        if num < 10:
            return num
        elif num % 9 == 0:
            return 9
        else:
            return num % 9