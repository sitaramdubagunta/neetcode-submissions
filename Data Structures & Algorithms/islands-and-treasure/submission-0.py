class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])

        queue = deque()
        for i in range(len(grid)):

            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((1 , i , j))


        directions = [(0,1) , (1,0) , (-1,0) , (0 , -1)]


        while queue:

            for _ in range(len(queue)):

                front = queue.popleft()
                i = front[1]
                j = front[2]
                for nx, ny in directions:

                    if nx+front[1] >= 0 and nx+front[1] < m and ny+front[2] >= 0 and ny+front[2] < n and grid[i+nx][j+ny] != -1 and grid[i+nx][j+ny] != 0:
                         
                        
                        
                        if grid[i+nx][j+ny] == 2147483647:
                            queue.append((front[0]+1 , nx+front[1] , ny+front[2]))
                            grid[i+nx][j+ny] = front[0]
                        

        
