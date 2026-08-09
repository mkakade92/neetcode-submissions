class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftPrd = [1]*n
        leftPrd[0] = nums[0]
        rightPrd = [1]*n
        rightPrd[-1] =nums[-1]
        for i in range(1,n):
            leftPrd[i] = leftPrd[i-1]*nums[i]
        for i in range(n-2,-1,-1):
            rightPrd[i] = rightPrd[i+1]*nums[i]   

        ans = [1]*n
        for i in range(n):
            if i==0:
                ans[i] = rightPrd[i+1]
                continue
            if i>0 and i<n-1:
                ans[i] = leftPrd[i-1]*rightPrd[i+1]
            if i==n-1:
                ans[i] = leftPrd[i-1]
        return ans