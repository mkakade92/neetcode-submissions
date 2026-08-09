class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m,n = len(matrix),len(matrix[0])

        a = [0]*(m*n)

        k = 0
        for i in range(m):
            for j in range(n):
                a[k] = matrix[i][j]
                k+=1
        
        def bin_search(mat,target):
            
            s = 0
            e = len(mat) - 1

            while s<=e:
                mid = s + (e-s)//2

                if mat[mid]==target:
                    return True
                elif mat[mid]>target:
                    e = mid-1
                else:
                    s=mid+1
            return False
        
        return bin_search(a,target)
