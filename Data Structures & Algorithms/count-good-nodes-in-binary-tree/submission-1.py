# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ans=0
    def goodNodes(self, root: TreeNode) -> int:
        self.l(root,-10000000)
        return self.ans

    def l(self,root,maxi):
        if root is not None:
            if root.val>=maxi:
                self.ans+=1
                maxi=root.val
            self.l(root.left,maxi)
            self.l(root.right,maxi)

        