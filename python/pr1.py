from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        
        for i,n in enumerate(nums):
            if d.get(target-n) is not None:
                return [i, d[target-n]]
            d[n] = i