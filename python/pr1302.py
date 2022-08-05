# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = [root, 0]
        max = -1
        sum = 0
        
        while q:
            curr = q.pop(0)
            i = q.pop(0)
            
            if i > max:
                sum = curr.val
                max = i
            elif i == max:
                sum += curr.val
                
            if curr.left:
                q.append(curr.left)
                q.append(i+1)
            if curr.right:
                q.append(curr.right)
                q.append(i+1)
                
        return sum
