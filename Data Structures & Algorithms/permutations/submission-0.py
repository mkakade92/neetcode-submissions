class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        res =[]

        def dfs(ind):

            if ind==len(nums):
                res.append(nums[:])
                return

            for i in range(ind,len(nums)):
                nums[i],nums[ind] = nums[ind],nums[i]
                dfs(ind+1)
                nums[i], nums[ind] = nums[ind],nums[i]
        dfs(0)
        return res
            