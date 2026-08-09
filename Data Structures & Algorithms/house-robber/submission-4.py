class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        dp = [0]*n
        a = nums[0]
        b = max(nums[0],nums[1])

        for i in range(2,n):
            temp = max(nums[i]+a,b)
            a = b
            b = temp
        return b
        