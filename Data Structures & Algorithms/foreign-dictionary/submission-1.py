class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        if len(words)==0:
            return ""
        if len(words)==1:
            return words[0]      


        graph = {}

        def add_edge(u,v=None):
            if u not in graph.keys():
                graph[u] = []
            
            if v:
                if v not in graph.keys():
                    graph[v] =[]
                if v not in graph[u]:
                    graph[u].append(v)

        
        def check_second_rule(smaller,larger):
            s , l = 0, 0
            while s < len(smaller) and smaller[s]==larger[l]:
                s+=1
                l+=1
            return s == len(smaller)
        

        def find_edge(w1,w2):

            s, l = 0,0

            # we don't have to worry about index error in find_edge because w2 is not a substring
            # so it won't be possible for l to exhaust before s even if s> l

            while s<len(w1) and w1[s]==w2[l]:
                s+=1
                l+=1
            
            if s<len(w1):
                # edge between w1[s] and w2[l]
                add_edge(w1[s],w2[l])

        
        def check_rules(w1,w2):
            # First lets add all letter to graph
            for w in w1:
                add_edge(w)
            for w in w2:
                add_edge(w)

            if len(w1) <= len(w2):
                # now add edge between first differing letter
                find_edge(w1,w2)
            else:
                if check_second_rule(w2,w1):
                    return False
                find_edge(w1,w2)
            return True
                    


        for i in range(len(words)-1):

            if not check_rules(words[i],words[i+1]):
                return ""
        

        q = deque()

        inDeg ={u:0 for u in graph.keys()}

        for u in graph.keys():
            for v in graph[u]:
                inDeg[v] +=1
        
        
        for u in graph.keys():
            if inDeg[u]==0:
                q.append(u)
        
        res = []

        visited= 0

        while q:

            u = q.popleft()
            visited+=1

            for v in graph[u]:
                inDeg[v]-=1
                if inDeg[v]==0:
                    q.append(v)
            res.append(u)
        
        if visited != len(graph.keys()):
            return ""
        return "".join(res)




            



