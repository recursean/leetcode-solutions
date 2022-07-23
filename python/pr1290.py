# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        self.getDecimalValueR(head)
        return self.total
    
    def getDecimalValueR(self, head: ListNode) -> int:
        if head.next is None:
            self.total = head.val
            return 1
        else:
            pos = self.getDecimalValueR(head.next)
            if head.val == 1:
                self.total = self.total + 2**pos
            return pos + 1