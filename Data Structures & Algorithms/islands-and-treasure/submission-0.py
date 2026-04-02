class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        INF = 2147483647

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        q = deque()
        # we might actually not need a set since we are modifying characters in place
        # visit = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))

        # now we perform bfs
        count = 1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    if r + dr < 0 or c + dc < 0 or r + dr >= rows or c + dc >= cols or grid[r + dr][c + dc] != INF:
                        continue
                    
                    grid[r + dr][c + dc] = count
                    q.append((r + dr, c + dc))

            count += 1