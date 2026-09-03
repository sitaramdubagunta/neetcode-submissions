class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        seen  = set()

        for i in range(len(board)):

            for j in range(len(board[0])):
                boardnum = (i//3) * 3 + j // 3
                if board[i][j] == '.':
                    continue
                if 'r' + str(i)+board[i][j] in seen or 'c' + str(j)+board[i][j] in seen:
                    return False
                if 'b' + str(boardnum)+ board[i][j] in seen:
                    return False 
                seen.add('r' + str(i) + board[i][j])
                seen.add('c' + str(j) + board[i][j])
                seen.add('b' + str(boardnum) + board[i][j])
        return True

        