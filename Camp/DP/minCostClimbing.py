#DP - bottom Up
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2,len(cost)):
            cost[i] = cost[i] + (min(cost[i-1],cost[i-2]))
            
            
        return min(cost[len(cost)-1],cost[len(cost)-2])
            
            
