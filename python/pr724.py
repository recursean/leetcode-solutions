class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum = 0
        for num in nums:
            sum = sum + num
        leftsum = 0
        for i,num in enumerate(nums):
            if leftsum == sum - leftsum - num:
                return i 
            leftsum += num
                
        return -1 
