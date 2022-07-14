from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = 10001
        ans = 0
        for price in prices:
            if price < min:
                min = price
            else:
                ans = max(ans,price-min)
        return ans

sol = Solution()
# prices = [7,1,5,3,6,4]
# prices = [7,6,4,3,1]
prices = [8,16,1,17]
print(sol.maxProfit(prices))