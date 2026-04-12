class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for s in strs:
            arr = [0] * 26

            for c in s:
                arr[ord(c) - ord('a')] += 1
            
            key = tuple(arr)
            if key in hashmap:
                hashmap[key].append(s)
            else:
                hashmap[key] = [s]

        return list(hashmap.values())