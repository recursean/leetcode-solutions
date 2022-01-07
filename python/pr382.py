from typing import *
from random import Random
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    

    def __init__(self, head: Optional[ListNode]):
        self.r = Random()
        self.r.seed()

        self.nodes = []
        
        while head:
            self.nodes.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return self.nodes[int(self.r.random() * len(self.nodes))]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()