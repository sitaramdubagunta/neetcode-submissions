class Solution:
    def countBits(self, n: int) -> List[int]:
        

        ans = []
        for i in range(n+1):

            count  = 0
            tmp = i
            while tmp:

                if tmp & 1 == 1:

                    count += 1
                
                tmp >>= 1
            ans.append(count)

        return ans

                

        