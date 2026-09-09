class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        


        def dfs(grid , r , c):

            m = len(grid)
            n = len(grid[0])
            if r<0 or c<0 or r>=m or c>=n or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            return(1 +dfs(grid , r+1,c)+
            dfs(grid , r-1 ,c)+
            dfs(grid , r , c+1)+
            dfs(grid , r , c-1))
        m = len(grid)
        n = len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):

                if grid[i][j] == 1:

                    ans = max(ans , dfs(grid,i,j))

        return ans


