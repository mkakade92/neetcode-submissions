class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        


        r  = len(matrix)
        c = len(matrix[0])

        res = []
        istart,iend = 0,r
        cstart,cend = 0,c 
        while len(res)<(r*c):
            i=istart
            for j in range(cstart,cend):
                res.append(matrix[i][j])
            j=cend-1
            for i in range(istart+1,iend):
                res.append(matrix[i][j])
            if istart!=iend-1:
                i=iend-1
                for j in range(cend-2,cstart-1,-1):
                    res.append(matrix[i][j])
            if cstart!=cend-1:
                j=cstart
                for i in range(iend-2,istart,-1):
                    res.append(matrix[i][j])
            istart+=1
            cstart+=1
            iend-=1
            cend-=1
            
            print(res)

        return res


