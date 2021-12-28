from typing import Optional
from collections import deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        k = 2
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

    def swapPairsConstantMem(self, head: Optional[ListNode]) -> Optional[ListNode]:
        k = 2
        current = head
        newHead = None
        prev = None
        ctr = 0
        stack = deque()

        if head == None:
            return None
            
        while True:
            # loop to kth position
            while current.next != None:
                # swap current and next
                tmp = current

                current = current.next
                tmp.next = current.next
                current.next = tmp

                if newHead == None:
                    newHead = current

                # next root of sublist
                current = current.next

            if current.next == None:
                return newHead
 
        return newHead        

n4 = ListNode(4)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)

sol = Solution()

# n = sol.swapPairs(n1)
n = sol.swapPairsConstantMem(n1)

while(n != None):
    print(n.val, '->')
    n = n.next