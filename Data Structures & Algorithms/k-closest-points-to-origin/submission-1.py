class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        for x, y in points:
            arr.append((x * x + y * y, [x, y]))

        heapq.heapify(arr)
            
        res = []
        while k:
            # res.append(arr[0])
            dist, point = heapq.heappop(arr)
            # heapq.heapify(arr)
            res.append(point)
            k -= 1

        return res