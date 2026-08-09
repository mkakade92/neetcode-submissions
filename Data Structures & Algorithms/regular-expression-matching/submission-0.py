class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n,m = len(s),len(p)
        mp  =[[None]*(m+1) for _ in range(n+1)]
        def recur(i,j):

            if mp[i][j] is not None:
                return mp[i][j]

            if j==m:
                mp[i][j] = (i==n)
                return mp[i][j]
            
            mat = i<len(s) and (s[i]==p[j] or p[j]=='.')

            if j+1<len(p) and p[j+1]=='*':

                mp[i][j] =  recur(i,j+2) or (mat and recur(i+1,j))
            else:
                mp[i][j] = mat and recur(i+1,j+1)
            return mp[i][j]

        return recur(0,0)