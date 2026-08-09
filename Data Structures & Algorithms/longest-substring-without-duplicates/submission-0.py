class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        #invariant : no dbplicate in substring s[st:e]
        mp = {}
        st = 0
        L = len(s)
        longest = 0
        for e in range(L):
            if s[e] in mp:
                st = max(st,mp[s[e]]+1)
            mp[s[e]] = e
            longest = max(longest,e-st+1)
        return longest
            

