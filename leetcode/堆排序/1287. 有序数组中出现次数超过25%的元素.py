from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if not arr:
            return
        n=len(arr)
        count=0
        temp=arr[0]
        for i in range(n):
            if temp==arr[i]:
                count+=1
                if count>(n*0.25):
                    return arr[i]
            else:
                temp=arr[i]
                count=1
        return -1
