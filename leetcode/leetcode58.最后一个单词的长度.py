class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip(' ')
        L = s.split(' ')[-1]
        return len(L)

if __name__ == '__main__':
     s=Solution()
     s1="     "

     res=s.lengthOfLastWord(s1)
     print(res)


