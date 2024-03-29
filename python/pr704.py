class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        mid = (r - l) // 2
        
        while l <= r:
            if nums[mid] == target:
                return mid

            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
                
            mid = (r - l) // 2 + l
                
        return -1
