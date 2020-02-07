from typing import List


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
                for p_n in p_res:
                    p_n.append(cand)
                    res.append(p_n)
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

    # 方法3 回溯
    def combinationSum3(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates or target<0:
            return
        candidates.sort()
        res=[]
        n=len(candidates)
        def helper(i,temp,target):
            if target<0:
                return
            if target==0:
                res.append(temp)
                return
            for j in range(i,n):
                if candidates[j] > target:
                    break
                helper(j,temp+[candidates[j]],target-candidates[j])

        helper(0,[],target)
        return res







if __name__ == '__main__':

    s=Solution()
    candidates = [2,3,6,7]
    target = 7
    # res=s.combinationSum(candidates,target)
    # print(res)
    # print("========================================")
    # c= [10,1,2,7,6,1,5]
    # ans=s.combinationSum2(c,8)
    # print("two",ans)
    # print(res)
    res1=s.combinationSum3(candidates,target)
    print(res1)