from typing import List


class Solution:
    # 分割函数 partition函数
    def partition(self ,nums:List[int],left:int,right:int):
        # random_index = random.randint(left, right)
        # nums[random_index], nums[left] = nums[left], nums[random_index]

       baseNumber=nums[left]
       while left<right:
           while left<right and baseNumber<=nums[right]:
               right-=1
           nums[left]=nums[right]

           while left<right and baseNumber>=nums[left]:
               left+=1
           nums[right]=nums[left]

       nums[left]=baseNumber
       return left
    def GetLeastNumber(self,nums:List[int],k:int):

        n=len(nums)
        if not nums or n<0:
            return
        res=[]
        start=0
        end=n-1
        index=self.partition(nums,start,end)
        while index!=(k-1):
            if index>k-1:
                end=index-1
                index=self.partition(nums,start,end)
            else:
                start=index+1
                index=self.partition(nums,start,end)
        for i in range(k):
            res.append(nums[i])
        return res

if __name__ == '__main__':
    s=Solution()
    nums=[4,109,1,6,2,7,3,8]
    res=s.GetLeastNumber(nums,6)
    print(res)









