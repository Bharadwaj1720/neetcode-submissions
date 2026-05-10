# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        p=head
        q=head
        r=None
        if head==None or head.next==None or head.next.next==None:
            return 
        while q!=None:
            if q.next==None:
                break
            r=p
            p=p.next
            q=q.next.next
        r.next=None
        q=p.next
        p.next=None
        while q!=None:
            t=q.next
            q.next=p
            p=q
            q=t
        qq=None
        while head!=None and p!=None:
            t=head.next
            tt=p.next
            head.next=p
            p.next=t
            qq=p
            head=t
            p=tt
        if p is not None:
            qq.next=p
            p.next=None
        

        