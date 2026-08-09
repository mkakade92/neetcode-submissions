class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        

        if len(edges)<n-1 or len(edges)>=n:
            return False
        

        st = []
        graph = {}
        for i in range(n):
            graph[i] = []

        for src,dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
        
        st.append(0)

        visited=set()

        while st:

            curr = st.pop()

            visited.add(curr)


            for x in graph[curr]:
                if x not in visited:
                    st.append(x)
        
        return len(visited)==n
