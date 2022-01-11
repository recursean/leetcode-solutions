from typing import List
from collections import deque

class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        floor = 0
        lefts = deque()

        for i,h in enumerate(height):
            # 0-height walls can not start or end water traps
            if h == 0:
                floor = 0
                continue

            # if we havent encountered a left wall yet, append it to list
            if len(lefts) == 0:
                lefts.append(i)

            # if most recent left is bigger than current wall, append it to lst
            elif height[lefts[len(lefts)-1]] > h:
                water += (i - lefts[len(lefts)-1] - 1) * \
                         (h - floor)
                lefts.append(i)

            # if most recent left is smaller than current, possible trap end
            else:
                while len(lefts) > 0 and height[lefts[len(lefts)-1]] <= h:
                    left = lefts.pop()

                    # width x height
                    water += (i - left - 1) * (height[left] - floor)
                    floor = height[left]

                if len(lefts) == 0:
                    floor = 0
                else:
                    if h > floor:
                        water += (i - lefts[len(lefts)-1] - 1) * \
                            (h - floor)
                
                lefts.append(i)

        return water

sol = Solution()
# height = [4,2,0,3,2,5]
# height = [5,4,1,2]
height = [0,1,0,2,1,0,1,3,2,1,2,1]
# height = [0,1,2,0,3,0,1,2,0,0,4,2,1,2,5,0,1,2,0,2]

print(sol.trap(height))










#      * 
# *~~~~*
# *~~*~*
# **~***
# **~***

# *
# **
# ** 
# ** *
# ****
#               *
#           *~~~*
#     *~~~~~*~~~*
#   *~*~~*~~**~**~~*~*
#  **~*~**~~*****~**~* 
# 0123456789