# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size=0
        p=head
        while p is not None:
            size+=1
            p=p.next
        n=size-n+1
        
        p=head
        q=None
        if n==1:
            return head.next
        for i in range(1,n):
            q=p
            p=p.next
        
        q.next=p.next
        return head
        
        

        