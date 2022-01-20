from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # to find min speed, bin search through range (1, max(piles))
        left = 1
        right = max(piles)

        while left < right:
            mid = left + (right-left) // 2

            if self.valid_k(mid, h, piles):
                right = mid
            else:
                left = mid + 1

        return right


    def valid_k(self, k, h, piles):
        for i,p in enumerate(piles):
            h -= math.ceil(p / k)

            if h < 0:
                return False
            
        return True


sol = Solution()
# piles = [3,6,7,11] #4
# h = 8
# piles = [30,11,23,4,20] #30
# h = 5
# piles = [30,11,23,4,20] #23
# h = 6
piles = [312884470]
h = 312884469 
print(sol.minEatingSpeed(piles, h))