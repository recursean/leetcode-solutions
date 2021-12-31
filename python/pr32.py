from typing import *
from collections import deque

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_depth = 0
        curr_depth = 0
        wf_count = 0
        wf = False

        for c in s:
            if c == '(':
                curr_depth += 1
            else:
                if curr_depth >= 1:
                    wf_count += 1
                    max_depth = wf_count if wf_count > max_depth else max_depth
                    curr_depth -= 1
                    wf = True
                else:
                    wf = False
            
            if curr_depth == 0 and not wf:
                wf_count = 0
                

        return max_depth * 2

sol = Solution()
s = ""
print(sol.longestValidParentheses(s))