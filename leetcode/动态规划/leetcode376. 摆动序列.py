from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n=len(nums)
        if not nums or n==0:
            return 0
        down,up=1,1
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                up=down+1
            elif nums[i]<nums[i-1]:
                down=up+1
        return max(down,up)


if __name__ == '__main__':
    nums=[1,17,5,10,13,15,10,5,16,8]
    s=Solution()
    res=s.wiggleMaxLength(nums)
    print(res)