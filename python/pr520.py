class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        fc = False
        fm = False
        for i,c in enumerate(word):
            if c == c.upper():
                if i == 0:
                    fc = True
                elif not fc:
                    return False
                else:
                    fm = True
            else:
                if fm:
                    return False
                fc = False
        return True

sol = Solution()
word = "Leetcode"
print(sol.detectCapitalUse(word))