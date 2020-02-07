from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if not points:
            return
        map_dist={}
        for num in points:
            map_dist[tuple(num)]=num[0]**2+num[1]**2
        def K_Maxheap(nums,k,i):
            left=2*i+1
            right=2*i+2
            max_index=i
            if left<k and nums[left][1]>nums[max_index][1]:
                max_index=left
            if right<k and nums[right][1]>nums[max_index][1]:
                max_index=right
            if max_index!=i:
                nums[max_index],nums[i]=nums[i],nums[max_index]
                K_Maxheap(nums,k,max_index)
        n=len(map_dist)
        map_arr=list(map_dist.items())
        if K<=n:
            k_maxheap=map_arr[:K]
            for i in range(n//2-1,-1,-1):
                K_Maxheap(k_maxheap,K,i)
            for i in range(K,n):
                if k_maxheap[0][1]>map_arr[i][1]:
                    k_maxheap[0]=map_arr[i]
                    K_Maxheap(k_maxheap,K,0)
        for i in range(K-1,0,-1):
            k_maxheap[i],k_maxheap[0]=k_maxheap[0],k_maxheap[i]
            K-=1
            K_Maxheap(k_maxheap,K,0)
        return [list(item[0]) for item in k_maxheap]

if __name__ == '__main__':
   s=Solution()
   points = [[3,3],[5,-1],[-2,4]]
   K = 2
   res=s.kClosest(points,K)
   print(res)