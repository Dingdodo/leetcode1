class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left=0
        right=num//2+1
        while left<=right:
            mid=(left+right)>>1
            square=mid*mid
            if square==num:
                return True
            elif square>num:
                right=mid-1
            else:
                left=mid+1
        return False
if __name__ == '__main__':
    s=Solution()
    num=14
    print(s.isPerfectSquare(num))