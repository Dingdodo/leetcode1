from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        dist_temp={}
        dist_str={"a":2,'b': 3,'c': 5,"d":7,'e':11,'f':13,'g':17,'h':19,'i':23,'j':29,
                   'k':31,'l':37,'m':41,'n':43,'o':47,'p':53,'q':59,'r':61,'s':67,'t':71,
                   'u':73,'v':79,'w':83,'x':89,'y':97,'z':101
                  }

        for str_ in strs:
            s_sum=1
            for s in str_:
                s_sum*=dist_str[s]
            if s_sum not in dist_temp:
                temp = []
                temp.append(str_)
                dist_temp[s_sum]=temp

            else:
                dist_temp[s_sum].append(str_)

        for val in dist_temp.values():
            res.append(val)

        return res




s=Solution()
list_a=["eat", "tea", "tan", "ate", "nat", "bat"]
res=s.groupAnagrams([])
print(res)