class Solution:
    def jump(self, nums: List[int]) -> int:
        
        N =  len(nums)
        farthest = 0
        edge = 0
        jumps = 0
        for i in range(N-1):
            if edge>=N-1:
                return jumps
            farthest = max(farthest,i+nums[i])
            if i==edge:
                jumps+=1
                edge = farthest 
        
        return jumps