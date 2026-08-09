class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        s = set()
        
        trip = sorted(triplets,key=lambda x:x[0])
        nxt  = []
        # print(trip)
        for ind,x in enumerate(trip):
            if x[0]<=target[0]:
                nxt.append(x)
        # print(nxt)
        trip = sorted(nxt,key = lambda x: x[1])
        nxt = []
        # print(trip)
        for ind,x in enumerate(trip):
            if x[1]<=target[1]:
                nxt.append(x)
        # print(nxt)
        trip = sorted(nxt,key = lambda x: x[2])
        nxt = []
        # print(trip)
        for ind,x in enumerate(trip):
            if x[2]<=target[2]:
                nxt.append(x)
        # print(nxt)
        

        ans=[-1,-1,-1]

        for i in nxt:
            ans[0] = max(ans[0],i[0])
            ans[1] = max(ans[1],i[1])
            ans[2] = max(ans[2],i[2])
        
        return ans==target
            




    