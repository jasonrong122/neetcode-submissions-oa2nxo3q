class Solution:
    def climbStairs(self, n: int) -> int:
        def memoization(n, cache):
            if n <= 3:
                cache[n] = n
                return cache[n]

            if n in cache:
                return cache[n]

            cache[n] = memoization(n - 1, cache) + memoization(n - 2, cache)
            return cache[n]
        
        return memoization(n, {})