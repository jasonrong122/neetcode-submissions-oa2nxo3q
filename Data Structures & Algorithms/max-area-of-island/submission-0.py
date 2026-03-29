class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0

        directions = [[1,0], [-1,0], [0, 1], [0, -1]]

        visit = set()

        def bfs(r, c):
            # do bfs later
            q = deque()
            q.append((r, c))
            visit.add((r, c))

            count = 1
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if (nr in range(rows) and
                        nc in range(cols) and
                        grid[nr][nc] == 1 and
                        (nr, nc) not in visit):
                        q.append((nr, nc))
                        visit.add((nr, nc))
                        count += 1
            
            return count

        tempArea = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] and (r, c) not in visit:
                    tempArea = bfs(r , c)
                    maxArea = max(maxArea, tempArea)

        return maxArea