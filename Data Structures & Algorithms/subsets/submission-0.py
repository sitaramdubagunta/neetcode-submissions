class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        def recurse(i , remaining):
            nonlocal ans

            if i == len(nums):
                ans.append(remaining.copy())

                return 

            
            recurse(i+1 , remaining)
            remaining.append(nums[i])

            
            recurse(i+1 , remaining)
            remaining.pop()

        recurse(0 , [])

        return ans
