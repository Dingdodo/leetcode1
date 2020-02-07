from typing import List


class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        if not candidates or target<0:
            return
        candidates.sort()
        res=[]
        n=len(candidates)
        def helper(i,temp,target):

            if 0==target:
               res.append(temp)
               return
            # 剪枝1
            if (i == n or target < candidates[i]):
                return

            for j in range(i,n):
                if candidates[j] > target:
                    break
                # 同一个父节点的子节点必须不同值
                # 剪枝2
                if j>i and candidates[j]==candidates[j-1]:
                    continue
                helper(j+1,temp+[candidates[j]],target-candidates[j])
        helper(0,[],target)
        return res
if __name__ == '__main__':
    s=Solution()
    nums= [2,5,2,1,2]
    res=s.combinationSum2(nums,5)
    print(res)




