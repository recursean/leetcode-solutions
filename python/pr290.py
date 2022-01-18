class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()

        if len(pattern) != len(s):
            return False
        
        d = {}
        for i,p in enumerate(pattern):
            if d.get(p):
                if d[p] != s[i]:
                    return False
            else:
                d[p] = s[i]

        return True

sol = Solution()
pattern = "abba"
s = "dog cat cat dog"
print(sol.wordPattern(pattern,s))