class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        ans =[]
        def dfs(start , path , remaining):
            nonlocal ans
            
            if remaining == 0:
                ans.append(path.copy())
                return
            
            if remaining < 0:
                return
            for i in range(start , len(nums)):

                path.append(nums[i])
                dfs(i , path , remaining - nums[i])
                path.pop()
        dfs(0 , [] , target)
        return ans
        