from typing import *

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        ht = {}

        for trip in trips:
            for i in range(trip[1], trip[2]):
                if ht.get(i):
                    ht[i] += trip[0]
                else:
                    ht[i] = trip[0]

                if ht.get(i) > capacity:
                    return False

        return True

sol = Solution()

trips = [[2,1,5],[3,5,7]]
capacity = 3

print(sol.carPooling(trips, capacity))