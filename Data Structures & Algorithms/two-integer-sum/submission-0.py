class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        a   = {}
        for ind,val in enumerate(nums):
            if val in a.keys():
               return [a[val],ind] 
            else:
                a[target-val] = ind
        return []