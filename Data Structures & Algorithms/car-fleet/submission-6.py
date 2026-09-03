class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:


        cars = []

        for i in range(len(position)):

            cars.append((position[i] , speed[i]))


        cars = sorted(cars , reverse = True)


        stack = []

        times = [ (target - cars[i][0]) / cars[i][1] for i in range(len(position))]
        stack.append(times[0])

        for time in times[1:]:


            if time > stack[-1]:
                stack.append(time)

        return len(stack)
        