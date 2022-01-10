class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(f"{int(a, base=2) + int(b, base=2):b}")

sol = Solution()
a = "1010"
b = "1011"
print(sol.addBinary(a,b))