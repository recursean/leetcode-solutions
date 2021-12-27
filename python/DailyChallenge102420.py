# You have an initial power of P, an initial score of 0, and a bag of tokens where tokens[i] is the value of the ith token (0-indexed).

# Your goal is to maximize your total score by potentially playing each token in one of two ways:

# If your current power is at least tokens[i], you may play the ith token face up, losing tokens[i] power and gaining 1 score.
# If your current score is at least 1, you may play the ith token face down, gaining tokens[i] power and losing 1 score.
# Each token may be played at most once and in any order. You do not have to play all the tokens.

# Return the largest possible score you can achieve after playing any number of tokens.

from typing import List

class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        score = 0
        power = P
        tokenPlayed = False
        turns = 0

        while True:
            min = -1
            max = -1
            tokenPlayed = False    

            for i in range(len(tokens)): 
                if power >= tokens[i] and (min == -1 or tokens[i] < tokens[min]):
                    min = i
                elif max == -1 or tokens[i] > tokens[max]:
                    max = i
            
            if min > - 1:
                score = score + 1
                power = power - tokens[min]
                tokens.pop(min)
                turns = 0 
                tokenPlayed = True

            elif max > -1 and score >= 1:
                score = score - 1
                power = power + tokens[max] 
                tokens.pop(max)
                turns = turns + 1
                tokenPlayed = True

            if not tokenPlayed:
                if turns > 0:
                    score = score + turns
                break     
   

        return score


sol = Solution()
tokens = [87,24,32]
p = 87
print(sol.bagOfTokensScore(tokens,p))