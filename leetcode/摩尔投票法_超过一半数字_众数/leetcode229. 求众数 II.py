from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        if not nums or n<0:
            return
        res=[]
        x,y,cx,cy=0,0,0,0
        for num in nums:
            if x==num:
                cx+=1
            elif y==num:
                cy+=1
            elif cx==0:
                x=num
                cx+=1
            elif cy==0:
                y=num
                cy+=1
            else:
                cx-=1
                cy-=1
        count1,count2=0,0
        for num in nums:
            if x==num:
                count1+=1
            elif y==num:
                count2+=1
        if count1>n//3:
            res.append(x)
        if count2>n//3:
            res.append(y)
        return res

if __name__ == '__main__':
    s=Solution()
    nums=[1,1,1,3,3,2,2,2]
    res=s.majorityElement(nums)
    print(res)