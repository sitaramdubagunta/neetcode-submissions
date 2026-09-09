class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ans = []
        visited_pacific = set()
        visited_atlantic = set()
        def dfs(r , c , heights , prevheight , visited):

            if(r < 0 or c<0 or r>= len(heights) or c>=len(heights[0]) or (r,c) in visited):
                return
            if(prevheight> heights[r][c]):
                return

            visited.add((r,c))
            dfs(r+1,c,heights,heights[r][c] , visited)
            dfs(r-1,c,heights,heights[r][c] , visited)
            dfs(r,c+1,heights,heights[r][c] , visited)
            dfs(r,c-1,heights,heights[r][c] , visited)
        colno = len(heights[0]) 
        
        for row in range(len(heights)):

            dfs(row , 0 , heights, heights[row][0] , visited_pacific)
            dfs(row ,colno-1, heights ,heights[row][colno-1] , visited_atlantic)

        for col in range(colno):
            dfs(0 , col , heights,heights[0][col] , visited_pacific)
            dfs(len(heights)-1,col , heights,heights[len(heights)-1][col],visited_atlantic)
        

        for row in range(len(heights)):
            for col in range(len(heights[0])):

                if (row,col) in visited_pacific and (row,col) in visited_atlantic:
                    ans.append((row,col))

        return ans

        