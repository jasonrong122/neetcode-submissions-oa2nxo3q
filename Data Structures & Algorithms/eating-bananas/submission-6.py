class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            time = 0
            mid = l + ((r - l) // 2)
            for i in range(len(piles)):
                time += math.ceil(piles[i] / mid)
            
            if time <= h:
                res = min(mid, res)
                r = mid - 1
            else:
                l = mid + 1
        
        return res