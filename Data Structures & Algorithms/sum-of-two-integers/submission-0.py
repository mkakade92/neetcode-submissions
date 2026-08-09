class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        res = 0
        carry  =0
        mask = 0XFFFFFFFF


        for i in range(32):

            b1 = (a>>i)&1
            b2 = (b>>i)&1

            curr = b1^b2^carry
            carry = (b1+b2+carry)>=2

            if curr:
                res |= (1<<i)
        if res>0X7FFFFFFF:
            res = ~(res ^ mask)
        return res