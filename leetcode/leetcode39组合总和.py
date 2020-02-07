class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        for i,cand in enumerate(candidates):
            if cand==target:
                res.append([cand])
            elif cand<target:
                p_res=self.combinationSum(candidates[i:],target-cand)
                print("++++++++++++++")
                print(p_res)
                for p_n in p_res:
                    p_n.append(cand)
                    res.append(p_n)
                print("res-->",res)

        return res

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates=sorted(candidates)
        res=[]
        temp=[]
        dist={}
        for i, c in enumerate(candidates):
            print(i,c)
            if c==target:
               dist[c]=i
               res.append([c])
               temp.append(i)
            elif c< target:
                dist[c] = i
                temp.append(i)
                p_res = self.combinationSum(candidates[i:], target - c)
                for p_n in p_res:
                    p_n.append(c)
                    res.append(p_n)

        print(temp)
        return res




s=Solution()
candidates = [2,3,5]
target = 8
res=s.combinationSum(candidates,target)
print(res)
print("========================================")
# c= [10,1,2,7,6,1,5]
# ans=s.combinationSum2(c,8)
# print("two",ans)
# print(res)