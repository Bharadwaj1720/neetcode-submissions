"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from copy import deepcopy
class Solution:
    def __init__(self):
        self.nodes=set()
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node==None:
            return
        cnode=deepcopy(node)
        self.nodes.add(cnode.val)
        for i in cnode.neighbors:
            if i.val not in self.nodes:
                self.cloneGraph(i)
        return cnode
        