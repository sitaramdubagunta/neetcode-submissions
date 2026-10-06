class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        left = 1
        right = max(piles)

        ans = 0
        while left<=right:

            mid = (left+right)//2

            est = sum([math.ceil(pile/mid) for pile in piles])


            if est <= h:
                ans = mid
                right = mid-1
            else:
                
                left = mid+1
        return ans
