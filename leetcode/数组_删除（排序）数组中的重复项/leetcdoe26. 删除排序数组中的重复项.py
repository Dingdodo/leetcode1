from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length=len(nums)
        if length<2:
            return length
        index=1
        for i in range (1,length):
            if nums[index-1]!=nums[i]:
                nums[index]=nums[i]
                index+=1
        return index
    # 方法2
    def removeDuplicates1(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 2:
            return length
        i=0
        for j in range(length):
            if nums[i]!=nums[j]:
                i+=1
                nums[i]=nums[j]
        return i+1




if __name__ == '__main__':
   s=Solution()
   nums=[1,1,2]
   index=s.removeDuplicates1(nums)
   print(index)
