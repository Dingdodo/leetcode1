from heapq import *
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.min_heap=nlargest(k,nums)

        heapify(self.min_heap)
        self.k = k



    def add(self, val: int) -> int:
       if len(self.min_heap)<self.k:
           # 往堆中插入一条新的值
           heappush(self.min_heap,val)
       else:
           # 将值插入到堆中同时弹出堆中的最小值
           heappushpop(self.min_heap,val)
       return self.min_heap[0]





if __name__ == '__main__':
    k=3
    arr=[]
    s=KthLargest(k,arr)
    r1=s.add(3)
    print(r1)
    r2 = s.add(5)
    print(r2)
    r3 = s.add(10)
    print(r3)
    r4 = s.add(9)
    print(r4)
    r5 = s.add(4)
    print(r5)



