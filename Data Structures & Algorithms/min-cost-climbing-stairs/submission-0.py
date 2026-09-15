class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def recurse(i):

            if i in memo:
                return memo[i]
            if i <= 1:

                return cost[i]
            memo[i] = min(recurse(i-1) , recurse(i-2)) + cost[i]
            return memo[i]

        return min(recurse(len(cost)-1) , recurse(len(cost)-2))

            
