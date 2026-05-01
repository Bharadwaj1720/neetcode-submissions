# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.maxi=0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameterOfBinaryTreeo(root)
        return self.maxi
    def diameterOfBinaryTreeo(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return -1
        left=self.diameterOfBinaryTreeo(root.left)
        right=self.diameterOfBinaryTreeo(root.right)
        k=left+right+2
        if self.maxi<k:
            self.maxi=k
        return max(left,right)+1


        