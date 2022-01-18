import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        right = int(math.sqrt(c))

        for n in range(right + 1):
            sum = n**2 + right**2

            if sum == c:
                return True

            if n == right:
                return False

            if sum > c:
                right -= 1

        return False

sol = Solution()
c = 0
print(sol.judgeSquareSum(c))