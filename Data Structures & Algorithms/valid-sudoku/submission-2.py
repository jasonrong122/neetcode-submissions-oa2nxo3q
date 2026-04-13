class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(len(board)):
            hashset = set()
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue
                
                if board[r][c] in hashset:
                    return False
                
                hashset.add(board[r][c])

        for c in range(len(board[0])):
            hashset = set()
            for r in range(len(board)):
                if board[r][c] == ".":
                    continue
                
                if board[r][c] in hashset:
                    return False
                
                hashset.add(board[r][c])

        hashmap = {}
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue

                if (r // 3, c // 3) not in hashmap:
                    hashmap[(r // 3, c // 3)] = set()

                if board[r][c] in hashmap[(r // 3, c // 3)]:
                    return False

                hashmap[(r // 3, c // 3)].add(board[r][c])

        return True