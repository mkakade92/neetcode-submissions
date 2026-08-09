class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += str(len(s))+"#"+s
        return ans


    def decode(self, s: str) -> List[str]:
        n =len(s)
        res = []
        i=0
        while i<n:
            j = i
            while s[j]!="#":
                j+=1
            num = int(s[i:j])
            i=j+1
            j=i+num
            res.append(s[i:j])
            i=j
            
        return res

