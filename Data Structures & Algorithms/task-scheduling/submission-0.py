class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
    
        count = Counter(tasks)
        heap = [cnt for cnt in count.values()]
        heapq.heapify_max(heap)

        q = deque()

        time= 0

        while heap or q:
            time+=1
            if heap:
                cnt = heapq.heappop_max(heap)-1
                if cnt:
                    q.append([cnt,time+n])
            if q and q[0][1]==time:
                elem,_ = q.popleft()
                heapq.heappush_max(heap,elem)
        
        return time


        