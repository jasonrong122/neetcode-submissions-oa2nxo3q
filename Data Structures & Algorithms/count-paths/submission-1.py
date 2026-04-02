class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows = m
        cols = n

        prevRow = [0] * cols
        # prevRow[rows - 1][cols - 1] = 1
        prevRow[cols - 1] = 1

        for r in range(rows - 1, -1, -1):
            currRow = [0] * cols
            for c in range(cols - 1, -1, -1):
                rightVal = currRow[c + 1] if c + 1 < cols else 0
                currRow[c] = rightVal + prevRow[c]
            prevRow = currRow 

        return prevRow[0]