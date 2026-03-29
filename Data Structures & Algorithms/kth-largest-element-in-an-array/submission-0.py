class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, -num)

        res = 0
        while k > 0:
            res = heapq.heappop(minHeap)
            k -= 1

        return -res