class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        l = 0
        res = 0

        for r in range(len(s)):
            highestFreq = 0
            if s[r] not in hashmap:
                hashmap[s[r]] = 1
                # highestFreq = max(hashmap.values())
                # while (r - l + 1) - highestFreq > k:
                #     hashmap[s[l]] -= 1
                #     l += 1
            else:
                hashmap[s[r]] += 1
                # highestFreq = max(hashmap.values())
                # while (r - l + 1) - highestFreq > k:
                #     hashmap[s[l]] -= 1
                #     l += 1
            highestFreq = max(hashmap.values())
            while (r - l + 1) - highestFreq > k:
                hashmap[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res