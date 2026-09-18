class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        

        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i>=len(nums):
                return 0

            best = 1
            for j in range(i):

                if nums[j] < nums[i]:

                    best = max(best , dfs(j)+1)
            memo[i] = best
            return memo[i]

        return max([dfs(i) for i in range(len(nums))])


