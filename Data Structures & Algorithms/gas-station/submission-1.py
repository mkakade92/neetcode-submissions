class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        curr = 0
        total = 0
        ST = 0
        n = len(gas)
        for st in range(n):
            

            curr +=(gas[st]-cost[st])
            total +=(gas[st]-cost[st])

            if curr <0:
                ST = (st+1)%n
                curr=0

        return -1 if total<0 else ST