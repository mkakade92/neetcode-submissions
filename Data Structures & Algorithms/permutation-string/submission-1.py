class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1)>len(s2):
            return False
        if s1==s2:
            return True
        f1,f2 = [0]*26,[0]*26

        for i in range(len(s1)):
            f1[ord(s1[i])-ord('a')]+=1
            f2[ord(s2[i])-ord('a')]+=1

        
        found = 0
        for i in range(26):
            found+= (1 if f1[i]==f2[i] else 0)

        l = 0
        for r in range(len(s1),len(s2)):
            if found==26:
                return True
            
            ind = ord(s2[r])-ord('a')

            f2[ind]+=1

            if f1[ind]==f2[ind]:
                found+=1
            elif f1[ind]+1==f2[ind]:
                found-=1

            ind = ord(s2[l])-ord('a')

            f2[ind]-=1

            if f1[ind]==f2[ind]:
                found+=1
            elif f1[ind]-1==f2[ind]:
                found-=1
            l+=1
        return found==26