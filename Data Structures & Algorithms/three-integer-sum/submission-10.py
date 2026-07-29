class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        hashset = set()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        hashset.add(tuple(sorted((nums[i], nums[j], nums[k]))))

        return [list(t) for t in hashset]