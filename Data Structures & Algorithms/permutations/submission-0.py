class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        def backtrack(currentarr , remaining):

            if not remaining:
                result.append(currentarr.copy())

            
            for i in range(len(remaining)):

                current = remaining[i]


                backtrack([current] + currentarr , remaining[:i]  + remaining[i+1:])
        backtrack([] , nums)
        return result

