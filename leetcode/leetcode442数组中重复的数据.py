from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if not nums or len(nums)<=0:
            return

        for i in range(0,len(nums)):
            if nums[i]<1 or nums[i]>len(nums):
                return

        ans=[]
        # temp=0
        for i in range(1,len(nums)+1):
            while nums[i-1]-1!=i-1:

                if nums[i-1]==nums[nums[i-1]-1]:
                    break
                else:
                    nums[nums[i-1]-1],nums[i-1]=nums[i-1],nums[nums[i-1]-1]

        print(nums)
        for i in range(1,len(nums)+1):
            if i!=nums[i-1]:
                ans.append(nums[i-1])
        return ans

if __name__ == '__main__':
    s=Solution()
    nums=[9,9,4,10,8,5,2,2,7,7]
    res=s.findDuplicates(nums)

    print(res)



