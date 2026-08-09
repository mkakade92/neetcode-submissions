class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        


        mp= {}

        longest  = 0
        maxF = 0
        l = 0

        for ind in range(len(s)):

            mp[s[ind]] = 1+mp.get(s[ind],0)

            maxF = max(maxF,mp[s[ind]])

            while (ind-l+1) - maxF > k:
                mp[s[l]]-=1
                l+=1
            longest = max(longest,ind-l+1)
        return longest