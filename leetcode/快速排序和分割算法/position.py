#分割函数
from typing import List


def position(nums:List[int]):
    if not nums:
        return
    i=0
    j=len(nums)-1
    temp=nums[0]
    while i!=j:
        while i<j and nums[j]>temp:
            j-=1
        if i<j:
            nums[i]=nums[j]
            i+=1
        while i<j and nums[i]<temp:
            i+=1
        if i<j:
            nums[j]=nums[i]
            j-=1
        nums[i]=temp
    return i
nums=[6,4,7,5,9]
i=position(nums)
print(i)