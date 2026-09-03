class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        bucket = [[]  for _ in range(len(nums)+1)]


        for i , j  in count.items():

            bucket[j].append(i)
        cnt = 0
        res = []
        for i in range(len(bucket) - 1 , -1 , -1):

            for num in bucket[i]:
                if cnt == k:
                    return res
                cnt += 1
                res.append(num)

        return res


        