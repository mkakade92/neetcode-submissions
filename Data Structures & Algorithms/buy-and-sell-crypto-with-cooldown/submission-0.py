class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        n = len(prices)
        hold = [0]*n
        free = [0]*n
        cooldown = [0]*n


        hold[0] = -prices[0]

        free[0] = 0

        cooldown[0] = -float('inf')


        for i in range(1,n):

            hold[i] = max(hold[i-1],free[i-1]-prices[i])
            cooldown[i] = hold[i-1]+prices[i]
            free[i] = max(free[i-1],cooldown[i-1])
        
        return max(free[n-1],cooldown[n-1])