# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p=list1
        q=list2
        if p==None and q==None:
            return None
        r=ListNode()
        rr=r
        while p is not None and q is not None:
            if p.val>q.val:
                r.val=q.val
                q=q.next
            else:
                r.val=p.val
                p=p.next
            r.next=ListNode()
            r=r.next
        if p is None:
            while q.next is not None:
                r.val=q.val
                r.next=ListNode()
                r=r.next
                q=q.next
        elif q is None:
            while p.next is not None:
                r.val=p.val
                r.next=ListNode()
                r=r.next
                p=p.next
        if q==None:
            r.val=p.val
            r.next=None
        else:
            r.val=q.val
            r.next=None
        return rr


                


        