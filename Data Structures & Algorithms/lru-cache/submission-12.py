class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None

def printList(head):
    curr = head
    while curr:
        print(curr.entry,"->",end="")
        curr = curr.next
    print("\n")


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache ={}

        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.pre = self.head
    
    def remove(self,node):
        node.pre.next=  node.next
        node.next.pre = node.pre
    
    def addToFront(self,node):
        node.next = self.head.next
        node.pre = self.head
        self.head.next.pre = node
        self.head.next = node


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node =self.cache[key]
        self.remove(node)
        self.addToFront(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove(node)
            self.addToFront(node)
            return
        
        if len(self.cache)>=self.capacity:
            lru = self.tail.pre
            self.remove(lru)
            del self.cache[lru.key]
        
        node = Node(key,value)
        self.cache[key] = node
        self.addToFront(node)




        
        
        
