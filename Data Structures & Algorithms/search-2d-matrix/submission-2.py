class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bot = rows - 1
        row = 0
        while top <= bot:
            mid = (top + bot) // 2

            if target < matrix[mid][0]:
                bot = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            # we found the correct row
            else:
                row = mid
                break

        if top > bot:
            return False

        # now that we found the right row, we perform binary search on that row

        l = 0
        r = cols - 1

        while l <= r:
            mid = (l + r) // 2
            
            if matrix[row][mid] == target:
                return True
            
            if matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False