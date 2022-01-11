from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, "", 0)

    def dfs(self, node, bin_str, total):
        if node:
            bin_str += f"{node.val}"
            if node.left is None and node.right is None:
                total += int(bin_str, base=2)
                bin_str = bin_str[:len(bin_str)-1]
            else:
                total = self.dfs(node.left, bin_str, total)
                total = self.dfs(node.right, bin_str, total)

        return total