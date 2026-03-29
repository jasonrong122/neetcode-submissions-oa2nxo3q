class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = 0

        for i in range(len(nums)):
            currSum = nums[i]
            for j in range(i + 1, len(nums)):
                currSum += nums[j]
                maxSum = max(maxSum, currSum)
        
        return maxSum