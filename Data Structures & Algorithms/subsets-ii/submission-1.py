class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        

        nums.sort()

        res = []

        def dfs(ind,curr):

            res.append(curr[:])
            for i in range(ind,len(nums)):
                if i>ind and nums[i]==nums[i-1]:
                    continue
            
                curr.append(nums[i])
                dfs(i+1,curr)
                curr.pop()
        dfs(0,[])
        return res