from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if not nums or len(nums)<0:
            return
        for i in range(len(nums)):
            if nums[i]<1 or nums[i]>len(nums):
                return
        for i in range(len(nums)):
            while(  i !=nums[i]-1) and nums[i]!=nums[nums[i]-1] :
                    nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]


        print(nums)
        ans=[]
        for i in range(len(nums)):
            if (i+1)!=nums[i]:
                ans.append(i+1)
        return ans


if __name__ == '__main__':
    s=Solution()
    nums=[4,3,2,7,8,2,3,1]
    # nums=[1,1,2,4]
    res=s.findDisappearedNumbers(nums)
    print(res)