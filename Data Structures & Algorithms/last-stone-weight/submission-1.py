class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            y = heappop_max(stones)
            x = heappop_max(stones)

            if x != y:
                heappush_max(stones, y - x)

        if len(stones) < 1:
            return 0
        return stones[0]