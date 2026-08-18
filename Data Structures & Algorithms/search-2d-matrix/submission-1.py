class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bottom = rows - 1

        # finding the correct row
        while top <= bottom:
            mid = (top + bottom) // 2
            if matrix[mid][0] > target:
                bottom = mid - 1
            elif matrix[mid][-1] < target:
                top = mid + 1
            else:
                break

        if not (top <= bottom):
            return False

        l = 0
        r = cols - 1
        row = (top + bottom) // 2
        while l <= r:
            mid = (l + r) // 2

            if matrix[row][mid] == target:
                return True

            if matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False