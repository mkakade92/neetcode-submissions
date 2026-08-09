class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        res =[]


        def recurse(currCombo,ind,target):
            if ind>=len(nums):
                return
            if target>0:
                currCombo.append(nums[ind])
                recurse(currCombo,ind,target-nums[ind])
                currCombo.pop()
                recurse(currCombo,ind+1,target)
            elif target==0:
                res.append(currCombo[:])
            else:
                recurse(currCombo,ind+1,target)

            
        recurse([],0,target)

        return res

            
            