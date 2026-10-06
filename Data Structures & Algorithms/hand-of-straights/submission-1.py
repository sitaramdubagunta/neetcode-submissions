class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        

        count = Counter(hand)
        sorted_keys = sorted(count.keys())


        for i in sorted_keys:


            if not count[i]:
                continue
            need = count[i]

            for j in range(groupSize):

                if need > count[j+i]:
                    return False

                count[i+j] -= need
        return True 


