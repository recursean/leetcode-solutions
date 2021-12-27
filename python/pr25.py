from typing import Optional
from collections import deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        newHead = None
        prev = None
        ctr = 0
        stack = deque()

        if head == None:
            return None
            
        while True:
            # loop to kth position
            while ctr < k-1 and current.next != None:
                stack.append(current)
                current = current.next

                ctr += 1
            
            if ctr != k-1:
                return newHead
            
            # save next node of new root of sublist 
            tmp = current.next

            # set new head node
            if newHead == None:
                newHead = current
            else:
                prev.next = current

            # reverse stacked nodes
            while len(stack) != 0:
                current.next = stack.pop()
                current = current.next

            current.next = tmp

            if current.next == None:
                return newHead

            # save previous to point to next sublist
            prev = current

            # next root of sublist to reverse
            current = current.next

            ctr = 0

        return newHead

n4 = ListNode(4)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)

sol = Solution()
k = 3

n = sol.reverseKGroup(n1, k)

while(n != None):
    print(n.val, '->')
    n = n.next