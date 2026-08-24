class Solution:
    def isHappy(self, n: int) -> bool:





        seen = set()
        sum1 = 0
        def sumofsquares(n):
            sum1 = 0
            while n > 0:
                sum1 += (n % 10)**2
                n = n // 10 
            return sum1
        

        while sum1 != 1:

            sum1 = sumofsquares(n)
            
            if sum1 in seen:
                return False
            seen.add(sum1)
            n = sum1
        
        return True



            
        