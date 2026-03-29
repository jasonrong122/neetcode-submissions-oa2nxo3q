class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(i + 2, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        arr.append([nums[i], nums[j], nums[k]])

        return arr
