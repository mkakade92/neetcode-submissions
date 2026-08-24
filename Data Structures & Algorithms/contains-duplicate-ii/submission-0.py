class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        

        w =set()

        l = 0

        for r in range(len(nums)):

            if r-l>k:
                w.remove(nums[l])
                l+=1
            
            if nums[r] in w:
                return True
            w.add(nums[r])
        return False