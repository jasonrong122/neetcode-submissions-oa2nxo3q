class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) == 0:
            return True

        hashmap = { i : [] for i in range(n) }
        for root, leaf in edges:
            hashmap[root].append(leaf)
            hashmap[leaf].append(root)
        
        visit = set()
        def dfs(i, prev):
            if i in visit:
                return False

            visit.add(leaf)
            for j in hashmap[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False

            return True

        return dfs(0, -1) and n == len(visit) 