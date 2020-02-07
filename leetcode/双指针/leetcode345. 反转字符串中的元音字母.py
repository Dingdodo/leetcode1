class Solution:
    def reverseVowels(self, s: str) -> str:
        if not s:
            return ''
        i=0
        j=len(s)-1
        arr='aeiouAEIOU'
        s2=list(s)
        while i<=j:
            if s2[i]in arr and s2[j]in arr:
                s2[i], s2[j] = s2[j], s2[i]
                i+=1
                j-=1
            elif s2[i] in arr and s2[j] not in arr:
                j-=1
            elif s2[i] not in arr and s2[j] in arr:
                i+=1
            else:
                i+=1
                j-=1
        return "".join(s2)
   #方法2 优化
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and s[i] not in 'aeiouAEIOU':
                i += 1
            while i < j and s[j] not in 'aeiouAEIOU':
                j -= 1
            if i < j:
                s[i], s[j] = s[j], s[i]
            i, j = i + 1, j - 1
        return "".join(s)
if __name__ == '__main__':
    s=Solution()
    s1='hello'
    res=s.reverseVowels(s1)
    print(res)