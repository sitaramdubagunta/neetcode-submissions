class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        array = [0]*n

        prefix = 1
        for i in range(n):
            array[i] = prefix
            prefix *= nums[i]


        suffix = 1

        for j in range(len(nums)-1 , -1 , -1):

            array[j] *= suffix
            suffix *= nums[j]

        return array
