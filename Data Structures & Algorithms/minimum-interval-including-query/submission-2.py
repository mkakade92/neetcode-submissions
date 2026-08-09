class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        

        intervals.sort()
        sortedQ = sorted(queries)
        pq = []
        # print(pq)
        res ={q:-1 for q in queries}
        ind = 0
        for q in sortedQ:
            # print(f"Finding for {q} in {intervals[ind:]}")
            while ind<len(intervals):
                if q>=intervals[ind][0]:
                    heapq.heappush(pq,[intervals[ind][1]-intervals[ind][0]+1,intervals[ind]])
                    ind+=1
                else:
                    break
            # print(pq)
            while pq:
                L,interval = heapq.heappop(pq)
                # print(f"q={q}, L={L}, interval={interval}")
                if q > interval[1]:
                    continue
                else:
                    res[q] = L
                    heapq.heappush(pq,[L,interval])
                    break
        ans = []
        # print(res)

        for q in queries:
            ans.append(res[q])
        return ans
        


                