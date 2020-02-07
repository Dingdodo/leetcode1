from typing import List
from heapq import *

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n=len(nums)
        if not nums or n<0:
            return
        first=-1<<32
        second=-1<<32
        third=-float('inf')


