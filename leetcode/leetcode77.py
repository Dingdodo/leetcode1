

from itertools import combinations,permutations
class Solution(object):

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res=[]
        temp=[]
        for i in range(1,n+1):
            temp.append(i)
        for j in combinations(temp,k):
            res.append(list(j))
        return res

s=Solution()
res=s.combine(4,2)
print(res)
