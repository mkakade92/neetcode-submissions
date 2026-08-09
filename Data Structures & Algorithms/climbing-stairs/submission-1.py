class Solution:
    def climbStairs(self, n: int) -> int:
        

        a = 1
        b = 1

        for _ in range(2,n+1):
            temp = a+b
            a = b
            b= temp
        return b