class Solution:
    def minimumMoves(self, s: str) -> int:
        flips = 0
        i = 0

        while i < len(s):
            if s[i] == "X":
                flips += 1
                i += 3
            else:
                i += 1

        return flips

sol = Solution()
s = "OOXOOOXXO"
print(sol.minimumMoves(s))