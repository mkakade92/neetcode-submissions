# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
    
        l = 0
        temp = head
        while temp is not None:
            l+=1
            temp =  temp.next
        
        if l<=2:
            return
        
        mid = l//2 if l % 2==0 else l//2+1

        l1 = head

        l2 = None

        tL = 0
        temp = head
        pre = None
        while tL != mid:
            tL+=1
            pre = temp
            temp = temp.next
        
        pre.next = None #cut of first part
        l2 = temp
        pre = None

        # reverse second part
        while temp is not None:
            nxt = temp.next
            temp.next = pre
            pre = temp
            temp = nxt
        
        l2 = pre # put l2 to head of reversed list

        k = 0
        temp = l1
        while l2 is not None:
            next_l1 = l1.next
            next_l2 = l2.next
            l1.next = l2
            l2.next = next_l1
            l1 = next_l1
            l2 = next_l2            





        


            