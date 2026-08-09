class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        

        S = 0

        if len(num2)>len(num1):
            num1, num2 = num2, num1
        

        first = True
        pos=-1
        for c in num2[::-1]:
            pos+=1
            carry = 0
            pr = 0
            pw = 0
            for d in num1[::-1]:
                P = (ord(c)-ord('0'))*(ord(d)-ord('0'))*(10**pw)
                pr += P
                pw+=1
                # print(f"{c}*{d} : P={P} pr = {pr}")
            if first:
                first=False
                S=pr
            else:
                S+=pr*(10**pos)
            # print(S)
        
        return str(S)
