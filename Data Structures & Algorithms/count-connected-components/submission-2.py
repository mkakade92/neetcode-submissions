class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        


        graph = {}

        for i in range(n):
            graph[i] = []
        
        for s,d in edges:
            graph[s].append(d)
            graph[d].append(s)


        def dfs(ind,visited,graph):

            st =[]
            st.append(ind)

            while st:

                curr = st.pop()
                visited.add(curr)

                for x in graph[curr]:
                    if x not in visited:
                        st.append(x)

        visited=set()
        cnt = 0
        for i in range(n):
            if i not in visited:
                dfs(i,visited,graph)
                cnt+=1
        return cnt
            