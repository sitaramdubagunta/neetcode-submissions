class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
        ans = []
        used = [False]*len(nums)
        def dfs(current , used):

            nonlocal ans
            if len(current) == len(nums):

                ans.append(current.copy())

                return

            


            for i in range(len(nums)):

                if used[i]:
                    continue

                
                used[i] = True
                current.append(nums[i])

                dfs(current , used)

                used[i] = False
                current.pop()
        dfs([] , used )
        return ans