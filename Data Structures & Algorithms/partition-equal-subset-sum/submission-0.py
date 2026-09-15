class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums)%2 != 0:
            return False
        memo = {}
        def recurse(i , target):

            if (i,target) in memo:
                return memo[(i,target)]
            if target == 0:

                return True

            if i >= len(nums) or target < 0:
                return False

            
            take = recurse(i+1 , target - nums[i])
            skip = recurse(i+1 , target)
            memo[(i,target)]  = take or skip
            return memo[(i,target)]

        return recurse(0,sum(nums)//2)