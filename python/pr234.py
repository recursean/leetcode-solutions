# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        count = 0
        curr = head
        while curr is not None:
            curr = curr.next
            count += 1
            
        curr = head
        for i in range((count+1)//2):
            curr = curr.next
            
        #reverse list
        tmp = None
        prev = None
        while curr is not None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            
        curr = prev
        curr2 = head
        
        while curr is not None:
            if curr2.val != curr.val:
                return False
            curr = curr.next
            curr2 = curr2.next
        
        return True