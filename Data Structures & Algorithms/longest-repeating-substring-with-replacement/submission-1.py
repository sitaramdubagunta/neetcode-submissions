class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        max_freq = 0

        freq = defaultdict(int)
        ans = 0
        left = 0

        for right in range(len(s)):

            freq[s[right]] += 1


            max_freq = max(max_freq , freq[s[right]])


            while abs(max_freq - (right-left+1)) > k:

                if freq[s[left]] == 0:
                    del freq[s[left]]


                freq[s[left]] -= 1
                left += 1

            
            ans = max(ans , right-left+1)
        return ans
