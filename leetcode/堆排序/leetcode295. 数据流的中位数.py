from heapq import *
# 大顶堆 将push(e)改为push(-e)、pop(e)改为-pop(e)。
# python默认小顶堆，对于如何实现大顶堆，
# 1.添加元素进去时，取反，
# 2.取出元素时，也取反
class MedianFinder:
    # 数据分为两部分A 和B 数据集A中的所有数值小于数据集B中的数值
    # 数据集A用大顶堆维护 数据集B用小顶堆维护
    # 新数据加入 先往小顶堆加入，然后小顶堆调整 出堆顶元素加入到左边的
    # 大顶堆，最后判断大顶堆里的元素个数是否小于小顶堆的元素个数（相差绝对值不能大于1）
    # 如果小顶堆元素个数大于大顶堆的元素个数，大顶堆出堆顶元素 加入到小顶堆
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap=[]
        self.max_heap=[]
        # 构建大顶堆（维护左边的值ps左边的堆值全部小右边的堆值）
        heapify(self.max_heap)
        #构建小顶堆 维护右边的大值
        heapify(self.min_heap)



    def addNum(self, num: int) -> None:
      # 加入的新值 num 直接进入小顶堆（右边的堆）
       heappush(self.min_heap,num)
       # 调整好小顶堆 出来堆顶元素 放到大顶堆中
       heappush(self.max_heap,-heappop(self.min_heap))
       # 确保右边的小顶堆里面的个数大于等于  左边的大顶堆里的个数
       if len(self.min_heap)<len(self.max_heap):
           heappush(self.min_heap,-heappop(self.max_heap))

    def findMedian(self) -> float:
        n=len(self.max_heap)
        m=len(self.min_heap)

        return self.min_heap[0] if m!=n else (-self.max_heap[0]+self.min_heap[0])/2

# 方法2
# def __init__(self):
#     """
#     initialize your data structure here.
#     """
#     self.large = []
#     self.small = []
#
#
# def addNum(self, num: int) -> None:
#     if len(self.large) > len(self.small):
#         heapq.heappush(self.small, -heapq.heappushpop(self.large, num))
#     else:
#         heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
#
#
# def findMedian(self) -> float:
#     if len(self.large) == len(self.small):
#         return (self.large[0] - self.small[0]) / 2
#     else:
#         return self.large[0]