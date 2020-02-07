class Solution:
    def myAtoi(self, str_: str) -> int:
        # 1.先去除字符头尾空格
        # 2.字符串是否为空
        # 3.'+'."-"的处理
        # 4.系统最大值，最小值处理，最小值：-0x80000000，最大值：0x7FFFFFFF
        str_ = str_.strip()
        if not str_:
            return 0

        sign = 1
        if str_[0] == "+" or str_[0] == '-':
            if str_[0] == '-':
                sign = -1
            str_ = str_[1:]
        i = 0
        num = 0
        n = len(str_)
        while i < n:
            if str_[i] >= '0' and str_[i] <= '9':
                num = num * 10 + int(str_[i])
                i += 1
            else:
                break
        num *= sign

        if num > 0x7FFFFFFF:
            return 0x7FFFFFFF
        elif num < -0x80000000:
            return -0x80000000
        return num
if __name__ == '__main__':
    s=Solution()
    res=s.myAtoi("-91283472332")
    print(res)
    print(0x7FFFFFFF)
    print(-0x80000000)
    print(-1<<32-1)
