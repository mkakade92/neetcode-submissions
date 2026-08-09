# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        st = []

        temp = head

        l = 0

        while temp is not None:
            l+=1
            temp= temp.next
        
        pre = None
        temp = head

        k = 0
        while k != l - n:
            k+=1
            pre = temp
            temp = temp.next
        
        if pre is not None:
            pre.next = temp.next
            return head
        return head.next
        
