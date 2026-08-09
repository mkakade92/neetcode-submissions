class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #store results
        res = []

        #check anagram
        def check(str1,str2):

            cc = [0]*26 #store character counts

            for c in str1:
                cc[ord(c)-ord('a')]+=1
            
            for c in str2:
                cc[ord(c)-ord('a')]-=1
            
            for count in cc:
                if count !=0:
                    return False
            return True
        

        for s in strs:
            foundAPlace = False
            for l in res:
                if check(s,l[0])==True:
                    l.append(s)
                    foundAPlace=True
                    break
            if not foundAPlace:
                res.append([s])
        return res
            
            