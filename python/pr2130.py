# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        vals = []
        curr = head
        runner = head
        while runner is not None:
            vals.append(curr.val)
            curr = curr.next
            runner = runner.next.next
            
        sum = -1
        i = 0
        while curr is not None:
            csum = curr.val + vals[len(vals) - i - 1]
            sum = sum if sum >= csum else csum
            i += 1
            curr = curr.next
        return sum
