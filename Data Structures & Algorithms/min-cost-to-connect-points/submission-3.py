class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        

        V = len(points)
        dist = [float('inf')]*V
        dist[0] = 0
        mst = set()

        def minDist():

            minD = float('inf')
            minInd = -1
            for ind in range(V):
                if dist[ind] < minD and ind not in mst:
                    minD = dist[ind]
                    minInd = ind
            return minInd
        
        res = 0
        for _ in range(V):

            u = minDist()
            mst.add(u)
            res+=dist[u]

            for ind in range(V):
                W = abs(points[ind][0]-points[u][0])+abs(points[ind][1]-points[u][1])
                if ind!=u and ind not in mst and dist[ind] > W:
                        dist[ind] = W
        return res

        