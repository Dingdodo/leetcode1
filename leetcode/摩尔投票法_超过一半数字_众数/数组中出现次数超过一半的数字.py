from typing import List


class Solution:
    def MoreThanHalfNum(self,nums:List[int]):
        n=len(nums)
        if not nums or n<0:
            return 0
        res=nums[0]
        times=1
        for i in range(1,n):
            if times==0:
                res=nums[i]
                times=1
            elif nums[i]==res:
                 times+=1
            else:
                times-=1
        counter=0
        if times<=0:
            return -1
        else:
            for num in nums:
                if res==num:
                    counter+=1
        if counter>n//2:
            return res
        return -1


if __name__ == '__main__':
    nums=[1,2,3,3,3,3,3,4,2]
    s=Solution()
    res=s.MoreThanHalfNum(nums)
    print(res)






