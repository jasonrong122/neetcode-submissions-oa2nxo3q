class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # so a single element with weight greater than capacity cannot go on the ship
        # so we know the lower bound is the max weight from the weights array
        # and we can also set the upper bound to be the sum of all weights
        # this optimizes our runtime from a linear search to a logarithmic search
        l = max(weights)
        r = sum(weights)
        ans = r
        while l <= r:
            mid = (l + r) // 2

            ships = 1
            curr_weight = 0
            for weight in weights:
                if curr_weight + weight > mid:
                    curr_weight = weight
                    ships += 1
                else:
                    curr_weight += weight

            if ships <= days:
                ans = min(ans, mid)
                r = mid - 1
            else:
                l = mid + 1

        return ans