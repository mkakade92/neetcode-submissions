class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        

        visited=set()
        st = set()
        graph  = {}
        for i in range(numCourses):
            graph[i] = []

        for src,dest in prerequisites:
            graph[src].append(dest)

        ans = []

        def cycleExist(ind,visited,st,graph,ans):

            if ind in st:
                return True
            
            if ind in visited:
                return False

            visited.add(ind)
            st.add(ind)

            for neighbor in graph[ind]:
                if cycleExist(neighbor,visited,st,graph,ans):
                    return True
            
            st.remove(ind)
            ans.append(ind)
            return False


        Ce = False
        for i in range(numCourses):
            if i not in visited:
                if cycleExist(i,visited,st,graph,ans):
                    return []
        return ans
            


