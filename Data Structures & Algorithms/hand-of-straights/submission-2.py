class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        


        count = Counter(hand)


        sorted_keys = sorted(count.keys())

       
        for key in sorted_keys:


            needed = count[key]
            if not needed:
                continue

            for j in range(key , key+groupSize):

                if needed > count[j]:
                    return False

                count[j] -= needed

        return True