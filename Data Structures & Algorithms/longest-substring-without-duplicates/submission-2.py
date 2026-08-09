class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        #invariant : no dbplicate in substring s[st:e]
        mp = {}
        st = 0
        L = len(s)
        longest = 0
        for e in range(L):
            if s[e] in mp:
                st = max(st,mp[s[e]]+1) # eg in abba, st will be backwards in max is not used, because it will already be at index 2 on seeing a suplicatet b at index 1.
            mp[s[e]] = e
            longest = max(longest,e-st+1)
        return longest
            

