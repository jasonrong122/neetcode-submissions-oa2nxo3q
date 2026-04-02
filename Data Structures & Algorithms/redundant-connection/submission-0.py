class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adjList = { i : [] for i in range(1, n + 1) }

        def hasPath(src, dst, visit):
            if src == dst:
                return True

            visit.add(src)
            for nei in adjList[src]:
                if nei not in visit:
                    if hasPath(nei, dst, visit):
                        return True
            return False

        for u, v in edges:
            if hasPath(u, v, set()):
                return [u, v]

            adjList[u].append(v)
            adjList[v].append(u)