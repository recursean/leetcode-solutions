from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        l1 = self.inorder(root1, [])
        l2 = self.inorder(root2, [])
        
        left, right = 0, 0
        ans = []
        
        while True:
            if left < len(l1) and right < len(l2):
                if l1[left] < l2[right]:
                    ans.append(l1[left])
                    left += 1
                else:
                    ans.append(l2[right])
                    right += 1
            elif left < len(l1):
                ans.append(l1[left])
                left += 1
            elif right < len(l2):
                ans.append(l2[right])
                right += 1
            else:
                break
        
        return ans
                
        
    def inorder(self, root: TreeNode, nodes):
        if root is None:
            return nodes
        nodes = self.inorder(root.left, nodes)
        nodes.append(root.val)
        nodes = self.inorder(root.right, nodes)
        
        return nodes