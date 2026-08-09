class Solution:
    def countSubstrings(self, s: str) -> int:
        

        n = len(s)
        memPalin = [[False]*n for _ in range(n)]
        dp = [[0]*n for _ in range(n)]


        for i in range(n):
            memPalin[i][i] = True
            dp[i][i] = 1
        
        for i in range(n-1):
            memPalin[i][i+1] = s[i]==s[i+1]

        for w in range(3,n+1):
            for i in range(n-w+1):
                j = i+w-1
                memPalin[i][j] = s[i]==s[j] and memPalin[i+1][j-1]
        

        for w in range(2, n+1):
            for i in range(n-w+1):
                j = i+w-1
                dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]
                if memPalin[i][j]:
                    dp[i][j] += 1
        
        return dp[0][n-1]
