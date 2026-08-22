class MyHashMap:

    def __init__(self):
        
        self.arr = []

    def put(self, key: int, value: int) -> None:

        for ind in range(len(self.arr)):
            k,v = self.arr[ind]
            if k==key:
                self.arr[ind][1] = value
                return
        self.arr.append([key,value])
        
        

    def get(self, key: int) -> int:
        for k,v in self.arr:
            if k==key:
                return v
        return -1
        

    def remove(self, key: int) -> None:
        for ind in range(len(self.arr)):
            k,v = self.arr[ind]

            if k==key:
                self.arr = self.arr[:ind]+self.arr[ind+1:]
                return
        return 
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)