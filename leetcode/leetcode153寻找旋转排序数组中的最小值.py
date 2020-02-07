from envs.py37.Lib.typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums or len(nums)<=0:
            return nums
        index1=0
        index2=len(nums)-1
        indexMid=index1
        while nums[index1]>=nums[index2]:
            if index2-index1==1:
                indexMid=index2
                break
            indexMid=(index1+index2)>>1
            if nums[index1]==nums[index2] and nums[index1]==nums[indexMid]:

                return self.MinInOrder(nums,index1,index2)

            if nums[index1]<=nums[indexMid]:
                index1=indexMid
            elif nums[index2]>=nums[indexMid]:
                index2=indexMid
        return nums[indexMid]

    def MinInOrder(self,nums,index1,index2):

        result=nums[index1]

        for i in range(index1+1,index2+1):

            if result>nums[i]:
                result=nums[i]

        return result
if __name__ == '__main__':
    s=Solution()
    nums=[1,0,1,1,1]
    result=s.findMin(nums)
    print(result)