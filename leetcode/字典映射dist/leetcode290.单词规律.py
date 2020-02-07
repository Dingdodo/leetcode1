class Solution:
    def wordPattern(self, pattern: str, str_: str) -> bool:

         s=str_.split(' ')
         m = len(s)
         n = len(pattern)
         if m != n:
             return False
         map_dist={}
         map_dist1={}
         # pattern 为key s 为values
         for i in range(n):
             if pattern[i] in map_dist.keys():
                 if map_dist[pattern[i]]!=s[i]:
                     return False
             else:
                 map_dist[pattern[i]]=s[i]
         # s 为key  pattern 为values
         for i in range(n):
             if s[i] in map_dist1.keys():
                 if map_dist1[s[i]]!=pattern[i]:
                     return False
             else:
                 map_dist1[s[i]]=pattern[i]
         return True

if __name__ == '__main__':
    s=Solution()
    pattern = "aaa"
    str1 = "aa aa aa aa"
    res=s.wordPattern(pattern,str1)
    print(res)