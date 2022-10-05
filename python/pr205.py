class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        smap = {}
        used = [0] * 128
        for i in range(len(s)):
            repl = smap.get(s[i])
            if repl:
                if repl != t[i]:
                    return False
            elif used[ord(t[i]) % 128] == 1:
                return False
            else:
                smap[s[i]] = t[i]
                used[ord(t[i]) % 128] = 1
                
        return True
