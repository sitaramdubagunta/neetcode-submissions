class Solution:
    def minWindow(self, s: str, t: str) -> str:
        


        subcount  = Counter(t)

        need = 0
        have = len(subcount)

        count = defaultdict(int)
        maxans = float('inf')
        l1 , r1 = 0 , 0
        left = 0
        for right in range(len(s)):
            count[s[right]] += 1
            if s[right] in subcount and count[s[right]] == subcount[s[right]]:

                need += 1
                

            

            while have == need:

                if right-left+1 <maxans:
        
                    maxans = min(maxans , right-left+1)
                    l1,r1 = left  , right
                count[s[left]] -= 1
                if count[s[left]] < subcount[s[left]]:
                    need -= 1

                if left and count[s[left]] == 0:
                    
                    del count[s[left]]

                left += 1

                
        return "" if maxans == float('inf') else  s[l1:r1+1]
                    
