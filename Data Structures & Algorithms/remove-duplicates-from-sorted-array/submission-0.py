class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0

        k=1

        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                continue
            nums[k]=nums[i]
            k+=1
        return k