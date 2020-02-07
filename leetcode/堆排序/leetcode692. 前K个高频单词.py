from audioop import reverse
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if not words:
            return
        res=[]
        def heapAdjust(nums,k,i):
            left=2*i+1
            right=2*i+2
            min_index=i
            if left<k and nums[left][1]<nums[min_index][1]:
                min_index = left
            if (left<k and nums[left][1]==nums[min_index][1] and len(nums[left][0])<len(nums[min_index][0])):
                min_index=left

            if right<k and nums[right][1]<nums[min_index][1] and len(nums[right][0])<len(nums[min_index][0]):
                min_index=right
            if (right < k and nums[right][1] == nums[min_index][1] and len(nums[right][0]) < len(nums[min_index][0])):
                min_index = right
            if min_index!=i:
                temp=nums[min_index]
                nums[min_index]=nums[i]
                nums[i]=temp
                # 调换之后 还可能需要往下一层调整
                heapAdjust(nums,k,min_index)

        map_dist={}
        for word in words:
            if word not in map_dist.keys():
                map_dist[word]=1
            else:
                map_dist[str(word)]+=1
        map_arr=list(map_dist.items())
        length=len(map_arr)
        print(map_arr)
        if k<=length:
            k_head=map_arr[:k]
            print("调整前",k_head)
            for i in range(k//2-1,-1,-1):
                heapAdjust(k_head,k,i)
            print("调整后",k_head)
            for i in range(k,length):
                if (k_head[0][1]==map_arr[i][1])and(len(k_head[0][0])>len(map_arr[i][0])):
                    k_head[0] = map_arr[i]
                    heapAdjust(k_head, k, 0)
                elif k_head[0][1] < map_arr[i][1]:
                    k_head[0] = map_arr[i]
                    heapAdjust(k_head, k, 0)
            print("wangz",k_head)
        res.append(k_head[0][0])
        for i in range(k-1,0,-1):
            res.append(k_head[i][0])
            k_head[i],k_head[0]=k_head[0],k_head[i]
            k-=1
            heapAdjust(k_head,k,0)

        print(res)
        # [::-1]逆
        return [ item[0] for item in k_head]



if __name__ == '__main__':
    s=Solution()
    words=["love", "love", "leetcode", "i", "i", "coding"]
    res=s.topKFrequent(words,4)
    print(res)