class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        nums.sort()

        exp = 1

        for num in nums:
            if num>0 and exp==num:
                exp+=1
        return exp