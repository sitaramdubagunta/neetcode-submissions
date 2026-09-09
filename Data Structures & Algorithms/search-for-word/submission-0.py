class Solution:

    def dfs(self , board, i , j , word , array , visited):
        if len(word) == len(array):

            return ''.join(array) == word

        if i<0 or j <0 or i>=len(board) or j>= len(board[0]) or visited[i][j]:
            return False
        if board[i][j] != word[len(array)]:
            return False
        visited[i][j] = True
        array.append(board[i][j])
        if(self.dfs(board , i+1 , j , word , array,visited) or 
        self.dfs(board , i-1 , j , word , array,visited) or 
        self.dfs(board , i , j+1 , word , array,visited) or 
        self.dfs(board , i , j-1 , word , array,visited)):
            return True
        visited[i][j] = False
        array.pop()
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited = [  [False] * len(board[0])  for i in range(len(board))]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if not visited[i][j]:
                    if self.dfs(board , i , j , word ,[] , visited ):
                        return True

        return False