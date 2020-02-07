import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 0:
            return 0
        n = len(prices)
        maxSum = 0
        minNum = prices[0]

        for i in range(1, n):
            if prices[i] <= minNum:
                minNum = prices[i]
            elif prices[i] - minNum > maxSum:
                maxSum = prices[i] - minNum
        return maxSum
