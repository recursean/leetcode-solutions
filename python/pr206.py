# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        self.reverseListR(head)
        head.next = None
        return self.actual_head
    
    def reverseListR(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            self.actual_head = head
        else:
            self.reverseListR(head.next).next = head
        return head