from typing import *

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot, pivot_idx = self.find_pivot(nums)

        low = pivot_idx
        high = pivot_idx - 1

        # binary search through rotated array for target
        while low != high:
            # if current sublist we are searching contains the rotated
            # part, we need to adjust the low and high values to reflect
            # the indexes they would be in the unrotated array
            adj_low = low if low < high else low - pivot_idx
            adj_high = high if low < high else high + pivot

            mid = low + (adj_high - adj_low) // 2
            print(f"{low} - {mid} - {high}")
            # if mid pushes past the end of the array, wrap around
            # to the front of the array
            if mid > len(nums) - 1:
                mid = mid - low - 1

            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                high = mid
            elif target > nums[mid]:
                low = mid

        return -1

    def find_pivot(self, nums):
        low = 0
        high = len(nums) - 1

        while True:
            mid = low + (high - low) // 2

            if nums[low] < nums[mid]:
                low = mid
            else:
                if mid != 0 and nums[mid] < nums[mid - 1]:
                    return len(nums) - mid + 1, mid
                else:
                    high = mid

sol = Solution()
nums = [4,5,6,7,0,1,2]
target = 0

print(sol.search(nums, target))