class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        

        for i in range(1,len(nums)+1):
            ind = abs(nums[i-1])-1
            if nums[ind] < 0:
                return abs(nums[i-1])
            nums[ind]*=-1
        return -1
