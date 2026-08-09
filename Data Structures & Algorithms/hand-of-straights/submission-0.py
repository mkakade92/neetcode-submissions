class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        
        if len(hand)%groupSize!=0:
            return False

        heapq.heapify(hand)
        count = Counter(hand)
        while hand:

            curr = heapq.heappop(hand)
            if count[curr]==0:
                continue
            
            for i in range(curr,curr+groupSize):
                if count.get(i,0)==0:
                    return False
                count[i]-=1
            
        return True


            