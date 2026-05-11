# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot==None and root==None:
            return True
        if (root==None and subRoot!=None) or (root!=None and subRoot==None):
            return False 
        return self.compare(root,subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)



    def compare(self,root,sub):
        if sub==None and root==None:
            return True
        if (root==None and sub!=None) or (root!=None and sub==None):
            return False
        if root.val!=sub.val:
            return False
        return self.compare(root.left,sub.left) and self.compare(root.right,sub.right)
        