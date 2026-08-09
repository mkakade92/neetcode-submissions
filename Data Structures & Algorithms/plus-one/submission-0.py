class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pw = 0

        num = 0
        for i in digits[::-1]:
            num+=(10**(pw))*i
            pw+=1
        num+=1
        return [int(d) for d in str(num)]
        

