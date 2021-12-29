from typing import *

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    depths = None

    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        self.inorder(root, 0)
        return root

    def inorder(self, node, depth):
        if node is None:
            return

        self.inorder(node.left, depth+1)

        if not self.depths:
            self.depths = [None] * (depth + 1)

        if self.depths[depth] is None:
            self.depths[depth] = node
        else:
            self.depths[depth].next = node
            self.depths[depth] = node

        self.inorder(node.right, depth+1)