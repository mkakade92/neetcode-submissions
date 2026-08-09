class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums.sort()
        d = {}

        for n in nums:
            if n in d.keys():
                continue
            if n-1 not in d.keys():
                d[n]  =[n]

            else:
                d[n-1].append(n)
                d[n] = d[n-1]
                del d[n-1]
        l = 0
        for k,v in d.items():
            if len(v)>l:
                l = len(v)
        return l