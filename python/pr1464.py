class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        x = -1
        y = -1
        for num in nums:
            if x == -1:
                x = num
            elif y == -1:
                y = num
            else:
                if num > x or num > y:
                    if num > x and x < y:
                        x = num
                    else:
                        y = num
                        
        return (x-1) * (y-1)
