class Solution:
    def jump(self, nums: List[int]) -> int:
        
        N =  len(nums)
        dp = [float('inf')]*N
        dp[N-1] = 0

        for i in range(N-2,-1,-1):
            min_possible_next = float('inf')
            for possible in range(1,nums[i]+1):
                if i+possible>=N:
                    min_possible_next = 0
                else:
                    min_possible_next = min(min_possible_next,dp[i+possible])
            dp[i] = 1+min_possible_next
        
        return dp[0]