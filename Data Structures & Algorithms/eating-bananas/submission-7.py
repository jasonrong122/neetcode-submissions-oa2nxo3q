class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # so koko can eat a minimum of 1 banana per hour
        # and koko can eat a max of max(piles) bananas per hour
        # we can use this search range space to help reduce time complexity from a linear algorithm to logarithmic by using [1, max[piles]]
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            mid = (l + r) // 2

            temp_h = 0
            for pile in piles:
                temp_h += math.ceil(pile / mid)
            
            if temp_h <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1

        return res