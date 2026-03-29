class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        res = high

        while low <= high:
            mid = (low + high) // 2

            total = 0
            for p in piles:
                total += (p + mid - 1) // mid
            
            if total <= h:
                res = mid
                high = mid - 1
            else:
                low = mid + 1

        return res