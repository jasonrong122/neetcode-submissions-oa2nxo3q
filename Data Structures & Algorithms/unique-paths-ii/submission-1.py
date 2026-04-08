class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        
        m = len(obstacleGrid) # rows
        n = len(obstacleGrid[0]) # columns
        cache = {}
        # we can only go down and right not up and left 
        def dfs(r, c):
            if r >= m or c >= n or obstacleGrid[r][c] == 1:
                return 0

            if r == m - 1 and c == n - 1:
                return 1

            # if obstacleGrid[r][c] in cache:
            #     return cache[r][c]
            if (r, c) in cache:
                return cache[(r, c)]
            
            cache[(r, c)] = dfs(r, c + 1) + dfs(r + 1, c)
            return cache[(r, c)]
            
        return dfs(0, 0)