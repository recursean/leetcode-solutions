from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class BST:
    root = None
    list_root = None
    list_curr = None

    def insert(self, val):
        if self.root == None:
            self.root = TreeNode(val)
        else:
            self.insert_r(self.root, val)
        
    def insert_r(self, root, val):
        if val < root.val:
            if root.left == None:
                root.left = TreeNode(val)
            else:
                self.insert_r(root.left, val)
        elif val >= root.val:
            if root.right == None:
                root.right = TreeNode(val)
            else:
                self.insert_r(root.right, val)

    def inorder(self):
        self.list_curr = None
        
        self.inorder_r(self.root)
        return self.list_root

    def inorder_r(self, node):
        if node == None:
            return

        self.inorder_r(node.left)

        # visit
        if self.list_curr == None:
            self.list_curr = ListNode(node.val)
            self.list_root = self.list_curr
        else:
            self.list_curr.next = ListNode(node.val)
            self.list_curr = self.list_curr.next

        self.inorder_r(node.right)

class TreeNode:
    left = None
    right = None

    def __init__(self, val):
        self.val = val   

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        bst = BST()

        for root in lists:
            current = root

            while current != None:
                bst.insert(current.val)
                current = current.next

        return bst.inorder()

    # the following works but is too slow
    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     new_head = None

    #     while True:
    #         small_idx = -1

    #         # find the smallest node and store index
    #         for i, n in enumerate(lists):
    #             if n != None and (small_idx == -1 or n.val < lists[small_idx].val):
    #                 small_idx = i

    #         # if no index was found, all of the nodes in lists are None
    #         if small_idx == -1:
    #             return new_head

    #         # add smallest node to master merged list
    #         if new_head == None:
    #             new_head = lists[small_idx]
    #             current = new_head
    #         else:
    #             current.next = lists[small_idx]
    #             current = current.next
            
    #         # set pointer in lists to node following smallest node found
    #         lists[small_idx] = lists[small_idx].next

sol = Solution()
sol.mergeKLists([[1,4,5],[1,3,4],[2,6]])