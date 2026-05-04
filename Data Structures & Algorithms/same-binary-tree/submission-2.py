# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.ans1=[]
        self.ans2=[]
        self.inOrder1(p,1)
        self.inOrder2(q,1)
        if self.ans1==self.ans2:
            return True
        return False




    def inOrder1(self,root,dept):
        if root!=None:
            self.inOrder1(root.left,dept+1)
            self.ans1.append(str(root.val)+str(dept))
            self.inOrder1(root.right,dept+1)
        else:
            self.ans1.append('null'+str(dept))
    def inOrder2(self,root,dept):
        if root!=None:
            self.inOrder2(root.left,dept+1)
            self.ans2.append(str(root.val)+str(dept))
            self.inOrder2(root.right,dept+1)
        else:
            self.ans2.append('null'+str(dept))

        