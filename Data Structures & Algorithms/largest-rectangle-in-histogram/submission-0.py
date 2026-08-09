class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        maxRect = 0
        for i in range(0,len(heights)):
            height = heights[i]
            w = 1
            for bar in range(i-1,-1,-1):
                if heights[bar]>=heights[i]:
                    w+=1
                else:
                    break
            for bar in range(i+1,len(heights)):
                if heights[bar]>=heights[i]:
                    w+=1
                else:
                    break
            # print(f"{height},{w} : {(w*height)}")
            maxRect = max(w*height,maxRect)
        return maxRect

        