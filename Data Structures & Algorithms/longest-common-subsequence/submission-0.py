from functools import cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @cache
        def memo(i , j):
            if i > len(text1) or j > len(text2):
                return 0
            

            if text1[i-1] == text2[j-1]:

                return 1+memo(i+1 , j+1)
            else:
                return max(memo(i+1 , j) , memo(i , j+1))


        return memo(1,1)