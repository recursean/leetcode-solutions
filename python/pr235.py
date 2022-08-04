# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
        
        # alternate solution 
        
        #self.rn = None
        #self.postOrder(root, p, q, False, False)
        #return self.rn
        
    def postOrder(self, root, p, q, pf, qf):
        pf2, qf2 = pf, qf
        if root is not None:
            pf, qf = self.postOrder(root.left, p, q, pf, qf)
            pf2, qf2 = self.postOrder(root.right, p, q, pf2, qf2)
            
            if root.val == p.val:
                pf = True
            elif root.val == q.val:
                qf = True
                
            if self.rn is None and ( (pf or pf2) and (qf or qf2) ):
                self.rn = root
            
        return (pf or pf2), (qf or qf2)
