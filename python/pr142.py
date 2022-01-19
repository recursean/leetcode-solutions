from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # to detect a loop in a linked list, use a runner
        # after k steps, slow will be at k and fast will be at 2k
        # if slow and fast collide, loop start is when head and collision meet
        try:
            slow = head.next
            runner = head.next.next
            while slow != runner:
                slow = slow.next
                runner = runner.next.next
        except:
            return None

        if slow == runner:
            while head != slow:
                head = head.next
                slow = slow.next

            return head


sol = Solution()
n = ListNode(1)
n1 = ListNode(2)
n.next = n1
n1.next = n
print(sol.detectCycle(n).val)