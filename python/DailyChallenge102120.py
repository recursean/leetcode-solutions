# We are given an array asteroids of integers representing asteroids in a row.

# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        currIdx = 0
        collisions = False

        while True:
            if currIdx + 1 < len(asteroids):
                if asteroids[currIdx] > 0 and asteroids[currIdx + 1] < 0:
                    collisions = True

                    if abs(asteroids[currIdx]) > abs(asteroids[currIdx + 1]):
                        asteroids.pop(currIdx + 1)
                    elif abs(asteroids[currIdx]) < abs(asteroids[currIdx + 1]):
                        asteroids.pop(currIdx)
                    else:
                        asteroids.pop(currIdx)
                        asteroids.pop(currIdx)   
                else:                                    
                    currIdx = currIdx + 1
            else:
                if collisions:
                    collisions = False
                    currIdx = 0
                else:
                    break


        return asteroids


sol = Solution()
asteroids = [-2,-1,1,2]
print(sol.asteroidCollision(asteroids))