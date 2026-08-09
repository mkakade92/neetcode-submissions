class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        s = 1
        e = max(piles)

        while s<e:
            mid = s+(e-s)//2

            rate = sum((p+mid-1)//mid for p in piles)

            if rate>h:
                s = mid+1  
            else:
                e = mid
        return s