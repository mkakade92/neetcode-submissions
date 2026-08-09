class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()


        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr[:])
                return
            
            if i>=len(candidates) or total>target:
                return
            
            currElem = candidates[i]  # select the curr element
            curr.append(currElem)
            dfs(i+1,curr,total+currElem) # same element cannot be select twice
            curr.pop()
            while i+1 < len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1,curr, total) # recurse without selecting the currElem
        
        dfs(0,[],0)
        return res