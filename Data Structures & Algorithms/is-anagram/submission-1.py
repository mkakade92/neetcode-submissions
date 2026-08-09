class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = [0]*26
        for i in s:
            freq[ord(i)-ord('a')]+=1
        for i in t:
            ind = ord(i)-ord('a')
            freq[ind]-=1

        for k in freq:
            if k!=0:
                return False
        return True