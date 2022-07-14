from typing import List
import math

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        nums.sort()

        # for max XOR pair, we need to maximize number of 1s turned on in
        # binary number. the bigger number out of the pair needs to have the 1
        # bit on in the highest bit position possible. 
        max_bin_len = math.ceil(math.log(nums[len(nums)-1], 2))

        i = 0
        while math.ceil(math.log(nums[i], 2)) < max_bin_len