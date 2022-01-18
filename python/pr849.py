from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        left = 0
        ans = 0
        found_one = False

        for i,n in enumerate(seats):
            if n == 1:
                if found_one:
                    seat = (i-left) // 2
                else:
                    # left will be 0
                    seat = i - left
                    found_one = True

                ans = max(ans, seat)
                left = i

        return max(ans, i-left)     

sol = Solution()
seats = [1,0,0,0,1,0,1] #2
# seats = [1,0,0,0] #3
# seats = [0,1] #1
# seats = [1,0] #1
# seats = [0,0,1] #2
# seats  = [1,0,0,1] #1
print(sol.maxDistToClosest(seats))