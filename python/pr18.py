from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        ans = set()
        for i in range(0,len(nums)-3):
            for j in range(i+1,len(nums)-2):
                left = j+1
                right = len(nums) - 1
                
                while left < right:
                    sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if sum == target:
                        ans.add((nums[i], nums[j], nums[left], nums[right]))
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif sum < target:
                        left += 1
                    else:
                        right -= 1

        return [list(x) for x in ans]

sol = Solution()
nums = [-3,-1,0,2,4,5]
target = 2
print(sol.fourSum(nums,target))