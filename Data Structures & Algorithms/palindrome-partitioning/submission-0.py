class Solution:
    def partition(self, s: str) -> List[List[str]]:
        

        res = []
        def isPalin(s):
            return s[:]==s[::-1]
        

        def dfs(ind,curr):

            if ind>=len(s):
                res.append(curr[:])
                return
            
            for i in range(ind,len(s)):
                if isPalin(s[ind:i+1]):
                    curr.append(s[ind:i+1])
                    dfs(i+1,curr)
                    curr.pop()
        dfs(0,[])
        return res
