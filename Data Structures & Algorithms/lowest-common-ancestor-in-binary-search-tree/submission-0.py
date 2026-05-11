# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ansp=[]
        self.ansq=[]
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.searchp(root,p)
        self.searchq(root,q)
        for i in self.ansp:
            if i in self.ansq:
                return i
    
    def searchp(self,root,p):
        if root==None:
            return False
        if root.val==p.val:
            self.ansp.append(root)
            return True

        k1=self.searchp(root.left,p)
        k2=self.searchp(root.right,p)
        if k1 or k2:
            self.ansp.append(root)
            return True
        return False

    def searchq(self,root,p):
        if root==None:
            return False
        if root.val==p.val:
            self.ansq.append(root)
            return True
        k1=self.searchq(root.left,p)
        k2=self.searchq(root.right,p)
        if k1 or k2:
            self.ansq.append(root)
            return True
        return False

        