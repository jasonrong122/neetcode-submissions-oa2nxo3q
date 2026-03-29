class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) / 2

            if nums[mid] > nums[target]:
                r = mid - 1
            elif nums[mid] < nums[target]:
                l = mid + 1
            else:
                return mid

        return -1