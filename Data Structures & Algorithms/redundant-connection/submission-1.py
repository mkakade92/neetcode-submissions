class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        

        graph= {}
        n = len(edges)

        for i in range(1,n+1):
            graph[i] = []
        
        for src,dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
        
        visited=[False]*(n+1)
        cycle = set()
        st = -1

        def cycleExist(node,parent):
            nonlocal st
            if visited[node]:
                st = node
                return True
            visited[node] = True 
            for x in graph[node]:
                if x== parent:
                    continue
                if cycleExist(x,node):
                    if st!=-1:
                        cycle.add(node)
                    if node==st:
                        st=-1
                    return True
            return False    

        cycleExist(1,-1)

        for u,v in edges[::-1]:
            if u in cycle and v in cycle:
                return [u,v]
        
        return []

        
