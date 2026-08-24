class FreqStack:

    def __init__(self):
        

        self.st =[]
        self.mp ={}
        self.time = 0

    def push(self, val: int) -> None:
        self.time+=1
        self.mp[val] = self.mp.get(val,0)+1
        heapq.heappush(self.st,[-self.mp[val],-self.time,val])
        
        

    def pop(self) -> int:

        while self.st:

            freq,ti,val = heapq.heappop(self.st)

            if self.mp[val] and self.mp[val] != -freq:
                continue
            
            if self.mp[val] and self.mp[val]>0:
                self.mp[val]-=1
            
            return val
        

            
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()