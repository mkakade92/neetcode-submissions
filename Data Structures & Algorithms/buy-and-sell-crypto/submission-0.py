class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP =0
        i=0
        j=1
        N = len(prices)
        while j<N:
            if prices[j]>prices[i]:
                maxP = max(maxP,prices[j]-prices[i])
            else:
                i=j
            j+=1
        
        return maxP