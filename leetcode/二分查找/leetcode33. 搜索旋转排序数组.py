from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        if not nums or n<0:
            return -1
        start=0
        end=n-1
        while start<=end:
            mid=start+(end-start)//2

            if nums[mid]==target:
                return mid
            if nums[start] == nums[mid]:
                start += 1
                continue

            if nums[start]<nums[mid]:
                # nums[start]<=target有=号 细节
                if nums[start]<=target and nums[mid]>target:
                    end=mid-1
                else:
                    start=mid+1
            else:
                if nums[mid]<target and nums[end]>=target:
                    start=mid+1
                else:
                    end=mid-1
        return -1
if __name__ == '__main__':
    s=Solution()
    nums=[3,1]
    target=1
    res=s.search(nums,target)
    print(res)











