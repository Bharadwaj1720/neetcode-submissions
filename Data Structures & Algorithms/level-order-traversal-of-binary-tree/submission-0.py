# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.dic={}
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.l(root,0)
        ans=[]
        for k, v in self.dic.items():
            ans.append(v)
        return ans


    def l(self,root,dept):
        if root is not None:
            if dept in self.dic:
                self.dic[dept].append(root.val)
            else:
                self.dic[dept]=[root.val]
            self.l(root.left,dept+1)
            self.l(root.right,dept+1)
        