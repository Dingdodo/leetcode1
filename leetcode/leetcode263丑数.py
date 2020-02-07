class Solution:
    def isUgly(self, num: int) -> bool:
        while num != 1:
            temp = num
            if num % 2 == 0:
                num //= 2
            if num % 3 == 0:
                num //= 3
            if num % 5 == 0:
                num //= 5
            if temp == num:
                return False
        return True
    # 方法2
    def isUgly2(self, num: int) -> bool:
        if num <= 0:  # 负数和0，不是
            return False
        if num == 1:  # 1是
            return True
        if num >= 2:  # >=2
            while num % 2 == 0:  # 包含的2，一次性除完
                num /= 2
            while num % 3 == 0:  # 包含的3，一次性除完
                num /= 3
            while num % 5 == 0:  # 包含的5，一次性除完
                num /= 5
            return (num == 1)  # 除完了，剩1，才是