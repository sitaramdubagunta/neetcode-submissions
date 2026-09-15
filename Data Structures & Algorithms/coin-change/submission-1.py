class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}

        def recursive(coins , remaining):

            if remaining == 0:
                return 0
            best = float('inf')
            if remaining in memo:
                return memo[remaining]
            for coin in coins:

                if remaining-coin >= 0:


                    best = min(best ,  1+recursive(coins,remaining-coin))

            memo[remaining] = best
            return best
        ans = recursive(coins,amount)
        return ans if ans != float('inf') else -1