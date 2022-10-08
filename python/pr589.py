"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.ret = []
        self.dfs(root)
        return self.ret
    
    def dfs(self, root):
        if root:
            self.ret.append(root.val)
            for child in root.children:
                self.dfs(child)
