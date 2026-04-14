class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        combSet = []
        def dfs(i, total):
            if total == target:
                res.append(combSet.copy())
                return
            
            if total > target or i >= len(candidates):
                return

            combSet.append(candidates[i])
            dfs(i, total + candidates[i])

            combSet.pop()
            dfs(i + 1, total)

        dfs(0, 0)

        return res