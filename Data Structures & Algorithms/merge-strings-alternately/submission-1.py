class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        j = 0

        newstr = ''
        for i in range(len(word1)):
            
            newstr+=word1[i]
            if len(word2) > j:
                newstr+=word2[j]
                j += 1

        while j < len(word2):

            newstr += word2[j]
            j += 1
        return newstr
            