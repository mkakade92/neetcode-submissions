class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        

        canReach= [[False]*len(heights[0]) for _ in range(len(heights))]

        print(canReach)

        def dfs(i,j):
            st = []


            st.append((i,j))


            visited =set()

            pacific = False
            atlantic = False
            while st:

                r,c = st.pop()

                if r==0 or c==0:
                    pacific=True
                if r==len(heights)-1 or c==len(heights[0])-1:
                    atlantic=True
                
                if pacific and atlantic:
                    return True
                

                visited.add(f"{r},{c}")


                for x,y in [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]:
                    
                    if f"{x},{y}" not in visited and x>=0 and y>=0 and x<len(heights) and y<len(heights[0]) and heights[x][y]<=heights[r][c]:
                        if canReach[x][y]:
                            canReach[r][c] = True
                            canReach[i][j] = True
                            return True
                        st.append((x,y))
            
            return False

        res= []

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if dfs(i,j):
                    canReach[i][j] = True
                    res.append([i,j])
        return res


        