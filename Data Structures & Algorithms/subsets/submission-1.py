class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        currSet = []

        def dfs(i):
            if i >= len(nums):
                subset.append(currSet[:])
                return

            currSet.append(nums[i])
            dfs(i + 1)

            currSet.pop()
            dfs(i + 1)

        dfs(0)
        return subset
