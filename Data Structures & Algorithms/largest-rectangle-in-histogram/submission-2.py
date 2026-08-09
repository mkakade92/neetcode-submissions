class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        st = []
        n = len(heights)
        maxAr = 0
        for i in range(n):
            start = i
            height = heights[i]
            while len(st)!=0 and st[-1][1]>height:
                ind,h = st.pop()
                maxAr = max(maxAr,h*(i-ind))
                start = ind
            st.append([start,height])
        
        for i in range(len(st)):
            ind,h = st[i][0],st[i][1]
            maxAr = max(maxAr,h*(n-ind))
        return maxAr


