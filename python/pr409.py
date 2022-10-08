class Solution:
    def longestPalindrome(self, s: str) -> int:
        map = {}
        for c in s:
            if map.get(c):
                map[c] = map[c] + 1
            else:
                map[c] = 1
                
        len = 0
        odd = False
        for k,v in map.items():
            if v % 2 == 0:
                len += v
            elif v - 1 > 0:
                len += v-1
                odd = True
            else:
                odd = True
                
        return len if not odd else len + 1
