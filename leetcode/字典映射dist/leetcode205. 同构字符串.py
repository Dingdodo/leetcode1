class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if not(s or t):
            return False
        def isIsomorphicHelper(s,t)->bool:
            n=len(s)
            map_dist={}
            for i in range(n):
                if s[i] in map_dist.keys():
                    if map_dist[s[i]]!=t[i]:
                        return False
                else:
                    map_dist[s[i]]=t[i]
            return True
        return isIsomorphicHelper(s,t)and isIsomorphicHelper(t,s)
if __name__ == '__main__':
    s=Solution()
    s1 = "erg"
    t = "add"
    res=s.isIsomorphic(s1,t)
    print(res)