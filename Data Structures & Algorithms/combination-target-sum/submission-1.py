class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        currSet = []

        def dfs(i, currSum):
            if currSum == target:
                res.append(currSet[:])
                return

            if currSum > target:
                return
            
            if i >= len(candidates):
                return

            currSet.append(candidates[i])
            dfs(i, currSum + candidates[i])

            currSet.pop()
            dfs(i + 1, currSum)

        dfs(0, 0)

        return res