class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s or len(s) == 0:
            return True
        n = len(s)
        import string
        s = s.lower()
        print(s)
        array = []
        for i in range(n):
            if (s[i] in string.ascii_lowercase) or (s[i] in string.ascii_uppercase):
                array.append(s[i])

        print(array)
        m = len(array)
        i, j = 0, m - 1
        while i < j:
            if array[i] != array[j]:
                return False
            i += 1
            j -= 1
        return True
#     方法二
    def isPalindrome1(self, s: str) -> bool:
        # isalnum 如果字符串至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
        s="".join(filter(str.isalnum,s))
        print(s)
        s=s.lower()
        return s==s[::-1]


if __name__ == '__main__':
   s1= "0P334gdfg  hdgh xA"
   s=Solution()
   res=s.isPalindrome1(s1)
   print(res)
