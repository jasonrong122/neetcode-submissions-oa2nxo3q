class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        directions = [[1, 0], [-1,0], [0, 1], [0, -1]]
        oVisit = set()

        def dfs(r, c, visit):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visit or board[r][c] == "X":
                return
            
            visit.add((r, c))
            board[r][c] = "T"
            for dr, dc in directions:
                dfs(r + dr, c + dc, visit)

        for r in range(rows):
            dfs(r, 0, oVisit)
            dfs(r, cols - 1, oVisit)

        for c in range(cols):
            dfs(0, c, oVisit)
            dfs(rows - 1, c, oVisit)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"