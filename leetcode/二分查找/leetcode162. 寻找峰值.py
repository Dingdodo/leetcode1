from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        if not nums or n<0:
            return
        start=0
        end=n-1
        while start<end:
            mid=start+(end-start)//2
            if mid-1<0 and mid+1<n and nums[mid]>nums[mid+1]:
                    return mid
            elif mid+1==n and mid-1>=0 and nums[mid]>nums[mid-1]:
                    return mid
            elif nums[mid]>nums[mid+1]:
                end=mid
            else:
                start=mid+1
        return start
if __name__ == '__main__':
    nums=[1,2,1,3,5,6,4]
    s=Solution()
    res=s.findPeakElement(nums)
    print(res)


