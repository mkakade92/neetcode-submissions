class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # keep tracking the minimum value
        # update profit by subtracting from minimum value

        minN = prices[0]
        profit = 0

        for p in prices:
            minN = min(p,minN)
            profit = max(profit,p - minN)
        return profit