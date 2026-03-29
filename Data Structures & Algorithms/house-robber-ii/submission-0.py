class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.robHelper(nums[1:]), self.robHelper(nums[:-1]))

    def robHelper(self, nums):
        rob1 = 0
        rob2 = 0

        for i in range(len(nums)):
            newRob = max(rob1 + nums[i], rob2)
            rob1 = rob2
            rob2 = newRob

        return rob2