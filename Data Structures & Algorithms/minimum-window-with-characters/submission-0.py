class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mp1 = {} # this is what we need in our window
        for c in t:
            mp1[c] = mp1.get(c,0)+1

        mp2 = {}  #this will track our window
        
        res_len = float('inf')
        res = ""
        left = 0
        right = 0
        have = 0
        need = len(mp1)
        for right in range(len(s)):
            curr = s[right]
            mp2[curr] = mp2.get(curr,0)+1 # increase window char freq
            if curr in mp1 and mp2[curr]==mp1[curr]:
                have+=1 # we found 1 char freq match in t and s
            
            while have>=need: # reduce window size untill we have valid window
                if res_len > (right-left+1):
                    res = s[left:right+1]
                    res_len = len(res)
                mp2[s[left]]-=1 # reduce the window freq
                if s[left] in mp1 and mp2[s[left]] < mp1[s[left]]: # OH no , we have reduced window too short
                    have-=1
                left+=1
        return res
            







