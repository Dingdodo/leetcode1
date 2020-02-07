from locale import str


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

     """
    输入: "abcabcbb"
    输出: 3 
    解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
    """
     if len(str)==0:
         return 0
     res=[]
     arr_s=[]
     res_len=[]
     for j in range(len(str)):
         arr_s.append(str[j])
         if j==len(str):
             res.append([str[j]])
             break
         for i in range(j+1,len(str)):
              if str[i] in arr_s:
                  break
              else:
                  arr_s.append(str[i])

         res.append(arr_s)
         arr_s = []
     # 求长度
     for s in res:
         res_len.append(len(s))
     max_len=max(res_len)
     return max_len

s=Solution()
str="pwwkew"
res=s.lengthOfLongestSubstring(str)
print(res)