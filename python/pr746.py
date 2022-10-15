class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mem = {
            len(cost)-1: cost[len(cost)-1], 
            len(cost)-2: cost[len(cost)-2]
        }
        
        for i in range(len(cost)-1):
            idx = len(cost) - 3 - i
            mem[idx] = cost[idx] + min(mem[idx+1], mem[idx+2])
            
        return min(mem[0], mem[1])
