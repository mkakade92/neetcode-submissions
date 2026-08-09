class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        

        n  =len(coins)
        coins.sort()
        dp =[[0]*(amount+1) for _ in range(n+1)]


        for i in range(n+1):
            dp[i][0] = 1
        
        for i in range(n-1,-1,-1):
            for rem in range(amount+1):
                if rem>=coins[i]:
                    dp[i][rem] = dp[i+1][rem]
                    dp[i][rem]+=dp[i][rem-coins[i]]
        return dp[0][amount]