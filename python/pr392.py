class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        if not s:
            return True
        elif not t:
            return False
        for c in s:
            if i >= len(t):
                return False
            while t[i] != c:
                i += 1
                if i >= len(t):
                    return False
            i += 1
        return True
