class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        

        mp = {}
        n = len(nums)
        res =[]
        for num in nums:
            mp[num] = mp.get(num,0)+1

        for k,v in mp.items():
            if v>n//3:
                res.append(k)
        return res
        