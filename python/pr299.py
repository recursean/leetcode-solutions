class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        vset = {}
        idxs = {}
        
        for i,s in enumerate(secret):
            idxs[i] = s
            if s in vset:
                vset[s] += 1
            else:
                vset[s] = 1
            
        bulls = 0
        cows = 0
        for i,g in enumerate(guess):
            if idxs[i] == g:
                bulls += 1
                vset[g] -= 1
        for i,g in enumerate(guess):
            if g in vset and idxs[i] != g and vset[g] > 0:
                cows += 1
                vset[g] -= 1
        
        return f'{bulls}A{cows}B'
