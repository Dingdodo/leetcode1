from typing import List
# 奇数 偶数判断
# 0x1=1，0x0=0,1&1=1,1&0=0
# x&0x1=0（偶数）x&0x1=0（奇数）

def ReorderOddEven(nums:List[int]):
    if not nums or len(nums)==0:
        return nums
    left=0
    right=len(nums)-1
    while left<right:
        while left<right and ((nums[left] & 0x1)!=0):

              left+=1
        while left<right and (nums[right]&0x1)==0:

              right-=1
        if left<right:
              nums[right],nums[left]=nums[left],nums[right]

    return nums
if __name__ == '__main__':

     nums=[1,2,3,4,5]
     res=ReorderOddEven(nums)
     print(res)