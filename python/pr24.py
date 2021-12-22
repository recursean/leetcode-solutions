# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = None
        curr = head

        while not curr.next == None:
            next = curr.next
            curr.next = curr.next.next
            next.next = curr

            if newHead == None:
                newHead = next

        return newHead