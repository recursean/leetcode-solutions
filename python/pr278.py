# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        mid = (r - l) // 2
        
        while l <= r:
            if isBadVersion(mid):
                if not isBadVersion(mid-1):
                    return mid
                
                r = mid - 1
            
            else:
                l = mid + 1
                
            mid = (r - l) // 2 + l
            
                
