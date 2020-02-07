from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n=len(nums)
        if not nums or n<0:
            return
        start=0
        end=n-1
        while start<=end:
            mid=start+(end-start)//2
            if nums[mid]==target:
                return True
            # 去重 很关键的一步
            if nums[start]==nums[mid]:
                start+=1
                continue

            if nums[start]<nums[mid]:
                if target<nums[mid] and target>=nums[start]:
                    end=mid-1
                else:
                    start=mid+1
            else:
                if nums[mid]<target and target<=nums[end]:
                    start=mid+1
                else:
                    end=mid-1
        return False

#     方法2
    def search1(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        left = 0
        right = len(nums) - 1
        while left <= right:
            if target == nums[left] or target == nums[right]:
                return True
            if target < nums[left] and target > nums[right]:
                return False
            if target < nums[right]:
                right -= 1
            if nums[left] < target:
                left += 1
        return False

if __name__ == '__main__':
    s=Solution()
    nums=[3,1]
    target=1
    print(s.search(nums,target))

