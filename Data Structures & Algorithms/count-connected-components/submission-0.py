class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = { i : [] for i in range(n)}
        count = 0
        for n1, n2 in edges:
            adjList[n1].append(n2)
            # undirected graph so maybe we add n1? but might also not need
            adjList[n2].append(n1)

        visit = set()
        def dfs(node):
            visit.add(node)
            for nei in adjList[node]:
                if nei not in visit:
                   dfs(nei)

        for i in range(n):
            if i not in visit:
                count += 1
                dfs(i)

        return count