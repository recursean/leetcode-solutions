from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: p[1])

        arrow, arrows = 0, 0
        for start,end in points:
            if arrows == 0 or start > arrow:
                arrows += 1
                arrow = end
                
        return arrows

sol = Solution()
points = [[10,16],[2,8],[1,6],[7,12]]
print(sol.findMinArrowShots(points))