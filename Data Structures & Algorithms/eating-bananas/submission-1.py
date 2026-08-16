class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = 0

        while l <= r:
            time = 0
            mid = (l + r) // 2
            for i in range(len(piles)):
                time += (piles[i] + mid - 1) // mid
            if time == h:
                return mid
            
            if time < h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res