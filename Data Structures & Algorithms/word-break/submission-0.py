class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp =[None]*len(s)
        
        def recur(ind,s):
            if ind==len(s):
                return True
            
            if dp[ind] is not None:
                return dp[ind]
            found = False
            for end in range(ind,len(s)+1):
                if s[ind:end] in wordDict:
                    found = found or recur(end,s)
            dp[ind] = found
            return dp[ind]
        return recur(0,s)
