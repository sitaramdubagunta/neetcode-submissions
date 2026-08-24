class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        


        left = 1

        right = max(piles)
        ans = 0
        
        while left <= right:

            mid = left + (right - left) // 2


            sum1 = sum([math.ceil(pile/mid) for pile in piles])


            if sum1 > h:
                
                left = mid +1
            else:
                ans = mid
                right = mid-1
        return ans
        
            
