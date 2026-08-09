class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        

        MAX_SUM  = nums[0]

        curr = nums[0]

        for i in nums[1:]:
            curr = max(curr+i,i)
            MAX_SUM = max(curr,MAX_SUM)
        return MAX_SUM
