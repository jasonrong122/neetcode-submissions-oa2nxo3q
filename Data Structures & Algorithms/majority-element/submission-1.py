class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}

        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)

        res = 0
        val = 0
        for k, v in hashmap.items():
            if v > val:
                res = k
                val = v

        return res