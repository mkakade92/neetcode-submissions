class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        



        n = len(nums)

        total = sum(nums)

        if target > total or target < -total or (total+target)%2!=0:
            return 0

        target  = (total+target)//2


        dp = [[0 for _ in range(target+1)] for _ in range(n+1)]

        dp[0][0]=1

        for j in range(1,target+1):

            dp[0][j] = 0
        

        for i in range(1,n+1):
            for j in range(target+1):

                dp[i][j] = dp[i-1][j] # exclude the current num

                if j-nums[i-1]>=0:
                    dp[i][j]+=dp[i-1][j-nums[i-1]]
        return dp[n][target]