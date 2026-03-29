class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        currSet = []
        candidates.sort()

        def dfs(i, currSum):
            if currSum == target:
                if currSet not in res:
                    res.append(currSet.copy())
                return

            if currSum > target:
                return
            
            if i >= len(candidates):
                return

            currSet.append(candidates[i])
            dfs(i + 1, currSum + candidates[i])
            currSet.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, currSum)

        dfs(0, 0)
        return res 