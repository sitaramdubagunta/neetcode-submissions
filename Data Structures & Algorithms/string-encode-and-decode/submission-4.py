class Solution:

    def encode(self, strs: List[str]) -> str:

        res =""

        for string in strs:


            res += f'{len(string)}#{string}'

        return res
        

    def decode(self, s: str) -> List[str]:


        i = 0
        word = []
        while(i < len(s)):
            length = 0
            j = i

            while(s[j] != '#'):
                j += 1

            length = int(s[i:j])

            word.append(s[j+1 : j+1+ length])

            i = j + 1 +length
        return word
       
