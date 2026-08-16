class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = sum(weights)

        while l <= r:
            mid = (l + r) // 2
            ships = 1

            curr_weight = 0
            for i in range(len(weights)):
                curr_weight += weights[i]

                if curr_weight > mid:
                    curr_weight = weights[i]
                    ships += 1
            
            if ships <= days:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1

        return res