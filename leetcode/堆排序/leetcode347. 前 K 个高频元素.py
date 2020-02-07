import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return
        def heapAdjust(nums,k,i):
            left=2*i+1
            right=2*i+2
            min_index=i
            if left<k and nums[left][1]<nums[min_index][1]:
                min_index=left
            if right<k and nums[right][1]<nums[min_index][1]:
                min_index=right
            if min_index!=i:
                temp=nums[i]
                nums[i]=nums[min_index]
                nums[min_index]=temp
                heapAdjust(nums,k,min_index)


        map_dist={}
        for num in nums:
            if num not in map_dist.keys():
                map_dist[num]=1
            else:
                map_dist[num]+=1
        map_arr=list(map_dist.items())
        length=len(map_arr)

        if k<=length:
           k_minheap=map_arr[:k]
           for i in range(k//2-1,-1,-1):
               heapAdjust(k_minheap,k,i)
           for i in range(k,length):
               if k_minheap[0][1]<map_arr[i][1]:
                   k_minheap[0]=map_arr[i]
                   heapAdjust(k_minheap,k,0)
        for i in range(k-1,0,-1):
           k_minheap[i],k_minheap[0]=k_minheap[0],k_minheap[i]
           k-=1
           heapAdjust(k_minheap,k,0)
        return [ item[0] for item in k_minheap]
               
# 方法2
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        from nltk import collections
        counts = collections.Counter(nums)
        print(counts.keys())
        return heapq.nlargest(k, counts.keys(), key=counts.get)

if __name__ == '__main__':
    nums=[1,2,2,3,1,1,1,1]
    s=Solution()
    res=s.topKFrequent(nums,2)
    print(res)
    ans=s.topKFrequent2(nums,2)
    print(ans)