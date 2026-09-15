class Solution:
    
    def rob(self, nums: List[int]) -> int:
        memo = {}


        def recursive(i):

            if i >= len(nums):

                return 0
            if i in memo:
                return memo[i]

            take = nums[i] + recursive(i+2) 
            skip = recursive(i+1)
            memo[i] = max(take,skip)
            return memo[i]

        return recursive(0)


        