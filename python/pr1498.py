from typing import List

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        ans = 0
        right = len(nums) - 1
        m = (10 ** 9 + 7)

        nums.sort()
        for i,n in enumerate(nums):
            if n + n <= target:
                while i <= right and n + nums[right] > target:
                    right -= 1
                if i <= right:
                    ans += pow(2, right - i, m)
            else:
                break

        return ans % m

sol = Solution()
# nums = [3,5,6,7]
# target = 9
nums = [2,3,3,4,6,7]
target = 12
print(sol.numSubseq(nums,target))