class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        


        s1counter = Counter(s1)


        left = 0
        if (s1counter == Counter(s2[0:len(s1)])):
            return True
        
        for right in range(len(s1)-1, len(s2)):



            if right - left + 1 == len(s1):

                if s1counter  == Counter(s2[left:right+1]):
                    return True

            left += 1

        return False