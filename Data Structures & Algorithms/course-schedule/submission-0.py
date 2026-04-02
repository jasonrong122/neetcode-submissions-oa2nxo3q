class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashmap = {}
        hashset = set()

        for src, dst in prerequisites:
            if src not in hashmap:
                hashmap[src] = []
            if dst not in hashmap:
                hashmap[dst] = []
            hashmap[src].append(dst)

        def dfs(src):
            if src in hashset:
                return False

            if hashmap[src] == []:
                return True

            hashset.add(src)
            for dst in hashmap[src]:
                if not dfs(dst):
                    return False
            hashset.remove(src)
            hashmap[src] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True