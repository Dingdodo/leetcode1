from typing import List

# 从第一个数开始count=1，遇到相同的就加1，
# 遇到不同的就减1，减到0就重新换个数开始计数，总能找到最多的那个
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        if not nums or n<0:
            return -1
        times=0
        x=None
        for num in nums:
            if x==num:
                times+=1
            elif times==0 :
                x=num
                times=1
            else:
                times-=1
        times=0
        for num in nums:
            if num==x:
                times+=1
        if times>n//2:
            return x
        return -1
if __name__ == '__main__':
    nums=[2,2,1,1,1,2,2]
    s=Solution()

    res=s.majorityElement(nums)
    print(res)
    


