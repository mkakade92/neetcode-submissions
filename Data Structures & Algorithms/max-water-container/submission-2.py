class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        MAX = 0
        i  =0 
        j = n-1

        while i<j:
            MAX = max(MAX,min(heights[i],heights[j])*(j-i))
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return MAX