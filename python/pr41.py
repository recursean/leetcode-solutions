from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if nums:
            pos = [0] * len(nums)

            for num in nums:
                if num > 0 and num <= len(pos):
                    pos[num-1] = 1

            for i,p in enumerate(pos):
                if p == 0:
                    return i+1
            
            # every number from 1-len(pos) was found
            return len(pos)+1

        return 1

sol = Solution()
# nums = [1,2,0]
# nums = [3,4,-1,1]
# nums = [7,8,9,11,12]
print(sol.firstMissingPositive(nums))