from typing import List


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        n=len(A)
        if not A or n<0:
            return
        num=A[0]
        for i in range(1,n):
            if num>A[i]:
                return i-1
            else:
                num=A[i]
        return -1
    # 方法2
    def peakIndexInMountainArray1(self, A: List[int]) -> int:
        start = 0
        end = len(A) - 1
        while (start <= end):
            mid = start + (end - start) // 2
            if A[mid] > A[mid + 1] and A[mid] > A[mid - 1]:
                return mid
            if mid > 0 and A[mid] > A[mid - 1]:
                start = mid + 1
            if mid > 0 and A[mid] < A[mid - 1]:
                end = mid - 1
    # 方法3
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        m = max(A)
        return A.index(m)


if __name__ == '__main__':
   s=Solution()
   nums=[0,1,2,3,4,1,2]
   index=s.peakIndexInMountainArray(nums)
   print(index)