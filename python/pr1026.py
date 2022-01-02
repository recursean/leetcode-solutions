from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # modified BFS. queue both current and parent node in order to 
    # have a dict of node->parent. when visiting each node, calculate
    # difference to every ancestor node
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        q = deque()
        # node_id -> parent node_id
        parents = {}
        # node_id -> node obj
        nodes = {}
        maxval = -1
        node_id = 0
        current_id = node_id
        
        if root:
            nodes[node_id] = root

        current = root
        while current:
            if current.left:
                q.append(current.left) 
                q.append(node_id + 1)   # current.left node id
                q.append(current_id)    # parent node id
                node_id += 1

            if current.right:
                q.append(current.right) 
                q.append(node_id + 1)   # current.right node id
                q.append(current_id)    # parent node id
                node_id += 1

            parent_id = parents.get(current_id)
            while parent_id is not None:
                parent = nodes[parent_id]
                maxval = (abs(parent.val - current.val) 
                          if abs(parent.val - current.val) > maxval 
                          else maxval)
                
                parent_id = parents.get(parent_id)

            if q:
                current = q.popleft()
                current_id = q.popleft()
                nodes[current_id] = current
                parents[current_id] = q.popleft()
            else:
                break

        return maxval
            