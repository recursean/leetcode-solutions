from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans = set()
        for i in range(0,len(nums)-2):
            left = i+1
            right = len(nums) - 1
            
            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if sum == 0:
                    ans.add((nums[i], nums[left], nums[right]))
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    right -= 1

        return [list(x) for x in ans]

sol = Solution()
nums = [-1,0,1,2,-1,-4]
print(sol.threeSum(nums))