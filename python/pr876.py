from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        runner = head

        while runner != None and runner.next != None:
            current = current.next
            runner = runner.next.next

        return current

n6 = ListNode(6)
n5 = ListNode(5, n6)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)

sol = Solution()

n = sol.middleNode(n1)

print(n.val)