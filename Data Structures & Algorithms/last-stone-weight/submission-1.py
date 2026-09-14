class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        

        stones = [-stone for stone in stones]

        heapq.heapify(stones)

        while stones:

            x = heapq.heappop(stones)
            if stones:
                y = heapq.heappop(stones)
            else:
                return -x

            if x-y != 0:
                heapq.heappush(stones , x-y)

        return 0


