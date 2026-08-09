class CountSquares:

    def __init__(self):
        self.p = []
        self.mp = defaultdict(int)

    def add(self, point: List[int]) -> None:

        self.p.append(point)

        self.mp[tuple(point)]+=1     

    def count(self, point: List[int]) -> int:

        res= 0
        px,py  = point

        for x,y in self.p:
            if (abs(px-x)!=abs(py-y)) or px==x or py==y:
                continue
            res+=self.mp[(x,py)]*self.mp[(px,y)]
        return res
        
