class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            col_hashmap = {}
            row_hashmap = {}
            for c in range(cols):
                if board[r][c] != ".":
                    if board[r][c] in row_hashmap:
                        return False
                    row_hashmap[board[r][c]] = 1

                if board[c][r] != ".":
                    if board[c][r] in col_hashmap:
                        return False
                    col_hashmap[board[c][r]] = 1

        for box_r in range(0, 9, 3):
            for box_c in range(0, 9, 3):
                box_hashmap = {}
                for r in range(box_r, box_r + 3):
                    for c in range(box_c, box_c + 3):
                        if board[r][c] != ".":
                            if board[r][c] in box_hashmap:
                                return False
                            box_hashmap[board[r][c]] = 1

        return True