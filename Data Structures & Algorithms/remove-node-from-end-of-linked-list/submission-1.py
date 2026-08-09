# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        slow = None
        fast = head

        k = 0
        pre = None
        while fast is not None:
            fast = fast.next
            k+=1
            if k>=n:
                pre = slow
                slow = head if slow is None else slow.next
        if pre is not None:
            pre.next = slow.next
            return head
        return head.next
