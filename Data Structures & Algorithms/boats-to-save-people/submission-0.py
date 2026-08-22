class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        b = 0

        l = 0
        r = len(people) - 1

        while l<=r:

            rem = limit - people[r]

            b+=1

            r-=1

            if l<=r and rem >= people[l]:
                l+=1
        
        return b