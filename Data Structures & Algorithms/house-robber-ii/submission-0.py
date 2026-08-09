class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums)
        a = nums[0]
        b = max(nums[0],nums[1])

        linearSoln1 = 0
        linearSoln2 = 0 

        for i in range(2,n-1):
            temp = max(nums[i]+a,b)
            a = b
            b = temp
        linearSoln1 = b

        a = nums[1]
        b = max(nums[1],nums[2])

        for i in range(3,n):
            temp = max(nums[i]+a,b)
            a = b
            b = temp
        linearSoln2 = b

        return max(linearSoln1,linearSoln2)
        