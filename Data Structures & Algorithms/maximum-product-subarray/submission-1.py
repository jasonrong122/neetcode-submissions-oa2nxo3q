class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = 0

        for i in range(len(nums)):
            temp = nums[i]
            res = max(res, temp)
            for j in range(i + 1, len(nums)):
                temp *= nums[j]
                res = max(res, temp)

        return res