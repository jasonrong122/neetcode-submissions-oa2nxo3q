class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        q = deque()
        visit = set()

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                
                if grid[r][c] == 2:
                    q.append((r, c))
                    visit.add((r, c))

        # q = deque()
        # visit = set()
        # q.append((0, 0))
        # visit.add((0, 0)) # might be wrong because we might want to initialize all rotten oranges to visit
        time = 0
        while q:
            if fresh > 0:
                time += 1
            for i in range(len(q)):
                r, c = q.popleft()
                
                # this problem wants us to set the fresh orange to rotten so i can simply do grid[r][c] = 2, but i want to try visit
                # visit.add((r, c))
                for dr, dc in directions:
                    if r + dr < 0 or r + dr >= rows or c + dc < 0 or c + dc >= cols or (r + dr, c + dc) in visit or grid[r + dr][c + dc] != 1:
                        continue    
                    fresh -= 1
                    visit.add((r + dr, c + dc))
                    q.append((r + dr, c + dc))
            

        if fresh == 0:
            return time
        return -1


