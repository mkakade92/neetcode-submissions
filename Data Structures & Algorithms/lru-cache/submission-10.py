class Node:
    def __init__(self,entry,next):
        self.entry = entry
        self.next = next

def printList(head):
    curr = head
    while curr:
        print(curr.entry,"->",end="")
        curr = curr.next
    print("\n")


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        

    def get(self, key: int) -> int:
        if self.head is None:
            return -1
        
        if self.head.entry[0]==key:
            return self.head.entry[1]
        
        curr = self.head
        pre = None
        while curr:
            if curr.entry[0]== key:
                pre.next = curr.next
                curr.next = self.head
                self.head = curr
                printList(self.head)
                return curr.entry[1]
            pre = curr
            curr = curr.next
        printList(self.head)
        return -1
        

    def put(self, key: int, value: int) -> None:
        if self.head == None:
            self.head = Node([key,value],None)
        if self.capacity==1:
            self.head.entry = [key,value]
            return
        else:        
            curr = self.head
            remaining = self.capacity
            pre = None
            while curr:
                if curr.entry[0]==key:
                    curr.entry[1] = value
                    if pre is not None:          # only needs moving if it's not already the head
                        pre.next = curr.next
                        curr.next = self.head
                        self.head = curr
                    printList(self.head)
                    return
                pre = curr
                curr = curr.next
                remaining-=1
            if remaining==0:
                curr = self.head
                while curr.next.next:
                    curr = curr.next
                curr.next = None
            temp = Node([key,value],None)
            temp.next = self.head
            self.head = temp
        printList(self.head)
        return




        
        
        
