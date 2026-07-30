class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = nums[4::]

        for i in range(len(nums) - k):
            arr.append(nums[i])

        nums = arr
        print(nums)