from typing import *

class Solution:
    def checkString(self, s: str) -> bool:
        foundB = False
        foundA = False

        for c in s:
            if c == 'a':
                if foundB:
                    return False

                foundA = True
                
            elif c == 'b':
                foundB = True

        return True

sol = Solution()
s = "ba"

print(sol.checkString(s))