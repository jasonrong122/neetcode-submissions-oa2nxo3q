class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combSet = []
        currSet = []

        def dfs(i):
            if len(currSet) == k:
                combSet.append(currSet[:])
                return
            
            if i > n:
                return

            currSet.append(i)
            dfs(i + 1)
            currSet.pop()

            dfs(i + 1)

        dfs(1)

        return combSet