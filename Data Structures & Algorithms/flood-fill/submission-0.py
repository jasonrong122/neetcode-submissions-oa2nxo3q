class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])

        visit = set()

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        oc = image[sr][sc]
        def dfs(r, c, originalColor):
            if r < 0 or c < 0 or r == rows or c == cols or image[r][c] != originalColor or (r, c) in visit:
                return

            visit.add((r, c))

            image[r][c] = color
            dfs(r + 1, c, originalColor)
            dfs(r - 1, c, originalColor)
            dfs(r, c + 1, originalColor)
            dfs(r, c - 1, originalColor)

        dfs(sr, sc, image[sr][sc])
        # dfs(sr, sc, oc)
        return image