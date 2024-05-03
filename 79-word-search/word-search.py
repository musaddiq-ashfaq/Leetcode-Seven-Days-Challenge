class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        def dfs(i,j,c):
            if i<0 or j<0 or i>=rows or j>=cols or board[i][j] != word[c]:
                return False
            if c == len(word)-1:
                return True
            temp = board[i][j]
            board[i][j] = "#"
            match = dfs(i+1,j,c+1) or dfs(i-1,j,c+1) or dfs(i,j+1,c+1) or dfs(i,j-1,c+1)
            board[i][j] = temp
            return match  
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        
        return False