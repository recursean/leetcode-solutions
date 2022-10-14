# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        runner = head
        curr = head
        prev = None
        
        while runner and runner.next:
            prev = curr
            curr = curr.next
            runner = runner.next.next
            
        if prev:
            prev.next = curr.next
        else:
            head = None
        
        return head
