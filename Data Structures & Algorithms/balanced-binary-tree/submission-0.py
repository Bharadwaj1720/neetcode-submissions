# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        s=k(root)
        if s<0:
            return False
        return True
        
        
        
def k(root):
    if root==None:
        return 0
    h1=k(root.right)
    h2=k(root.left)
    if abs(h1-h2)>1:
        return -1000
    else:
        return max(h1,h2)+1