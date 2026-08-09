class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxL = [0]*n
        maxL[0] = height[0]
        maxR = [0]*n
        maxR[-1] = height[-1]
        for i in range(1,n):
            maxL[i] =max(maxL[i-1],height[i])
        for i in range(n-2,0,-1):
            maxR[i] = max(maxR[i+1],height[i])
        
        MAX = 0
        # print(f"maxL={maxL}")
        # print(f"maxR={maxR}")
        for i in range(n):
            # print(f"wheight={min(maxL[i],maxR[i])-height[i]}")
            MAX+=max(0,min(maxL[i],maxR[i])-height[i])
        return MAX

