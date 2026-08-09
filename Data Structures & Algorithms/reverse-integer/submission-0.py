class Solution:
    def reverse(self, x: int) -> int:
        

        pos  = x>0
        x = abs(x)
        res = 0
        while x:

            res = (res*10)+ x%10

            x = x//10
        
        if res < -(1<<31) or res > (1<<31)-1:
            return 0
        return res if pos else -res