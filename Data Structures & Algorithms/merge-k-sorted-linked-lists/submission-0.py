# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists or len(lists)==0:
            return None
        return self.divide(lists,0,len(lists)-1)

    def divide(self, lists, l, r):
        if l>r:
            return None
        if l==r:
            return lists[l]
        
        mid = l+ (r-l)//2
        left  = self.divide(lists,l,mid)
        right = self.divide(lists,mid+1, r)

        curr = ListNode(0)
        head = curr;

        while left and right:
            if left.val<=right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        
        if left:
            curr.next = left
        if right:
            curr.next = right
        return head.next
            
