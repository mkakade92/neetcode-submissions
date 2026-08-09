class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        

        intervals.sort()
        sortedQ = sorted(queries)
        pq = []
        # print(pq)
        res ={q:-1 for q in queries}
        for q in sortedQ:
            for interval in intervals:
                if q>=interval[0]:
                    heapq.heappush(pq,[interval[1]-interval[0]+1,interval])
            while pq:
                L,interval = heapq.heappop(pq)
                # print(f"q={q}, L={L}, interval={interval}")
                if q not in range(interval[0],interval[1]+1):
                    continue
                else:
                    res[q] = L
                    break
        ans = []
        # print(res)

        for q in queries:
            ans.append(res[q])
        return ans
        


                