from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # dict {x:set(i)}
        # set of popped balloons
        # for each balloon in dict
        # if every balloon is unpopped, add to popped and increase counter
        # if atleast one baloon is popped, the rest are also, add to popped
        
        d = {}
        p = set()
        arrows = 0
        for i, point in enumerate(points):
            for k in range(point[0], point[1]+1):
                if d.get(k):
                    d[k].add(i)
                else:
                    d[k] = {i}
                    
        for x, bals in d.items():
            popped = False
            for bal in bals:
                if bal in p:
                    popped = True
                else:
                    p.add(bal)
                    
            if not popped:
                arrows += 1
                
        return arrows

sol = Solution()
points = [[10,16],[2,8],[1,6],[7,12]]
print(sol.findMinArrowShots(points))