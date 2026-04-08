class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [""]

        hashmap = {}

        for s in strs:
            sSorted = sorted(s)
            if tuple(sSorted) in hashmap:
                hashmap[tuple(sSorted)].append(s)
            else:
                hashmap[tuple(sSorted)] = [s]

        res = []
        for k, v in hashmap.items():
            res.append(v)

        return res