class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def cycleExist(ind,visited,st,graph):
            
            if ind in st:
                return True

            if ind in visited:
                return False
            
            visited.add(ind)
            st.add(ind)

            for neighbor in graph[ind]:
                if cycleExist(neighbor,visited,st,graph):
                    return True
            
            st.remove(ind)
            return False


        graph = {}
        for i in range(numCourses):
            graph[i] = []

        for src,dest in prerequisites:
            graph[src].append(dest)
        
        print(graph)

        st = set()
        visit = set()
        for i in graph.keys():
            if i not in visit and cycleExist(i,visit,st,graph):
                return False
        
        return True

        