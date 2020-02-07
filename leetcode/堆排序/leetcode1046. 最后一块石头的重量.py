from typing import List
from heapq import *

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return
        n=len(stones)
        for i in range(n):
            stones[i]=-stones[i]
        heapify(stones)
        while stones:
            y=-heappop(stones)
            if len(stones)==0:
                return y
            x=-heappop(stones)
            if len(stones)==0:
                return x
            if x!=y:
                heappush(stones,x-y)
        return 0

    def lastStoneWeight2(self, stones: List[int]) -> int:
        if not stones:
            return
        n = len(stones)
        for i in range(n):
            stones[i] = -stones[i]
        heapify(stones)
        while len(stones)>1:
            y = -heappop(stones)
            x = -heappop(stones)
            if x!=y:
               heappush(stones, x - y)
        return 0 if len(stones)==0 else -stones[0]
if __name__ == '__main__':
    s=Solution()
    nums=[2,7,4,1,8,1]
    res=s.lastStoneWeight(nums)
    print(res)








