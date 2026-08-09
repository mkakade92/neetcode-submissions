class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = [0]*26

        for k in s:
            a[ord(k)-ord('a')]+=1
        
        for k in t:
            a[ord(k)-ord('a')]-=1
        
        for k in a:
            if k!=0:
                return False
        return True