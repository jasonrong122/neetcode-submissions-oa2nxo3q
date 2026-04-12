class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minHeap = []
        hashmap = {}

        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)

        for key, value in hashmap.items():
            heapq.heappush(minHeap, (-value, key))

        res = []
        while k > 0:
            f, v = heapq.heappop(minHeap)
            res.append(v)
            k -= 1

        return res