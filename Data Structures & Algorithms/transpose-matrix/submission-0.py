class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        

        row,col = len(matrix),len(matrix[0])

        res = []

        for c in range(col):
            cl = []
            for r in range(row):
                cl.append(matrix[r][c])
            res.append(cl)
        return res