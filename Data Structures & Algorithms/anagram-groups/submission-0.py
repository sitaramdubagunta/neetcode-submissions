class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        dt1 = defaultdict(list)


        for str1 in strs:
            
            dt1["".join(sorted(str1))].append(str1)


        return [  j  for i , j in dt1.items()]
