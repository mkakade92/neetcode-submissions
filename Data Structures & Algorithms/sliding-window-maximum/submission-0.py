class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        for e in range(k,len(nums)+1):
            res.append(max(nums[e-k:e]))
        return res
