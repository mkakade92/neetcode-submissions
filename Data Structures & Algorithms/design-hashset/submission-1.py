class MyHashSet:

    def __init__(self):
        

        self.arr = []

    def add(self, key: int) -> None:

        if not self.contains(key):
            self.arr.append(key)
        

    def remove(self, key: int) -> None:
        ind = -1
        for i in range(len(self.arr)):
            if self.arr[i]==key:
                ind= i
        if ind!=-1:
            self.arr  =self.arr[:ind]+self.arr[ind+1:]
        
        

    def contains(self, key: int) -> bool:

        for num in self.arr:
            if num==key:
                return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)