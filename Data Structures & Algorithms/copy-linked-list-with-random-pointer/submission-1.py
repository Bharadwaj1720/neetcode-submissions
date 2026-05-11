"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dic={}
        if head is None:
            return head
        headn=Node(head.val,head.next,head.random)
        p=head.next
        q=headn
        dic[head]=headn
        while p!=None:
            temp=Node(p.val,p.next,p.random)
            dic[p]=temp
            q.next=temp
            p=p.next
            q=q.next
        p=headn
       
        while p is not None:
            if p.random!=None:
                
                p.random=dic[p.random]
            p=p.next
        return headn
        
        