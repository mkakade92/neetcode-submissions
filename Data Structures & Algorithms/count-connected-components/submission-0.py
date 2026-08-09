class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        


        graph ={}
        for i in range(n):
            graph[i] = []
    
        for src,dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)

        
        visited =set()

        def dfs(ind,visited,graph):
            
            st = []
            st.append(ind)
            visited.add(ind)
            while st:

                curr = st.pop()
                visited.add(curr)
                
                for x in graph[curr]:
                    if x not in visited:
                        st.append(x)
            
            return
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i,visited,graph)
                count+=1
        return count

