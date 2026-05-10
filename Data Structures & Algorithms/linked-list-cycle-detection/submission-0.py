# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p=head
        if p is None:
            return False
        q=head.next
        while p is not None and q is not None:
            if p==q:
                return True
            p=p.next
            if q.next==None:
                return False
            q=q.next.next
        return False
        