class Solution:
    def numDecodings(self, s: str) -> int:
        
        memo = {}

        def recurse(i):
            if i in memo:
                return memo[i]

            ways = 0
            if i == len(s):
                return 1

            if s[i] != '0':
                ways += recurse(i+1)

            if i + 1 < len(s) and 10<=int(s[i:i+2])<=26:
                ways += recurse(i+2)
            memo[i] = ways
            return memo[i]

        return recurse(0)