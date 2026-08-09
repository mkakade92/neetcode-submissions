class Solution:
    def jump(self, nums: List[int]) -> int:
        
        N =  len(nums)

        mem = dict()
        def min_jumps(ind):

            if ind in mem.keys():
                return mem[ind]


            if ind >= N-1:
                mem[ind] = 0
                return mem[ind]
            

            min_jump = float('inf')

            for possible in range(1,nums[ind]+1):
                min_jump = min(min_jump, min_jumps(ind+possible))
            mem[ind] = 1+min_jump
            return mem[ind]
        
        return min_jumps(0)