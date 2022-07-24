# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a_count = 1
        b_count = 1
        
        curr_a = headA
        while curr_a.next is not None:
            a_count += 1
            curr_a = curr_a.next
            
        curr_b = headB
        while curr_b.next is not None:
            b_count += 1
            curr_b = curr_b.next
            
        if curr_a == curr_b:
            curr_a = headA
            curr_b = headB
            if a_count > b_count:
                for i in range(a_count - b_count):
                    curr_a = curr_a.next
            elif a_count < b_count:
                for i in range(b_count - a_count):
                    curr_b = curr_b.next
                    
            while curr_a != curr_b:
                curr_a = curr_a.next
                curr_b = curr_b.next
                
            return curr_a
        else:
            return None