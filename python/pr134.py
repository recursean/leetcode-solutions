class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        surplus = 0
        tank = 0
        start = 0
        
        for i in range(len(gas)):
            surplus += gas[i] - cost[i]
            tank += gas [i] - cost[i]
            
            if tank < 0:
                tank = 0
                start = i + 1
                
        return start if surplus >= 0 else -1