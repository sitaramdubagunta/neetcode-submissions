class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        

        task_counter = Counter(tasks)

        taskheap = [  -freq for item , freq in task_counter.items()]


        heapq.heapify(taskheap)

        queue = deque()
        time = 0
        while queue or taskheap:


            time += 1

            if queue and queue[0][1] == time:
                heapq.heappush(taskheap , queue.popleft()[0])

            if taskheap:

                freq = heapq.heappop(taskheap) + 1
                if freq != 0:

                    queue.append((freq , time + n + 1))


        return time