from itertools import combinations,permutations
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)==0:
            return
        res=[]
        for i in permutations(nums,len(nums)):
            res.append(list(i))
        return res

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)==0:
            return
        res=[]
        for i in permutations(nums,len(nums)):
            if  list(i) in res:
                continue
            else:
                res.append(list(i))

        return res

s=Solution()
res=s.permute([1,2,3])
s.permuteUnique([1,1,2])
ans=s.permuteUnique([1,1,2])
print(res)
print(ans)
