# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        


        h1,h2 = l1,l2

        carry = 0
        res = None
        head = res
    

        while h1 or h2 or carry>0:
            num = carry
            if h1:
                num+=h1.val
                h1 = h1.next
            if h2:
                num+=h2.val
                h2 = h2.next
            carry = num//10

            num = num%10

            if not res:
                res = ListNode(num)
                head = res
            else:
                res.next =ListNode(num)
                res=  res.next
        return head


