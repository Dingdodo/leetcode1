from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        flag=0
        if n==0:
            return None
        if n==1:
            return nums
        for i in range(len(nums)-1,0,-1):
            if nums[i]>nums[i-1]:
                flag=i-1
                break

        max_val=nums[flag]
        flag_1=0
        for j in range(flag+1,n):
            if max_val<nums[j]:
                flag_1=j
                break

        for k in range(flag_1+1,n):
            if nums[k]>max_val and nums[k]<nums[flag_1]:
                flag_1=k
        # 和后面比找的数 的最小的数交换
        t=0
        t=nums[flag]
        nums[flag]=nums[flag_1]
        nums[flag_1]=t

        res=nums[:flag+1]

        nums_temp=sorted(nums[flag+1:])

        res.extend(nums_temp)

        return res


if __name__=='__main__':
   s=Solution()
   nums=[1,3,2]
   res=s.nextPermutation(nums)
   print("kgfmh",res)


