class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        


        data = {}
        heap = []

        for point in points:

            dist = math.sqrt(point[0]**2 + point[1]**2)

            heap.append([dist,point])
        

        heapq.heapify(heap)

        res = []

        kLargest = heapq.nsmallest(k,heap)

        for entry in kLargest:
            res.append(entry[1])
        return res

            

