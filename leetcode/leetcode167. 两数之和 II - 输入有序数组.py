from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return []
        left=0
        right=len(numbers)-1
        while left<right:
            tsum=numbers[left]+numbers[right]
            if tsum<target:
                left+=1
            elif tsum>target:
                right-=1
            else:
                return[left+1,right+1]
        return []

if __name__ == '__main__':
    s=Solution()
    nums=[2,7,11,15]
    ans=s.twoSum(nums,9)
    print(ans)