from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        left, right = 0, len(arr)-1
        for _ in range(len(arr)-1):
            if arr[left] < arr[left+1]:
                left += 1
            if arr[right] < arr[right-1]:
                right -= 1

            if left > right:
                return False
                
        return left == right if left != 0 and left != len(arr)-1 else False

sol = Solution()
# arr = [0,3,2,1]
arr = [3,5,5]
# arr = [2,1]
# arr = [1,2,3,1,2]
# arr = [0,1,2,3,4,8,9,10,11,12,11]
# arr = [0,1,2,3,4,5,6,7,8,9]
print(sol.validMountainArray(arr))