class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        

        freq = defaultdict(int)
        count = Counter(s1)

        left = 0
        for right in range(len(s2)):


            freq[s2[right]] += 1


            while right-left+1 > len(s1):

                freq[s2[left]] -= 1
                
                if freq[s2[left]] == 0:

                    del freq[s2[left]]

                left += 1


            if right-left + 1 == len(s1):

                if freq == count:

                    return True

        return False

