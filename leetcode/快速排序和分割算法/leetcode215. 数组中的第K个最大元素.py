from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        n = len(nums)
        if not nums or n < 0:
            return

        start = 0
        end = n - 1
        index = self.partition(nums, start, end)
        while index != n - k:
            if index > n - k:
                end = index - 1
                index = self.partition(nums, start, end)
            else:
                start = index + 1
                index = self.partition(nums, start, end)
        return nums[index]

    # 分割函数 partition函数
    def partition(self, nums: List[int], left: int, right: int):
        baseNumber = nums[left]
        while left < right:
            while left < right and baseNumber <= nums[right]:
                right -= 1
            nums[left] = nums[right]

            while left < right and baseNumber >= nums[left]:
                left += 1
            nums[right] = nums[left]

        nums[left] = baseNumber
        return left