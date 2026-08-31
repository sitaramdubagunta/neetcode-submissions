class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        left = 0

        freq = defaultdict(int)
        max_freq = 0
        ans = 0
        for right in range(len(s)):

            freq[s[right]] += 1
            
            max_freq = max(max_freq , freq[s[right]])

            while (right-left+1) - max_freq > k:


                freq[s[left]] -= 1
                if freq[s[left]] == 0:

                    del freq[s[left]]
                left += 1
            ans = max(ans , right-left+1)
        return ans
            
