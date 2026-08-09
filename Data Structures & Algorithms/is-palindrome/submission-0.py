class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        newS = ""
        smallR = range(ord('a'),ord('z')+1)
        capR = range(ord('A'),ord('Z')+1)
        numR = range(ord('0'),ord('9')+1);
        for c in s:
            if ord(c) not in smallR and ord(c) not in capR and ord(c) not in numR:
                continue
            newS+=c
        newS = newS.lower()
        l = 0
        r = len(newS)-1
        while l<=r:
            if newS[l]!=newS[r]:
                return False
            l+=1
            r-=1
        return True