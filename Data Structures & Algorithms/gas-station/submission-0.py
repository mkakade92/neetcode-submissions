class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        

        n = len(gas)
        for st in range(n):
            

            fuel = 0
            
            ind = st

            while True:
                fuel+=(gas[ind]-cost[ind])
                if fuel<0:
                    break
                ind = (ind+1)%n
                if ind==st:
                    break
            
            if fuel>=0:
                return st
        return -1