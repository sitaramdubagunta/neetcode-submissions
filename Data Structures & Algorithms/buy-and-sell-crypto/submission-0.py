class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mini = prices[0]

        ans = 0
        for price in prices:
            ans = max(ans , price - mini)
            if price < mini:
                mini = price
                
           
        return ans
                