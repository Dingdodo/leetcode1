from typing import List

from test import j


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums or len(nums)==0:
            return 0
        length=len(nums)
        if length<3:
            return length
        j=length-1
        temp=0
        while j>0:
            num=0
            for i in range(j-1,-1,-1):
                if nums[i]==nums[j]:
                    num+=1
                    temp=i
            print(num)

            if num>=2:
                while num>1:
                    nums[temp]=None
                    temp+=1
                    num-=1

                j=temp-1
            else:
                j-=1
        count=0
        for i in range(length):
            if nums[i]==None:
                count+=1
        if count>0:
           for i in range(count):
               nums.remove(None)

        return len(nums)

    def removeDuplicates1(self, nums: List[int]) -> int:
        length=len(nums)
        if length<3:
            return length
        index=2
        for i in range(length):
            if nums[index-2]!=nums[i]:
               nums[index]=nums[i]
               index+=1
        return index
    # 移除元素
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums)==0:
            return 0
        i=0
        if j in range(len(nums)):
            if nums[j]!=val:
                nums[i]=nums[j]
                i+=1
        return i










if __name__ == '__main__':
    s=Solution()
    # nums= [1,2,2]
    nums=[1,1,1,2,2,3]
    # nums=[1,1,1,2,2,2,3,3]
    # nums=[0,0,1,1,1,1,2,3,3]
    nums=s.removeDuplicates(nums)
    num1=s.removeDuplicates1([2,2,2,3,3,3])
    print(nums)
    print("================")
    print(num1)
