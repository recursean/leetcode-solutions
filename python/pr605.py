from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
            
        p = True
        for i,f in enumerate(flowerbed):
            if f == 0:
                if p:
                    if i == len(flowerbed)-1 or flowerbed[i+1] == 0:
                        n -= 1
                        if n == 0:
                            return True

                        p = False
                else:
                    p = True
            else:
                p = False

        return n == 0        

sol = Solution()
flowerbed = [0,0,1,0,0]
n = 1
print(sol.canPlaceFlowers(flowerbed,n))