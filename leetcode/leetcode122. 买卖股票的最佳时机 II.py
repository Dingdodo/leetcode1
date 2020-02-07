from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices)<0:
            return
        sumPrice=0
        n=len(prices)
        for i in range(1,n):
            if prices[i]>prices[i-1]:
                sumPrice+=prices[i]-prices[i-1]
        return sumPrice
