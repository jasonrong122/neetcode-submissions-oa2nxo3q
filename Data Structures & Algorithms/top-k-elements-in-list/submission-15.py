class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = [[] for i in range(len(nums) + 1)]
        hashmap = {}

        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)

        for key, value in hashmap.items():
            arr[value].append(key)
        
        res = []
        for i in range(len(arr) - 1, -1, -1):
            for j in arr[i]:
                res.append(j)
                if len(res) == k:
                    return res

