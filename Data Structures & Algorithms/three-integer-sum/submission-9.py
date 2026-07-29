class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        hashset = set()
        # i = 0
        # j = 1
        # k = 2
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = tuple(sorted((nums[i], nums[j], nums[k]
                        )))
                        if triplet not in hashset:
                            hashset.add(triplet)

        return list(hashset)