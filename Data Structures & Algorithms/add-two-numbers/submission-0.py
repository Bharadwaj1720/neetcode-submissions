# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p=l1
        q=l2
        r=ListNode((p.val+q.val)%10,None)
        head=r
        carry=(p.val+q.val)//10
        p=p.next
        q=q.next
        while p is not None and q is not None:
            val=(p.val+q.val+carry)%10
            carry=(p.val+q.val+carry)//10
            temp=ListNode(val,None)
            p=p.next
            q=q.next
            r.next=temp
            r=temp
        if p is None:
            while q is not None:
                val=(q.val+carry)%10
                carry=(q.val+carry)//10
                temp=ListNode(val,None)
                q=q.next
                r.next=temp
                r=temp
        elif q is None:
            while p is not None:
                val=(p.val+carry)%10
                carry=(p.val+carry)//10
                temp=ListNode(val,None)
                p=p.next
                r.next=temp
                r=temp
        if carry!=0:
            r.next=ListNode(carry,None)
        return head
