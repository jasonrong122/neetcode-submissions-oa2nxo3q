class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        visit = set()
        q.append((0, 0))
        visit.add((0, 0))

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1],
                      [1, -1], [1, 1], [-1, -1], [-1, 1]]

        length = 0

        while q:
            length += 1
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    if r == rows - 1 and c == cols - 1:
                        return length

                    if r + dr < 0 or r + dr >= rows or c + dc < 0 or c + dc >= cols or grid[r + dr][c + dc] == 1 or (r + dr, c + dc) in visit:
                        continue

                    q.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))

            

        return -1