# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        

        def getKth(curr,k):
            while curr and k>0:
                curr = curr.next
                k-=1
            return curr
        dummy = ListNode(-1,head)

        groupPre = dummy

        while True:

            kth = getKth(groupPre,k)

            if not kth:
                break
            
            groupNext = kth.next
            pre , curr = kth.next, groupPre.next
            while curr!=groupNext:
                temp = curr.next
                curr.next = pre
                pre = curr
                curr =temp
            
            temp = groupPre.next
            groupPre.next = kth
            groupPre = temp
        return dummy.next

