class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        

        if len(intervals)==1:
            return intervals

        sorted_intervals = sorted(intervals,key=lambda x: x[0])
        print(sorted_intervals)

        i = 0

        while i < len(sorted_intervals)-1:
            inter = sorted_intervals[i]
            next_inter = sorted_intervals[i+1]

            if inter[1]>=next_inter[0]:
                sorted_intervals.pop(i)
                sorted_intervals.pop(i)
                sorted_intervals.insert(i,[inter[0],max(inter[1],next_inter[1])])
            else:
                i+=1

        return sorted_intervals