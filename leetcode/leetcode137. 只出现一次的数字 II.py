from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums:
            return
        n=len(nums)

        ans=0
        for i in range(32):
            count=0
            for j in range(n):
                if nums[j]>>i & 0x1==0x1:
                    count+=1
            if count%3!=0:
                ans+= 1<<i
        return ans
if __name__ == '__main__':
    nums=[-2,-2,1,1,-3,1,-3,-3,-4,-2]
    s=Solution()
    res=s.singleNumber(nums)
    print(res)
    print(bin(3))



    # def intToBin32(self, i):
    #     return (bin(((1 << 32) - 1) & i)[2:]).zfill(32)
