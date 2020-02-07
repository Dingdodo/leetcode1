from typing import List


def BinSearch(nums:List,target):
    if not nums:
        return 0
    left=0
    right=len(nums)-1
    while left<=right:
        mid=(left+right)>>1
        if nums[mid]>target:
            right=mid-1
        elif nums[mid]<target:
            left=mid+1
        else:
            return mid
    #     一行代码实现两个数的比较
    return int(((left+right) + abs(left-right))/2)
if __name__ == '__main__':
    nums=[1,3,5,6]
    res=BinSearch(nums,2)
    print(res)