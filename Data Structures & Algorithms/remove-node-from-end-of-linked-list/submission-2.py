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
        while fast is not None:
            fast = fast.next
            k+=1
            if k>n:
                pre = slow
                slow = head if slow is None else slow.next
        if slow is not None:
            slow.next = slow.next.next
            return head
        return head.next
