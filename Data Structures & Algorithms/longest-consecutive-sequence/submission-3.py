class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        num_set = set(nums)

        maxlen = 0
        for i in num_set:
            if i-1 not in num_set:
                length = 1

                while i + length in num_set:

                    length += 1

                maxlen = max(maxlen  , length)
        return maxlen
        