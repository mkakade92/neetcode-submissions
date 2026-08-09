class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        

        n = len(nums)
        res= nums[0]

        MIN,MAX = 1,1

        for num in nums:
            temp = MAX*num

            MAX = max(num*MAX,num*MIN,num)
            MIN = min(temp,num*MIN,num)
            res=  max(res,MAX)
        return res