class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for r in range(len(board)):
            hashsetRows = set()
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue
                if board[r][c] in hashsetRows:
                    return False
                hashsetRows.add(board[r][c])

        # check cols
        for c in range(len(board[0])):
            hashsetCols = set()
            for r in range(len(board)):
                if board[r][c] == ".":
                    continue
                if board[r][c] in hashsetCols:
                    return False
                hashsetCols.add(board[r][c])

        # check 3 x 3
        hashmap = {}
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue
                key = (r // 3, c // 3)

                if key not in hashmap:
                    hashmap[key] = set()

                if board[r][c] in hashmap[key]:
                    return False
            
                hashmap[key].add(board[r][c])

        return True