class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ans = [0, 0, 0]
        for t in triplets:
            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
                ans[0] = max(ans[0], t[0])
                ans[1] = max(ans[1], t[1])
                ans[2] = max(ans[2], t[2])
        return ans == target
            




    