class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for s in strs:
            key = [0] * 26
            for c in s:
                diff = ord(c) - ord("a")
                key[diff] += 1
            if tuple(key) in hashmap:
                hashmap[tuple(key)].append(s)
            else:
                hashmap[tuple(key)] = [s]

        return list(hashmap.values())