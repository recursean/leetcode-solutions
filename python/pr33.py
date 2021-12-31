from typing import *

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot, pivot_idx = self.find_pivot(nums)
        # print(f"pivot: {pivot}:{pivot_idx}")
        low = pivot_idx if pivot_idx >= 0 else 0
        high = pivot_idx - 1 if pivot_idx >= 0 else len(nums) - 1

        # binary search through rotated array for target
        while True:
            # if current sublist we are searching contains the rotated
            # part, we need to adjust the low and high values to reflect
            # the indexes they would be in the unrotated array
            adj_low = low if low <= high else low - pivot_idx
            adj_high = high if low <= high else high + pivot - 1

            if adj_high < adj_low:
                break

            mid = low + (adj_high - adj_low) // 2
            # if mid pushes past the end of the array, wrap around
            # to the front of the array
            if mid > len(nums) - 1:
                # (mid - low) tells how many steps to take from low to get 
                # to mid
                # (len(nums) - low) tells how many steps we need to take to get
                # from low to the end of the array
                # subtracting these tells how many steps off the front of the
                # rotated array we need to take to get to mid
                mid = (mid - low) - (len(nums) - low)

            #print(f"{low}:{mid}:{high}")
            #print(f"{adj_low}:{mid}:{adj_high}(adj)")

            if target == nums[mid]:
                return mid
            else:
                if target < nums[mid]:
                    high = mid #- 1
                elif target > nums[mid]:
                    low = mid + 1

            if adj_high == adj_low:
                break

        return -1

    def find_pivot(self, nums):
        low = 0
        high = len(nums) - 1

        # is array unrotated?
        if nums[high] > nums[low]:
            return -1,-1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[low] < nums[mid]:
                low = mid #+ 1
            else:
                if mid == 0:
                    if len(nums) > 1 and nums[mid + 1] < nums[mid]:
                        return len(nums) - mid, mid + 1
                    else:
                        break

                if nums[mid] < nums[mid - 1]:
                    return len(nums) - mid + 1, mid
                elif mid < len(nums) and nums[mid] > nums[mid + 1]:
                    return len(nums) - mid, mid + 1
                else:
                    high = mid

            if low == high:
                break

        return -1,-1

sol = Solution()
nums = [5,6,1,2,3,4]
# nums = [3,1]
# nums = [4,5,6,7,0,1,2]
# nums = [1]
# nums = [1,3,5]
nums = [3,5,1]
target = 1
print(sol.search(nums, target))